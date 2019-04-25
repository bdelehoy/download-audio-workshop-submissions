This Python 3 script accepts a CSV file of Google Form responses, converts all youtube links inside to MP3 files, and organizes them in a folder of your choice (defaults to your Downloads folder). Download it with the big green "Clone or Download" button up there^ somewhere and download the ZIP.

I've confirmed that this script works with Windows 10.  Some modification *may* be required for use with other platforms, although youtube-dl does a good job of santizing file paths.

Run it like this in a command prompt or terminal:

`python read_audioworkshop_form.py C:/path/to/your/form.csv C:/path/to/your/folder/of/choice`

Requires the programs `youtube-dl` and `ffmpeg` in your PATH variable. And Python 3. Get them here:

* [youtube-dl](https://rg3.github.io/youtube-dl/)
    * [youtube-dl downloads page](https://ytdl-org.github.io/youtube-dl/download.html) - you need the Windows .exe and also the C++ package that they mention here. Install that package and youtube-dl should just  work in a command prompt.
* [ffmpeg](https://www.ffmpeg.org/download.html)
    * [ffmpeg Windows build](https://ffmpeg.zeranoe.com/builds/) - this should be what you need if you want to run this Python script on a Windows machine.

(I'd recommend making a folder in Program Files so you can put these where they seem fit, but you do you. Just don't put them anywhere where they could be deleted.)

* [and Python 3.](https://www.python.org/)

How to edit your PATH variable on Windows 10:

1. Open the Control Panel (just type "Control Panel" on the Start menu)
2. Click "System"
3. Click "Advanced System Settings" on the left panel
4. Click "Environment Variables"
5. In the upper list, find "Path". Click on it and then click the "Edit" button just below the list. This should open up a window that has a neat list of every folder currently in your PATH right now - it could be empty, it could not.
6. Open a file explorer and navigate to the folder you want to add. Click on the file address bar and copy it.
7. In the Path editing window that opened in step 5, click "New" on the top-right and paste in the address from step 6.
8. Click "OK" and close all the windows that popped up. You're done!

Run these steps for the folders that contain the files `youtube-dl.exe` and `ffmpeg.exe`. You should find the ffmpeg .exe's in the `/bin` folder. `/bin` is short for "binary" and this is where you can find executable programs in lots of applications. These programs can now be called from anywhere you are on your computer, which this Python script relies on.

* If typing `python` in the command prompt does nothing, then a possible error could be that Python isn't on your PATH. If you're installing Python for the first time, there should be an option somewhere to add Python to your PATH variable. Make sure that box is ticked! If you have Python installed already but it's not on your PATH, you can always add it yourself with the steps above. If you're on Windows, I think its default folder should be somewhere in `C:\Program Files\`, or maybe `C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\` - you're looking for the folder that has `python.exe`.

* If there's further trouble with `youtube-dl` throwing up "ffprobe or avprobe not found", here's [a helpful thread on stackoverflow](https://stackoverflow.com/a/38878753).
    * Most youtube-dl problems should be solvable by updating it in an elevated/admin terminal: `youtube-dl -U`
