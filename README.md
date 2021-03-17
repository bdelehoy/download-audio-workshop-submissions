This Python 3 script accepts a CSV file of Google Form responses, converts all youtube links inside to MP3 files, and organizes them in a folder of your choice (defaults to your Downloads folder). Download it with the big green "Clone or Download" button up there^ somewhere and download the ZIP.

I've confirmed that this script works with Windows 10.  Some modification *may* be required for use with other platforms, although youtube-dl does a good job of santizing file paths.

Run it like this in a command prompt or terminal:

`python read_audioworkshop_form.py C:/path/to/your/form.csv C:/path/to/your/folder/of/choice/`

Requires the programs `youtube-dl`, `ffmpeg`, and `Python 3`. Get them all here:

* [youtube-dl](https://rg3.github.io/youtube-dl/)
    * [youtube-dl downloads page](https://ytdl-org.github.io/youtube-dl/download.html) - you need the "Windows .exe" and also the C++ package that they mention here at the top of the page. Make a folder for it where it's safe (`C:\Program Files\youtube-dl` for example) and put `youtube-dl.exe` in there. Remember this.
* [ffmpeg](https://www.ffmpeg.org/download.html)
    * [ffmpeg Windows build](https://ffmpeg.zeranoe.com/builds/) - Make sure you download "Static" linking. Just like with `youtube-dl`, make a folder for it somewhere and put *everything* from the .zip you download in there. Observe that `ffmpeg.exe` is in the `/bin/` folder. Remember this.
* [Python 3](https://www.python.org/downloads/) - This should be fairly straightforward to install. See the note [1] at the bottom of this document.

`youtube-dl` and `ffmpeg` need to be in your system's PATH variable, which just means that you need to be able to run those programs from anywhere in a command prompt. Here's how to do that on Windows 10:

1. Open the Control Panel (just type "Control Panel" on the Start menu)
2. Click "System"
3. Click "Advanced System Settings" on the left panel
4. Click "Environment Variables"
5. In the upper "User Variables for..." list, find "Path". Click on it and then click the "Edit" button just below the list. This should open up a window that has a neat list of every folder in PATH right now.
6. Open a file explorer and navigate to the folder you want to add. Click on the file address bar and copy it.
7. In the Path editing window that opened in step 5, click "New" on the top-right and paste in the address from step 6.
8. Click "OK".

Run these steps for the folders you made that contain the files `youtube-dl.exe` and `ffmpeg.exe`. Remember that you should find `ffmpeg.exe` in the `/bin/` folder wherever you put `ffmpeg` before. Now that these folders are on your PATH variable, any program inside them can now be run from anywhere on your computer.

* [1] If typing `python` in the command prompt does nothing, then a possible error could be that Python isn't on your PATH. If you're installing Python for the first time, there should be an option somewhere to add Python to your PATH variable. Make sure that box is ticked! If you have Python installed already but it's not on your PATH, you can always add it yourself with the steps above. If you're on Windows, I think its default folder should be somewhere in `C:\Program Files\`, or maybe `C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\` - you're looking for the folder that has `python.exe`.

* [2] If there's further trouble with `youtube-dl` throwing up "ffprobe or avprobe not found", here's [a helpful thread on stackoverflow](https://stackoverflow.com/a/38878753).
    * Most youtube-dl problems should be solvable by updating it in an elevated/admin terminal: `youtube-dl -U`
