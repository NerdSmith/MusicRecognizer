import logging
import wave

import numpy as np
import pyaudio
from definitions import (DEFAULT_FRAMES,
                         CHUNK,
                         FORMAT,
                         RATE,
                         RECORD_SECONDS,
                         EXCERPT_PATH)


class Recorder(pyaudio.PyAudio):
    def __init__(self):
        super().__init__()

        self.stream = None
        self.devices = self._get_valid_devices()

        try:
            self.default_device = self.devices[0]
        except IndexError as e:
            logging.error("devices not found")
            raise Exception("devices not found")

        logging.info("devices have been found")

    def _get_valid_devices(self):
        devices = []
        for i in range(0, self.get_device_count()):
            info = self.get_device_info_by_index(i)
            is_wasapi = (self.get_host_api_info_by_index(info["hostApi"])["name"]).find("WASAPI") != -1
            is_input = info["maxInputChannels"] > 0
            is_output = info["maxOutputChannels"] > 0
            device_type = "in" if is_input else ("out" if is_output else None)
            if is_wasapi:
                devices.append({"index": i,
                                "type": device_type,
                                "name": str(info["name"]),
                                "defaultSampleRate": info["defaultSampleRate"]}
                               )
        return devices

    def _get_device_from_list(self, idx):
        for list_idx in range(len(self.devices)):
            if self.devices[list_idx].get("index") == idx:
                return self.devices[list_idx]
        return None

    def set_default_device(self, sys_device_idx):
        if sys_device_idx != -1:
            device = self._get_device_from_list(sys_device_idx)
            if device is not None:
                self.default_device = device

    def record(self, sys_device_idx=-1):
        self.set_default_device(sys_device_idx)

        try:
            self.stream = self.open(
                format=FORMAT,
                channels=2 if self.default_device.get('type') == "out" else 1,
                rate=int(self.default_device.get('defaultSampleRate')),
                input=True,
                frames_per_buffer=DEFAULT_FRAMES,
                input_device_index=self.default_device.get('index'),
                as_loopback=self.default_device.get('type') == "out")
            frames = []

            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = self.stream.read(CHUNK)
                frames.append(data)

            frames = b''.join(frames)

            decoded = np.frombuffer(frames, 'int16')

            if self.default_device.get('type') == "out":
                decoded = decoded[1::2] + decoded[::2]

            signal = np.clip(decoded, -32767, 32766)
            packed_signal = wave.struct.pack("%dh" % (len(signal)), *list(signal))

            self.stream.stop_stream()
            self.stream.close()

            wf = wave.open(EXCERPT_PATH, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(self.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(packed_signal)
            wf.close()
            return True

        except Exception as e:
            logging.error(f"record error {e}")
            self.close_channels()
            return False

    def close_channels(self):
        if self.stream.is_active():
            self.stream.stop_stream()
            self.stream.close()

    def get_devices(self):
        return self.devices


if __name__ == '__main__':
    rec = Recorder()
    rec.record()
