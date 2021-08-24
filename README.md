# MusicRecognizer

## Music recognition application for windows  
![alt-text](https://github.com/NerdSmith/MusicRecognizer/blob/master/screenshots/MR_v0.8.0.png?raw=true)

You can choose from which of the devices the recording will be made.

If you choose speakers, everything that you hear will be recorded.
If you have chosen a microphone, everything that comes from it will be recorded, as an option, you can bring your phone with music on to recognize it.
The recognized tracks will be added to the history, which can be cleared or exported to a CSV file. when you click on a story item, the cover will appear in the window.
You can also search for a track on YouTube, Shazam and Spotify.

# Usage

You can use the compiled application from the release.  
![alt-text](https://raw.githubusercontent.com/NerdSmith/MusicRecognizer/master/screenshots/curr_release.png)  
Just download the archive, unzip it to the location you need and run Music Recognizer.exe  
You can also run the application from source files (how to install source files and dependencies is shown in the next chapter)

# Installation

You can install the application from the source code.  
For this you need to download Python v3.7 (the application has not been tested on other versions) from https://www.python.org/downloads/.

Install and activate the virtual environment  
(how to do this see the link https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)  
Install requirements file using pip (make sure the virtual environment is activated (the inscription (venv) will be before the console input))  
```
pip install -r requirements.txt
```  
Run main.py from source location 
```
py main.py
```
