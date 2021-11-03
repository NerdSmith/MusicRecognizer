# MusicRecognizer

## Music recognition application for windows  
![alt-text](https://github.com/NerdSmith/MusicRecognizer/blob/master/screenshots/MR_v0.8.0.png?raw=true)

You can choose from which of the devices the recording will be made.

If you choose speakers, everything that you hear will be recorded (e.g. when you want to recognize music from 
[Coub](https://coub.com/), [TikTok](https://www.tiktok.com/), [YouTube](https://www.youtube.com/), etc.  
But if you have chosen a microphone, everything that comes from it will be recorded (you can bring your phone with music on to recognize it).  
The recognized songs will be added to the history, which can be cleared or exported to a CSV file. When you click on a history item, the cover will appear in the window.
You can also search for the found song on [YouTube](https://www.youtube.com/), [Shazam](https://www.shazam.com/) and [Spotify](https://open.spotify.com/) using the buttons.

# Usage

You can use the compiled application from the release.  
![alt-text](https://raw.githubusercontent.com/NerdSmith/MusicRecognizer/master/screenshots/curr_release.png)  
Just download the archive, unzip it to the location you need and run Music Recognizer.exe  
You can also run the application from source files (how to install source files and dependencies is shown in the next chapter)

# Installation

You can install the application from the source code.  
For this you need to download [Python v3.7](https://www.python.org/downloads/) (the application has not been tested on other versions).

Install and activate the virtual environment (how to do it see [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/))  
Install requirements file using pip (make sure the virtual environment is activated (the inscription (venv) will be before the console input))  
```
pip install -r requirements.txt
```  
Run main.py from source location 
```
py main.py
```
