from csv import reader  # To parse the CSV file that you download from Google Forms
from sys import argv    # To read the command-line arguments
import subprocess       # To call youtube-dl (see the readme file)

### Originally written by Brandon Delehoy
### for the Audio Department of the Video Game Development Club at UC Irvine

# CSV format for each row (if you modify the survey in the future, make sure to see if this changes!):
# row[0]: timestamp (not really needed)
# row[1]: submitter's name
# row[2]: 'Yes'/'No'/'Maybe' (are they attending the workshop?)
# row[3]: ***THE LINK***

###########
### STARTUP
# the folder that all the files should be downloaded to - by default:
#             "~/Downloads/"    (the '~' means "home" and is standard on Linux... and Windows too, apparently!)
# if this default throws up errors, just use this instead:
#             "C:/Users/YOUR_USER_NAME_HERE/Downloads/"
DOWNLOAD_TO = "~/Downloads/"

if len(argv) == 1:
    # if no arguments were provided, display a help string
    print("\n************************************************************************************")
    print("*** ~ Bulk YouTube to MP3 Downloading Script For Audio Department Survey Forms ~ ***")
    print("************************************************************************************")
    
    print("\nHOW TO USE:")
    
    print("\nSupply a valid path to a CSV file as a command-line parameter, and optionally a folder to download everything to.")
    print("Example:\n\t\tpython read_audioworkshop_form.py ./example_form.csv C:/Users/Brandon/Downloads/Workshop04242019/")
    
    print("\nIf you're going to change the format of the survey in the future, feel free to modify this script as needed. I've tried to document it well, but if anything's unclear please let me know!")
    
    print("\nand please read the readme if any errors pop up ty")
    exit(0)
else:
    MY_CSV_PATH = argv[1]
    print("Will attempt to download links from:\t"+MY_CSV_PATH)
    # check if the file provided ends in ".csv"
    if len(MY_CSV_PATH) >= 4 and MY_CSV_PATH[-4:].lower() != ".csv":
        raise Exception("Please provide a path to a CSV file. You wrote:\n>>\t" + MY_CSV_PATH)
    # now check if any specific download folders were provided and sanitize:
    if len(argv) >= 3:
        DOWNLOAD_TO = argv[2]
        # this is where cross-platform file paths would have to be specified - also later on in path_to_download_to.
        if DOWNLOAD_TO[-1] not in "\\/":
            raise Exception("Please add your operating system's file path separator to the end of your specified download folder:\n\tWindows: \t\\\n\tLinux/OS X: \t/\nYou wrote:\n>>\t" + DOWNLOAD_TO)

print("Will download files to:\t\t\t"+DOWNLOAD_TO)

###################
### THE DOWNLOADIN'
with open(MY_CSV_PATH) as f:
    my_reader = reader(f)
    print("CSV file successfully opened.")
    #print("CSV file successfully read: {}\nFound {} videos to download".format(MY_CSV_PATH, sum(1 for row in my_reader)-1))
    # wanted to print out amount of entries, but... generators.... (cannot read anymore since we exhausted it)
    print("\nRemember to UPDATE youtube-dl if any weirdness comes up, like errors or missing titles.")
    print("To do that, run the following command:\n\tyoutube-dl -U\nin an admin command prompt or terminal.")
    input("\nPress Enter to continue...\n")
    count = 1
    for row in my_reader:
        # skip the first row (it's a header)
        if row[0] != 'Timestamp':
            # if the person is attending or could be attending, place them higher in the file order (so their submission shows up first)
            persons_name = row[1].replace(" ", "_") # replace the spaces in their name to underscores; for use in naming the file that we download to
            attending = ''
            path_to_download_to = DOWNLOAD_TO
            if row[2] == "Yes":
                path_to_download_to += "__"     # add an "__" at the beginning to their file to put them at the top
            elif row[2] == "Maybe":
                path_to_download_to += "_"      # add "_" at the beginning to their file to put them in a second, middle category
            # if the person's not attending, no extra formatting is needed and theirs will sort to the bottom by default
            path_to_download_to += "{}_{}___%(title)s_%(id)s.%(ext)s".format(count, persons_name)
            
            print("** Submission #{}:".format(count))
            print("** \tName:\t\t" + row[1])
            print("** \tAttending?\t" + row[2].upper())
            print("** \tSubmitted at:\t" + row[0])
            print("** \tLink:\t\t" + row[3])
            print("** \tSaving to:\t" + path_to_download_to)
            
            # the string that we use to call youtube-dl, with all of its own arguments and flags
            youtube_dl_string = 'youtube-dl -x --audio-format mp3 -o {} --no-check-certificate --no-playlist {}'.format(path_to_download_to, row[3].strip())
            # if you want to keep all the videos, use the following string instead:
            # youtube_dl_string = 'youtube-dl -x --audio-format mp3 -o {} --no-check-certificate --no-playlist {} -k'.format(path_to_download_to, row[3].strip())
            
            print("** EXECUTE:\n** "+youtube_dl_string)
            subprocess.call(youtube_dl_string)   # call youtube-dl! this could take a while.
            
            print ("\n** Submission {} complete.\n".format(count))
            count += 1
    print("\nDone!")
    print("If youtube-dl spat out any errors, try updating it with\n   youtube-dl -U")
    print("(you might need to run cmd or Powershell in Administrator Mode to do that)")
