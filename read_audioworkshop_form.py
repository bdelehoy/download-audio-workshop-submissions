from csv import reader
import subprocess

### Originally written by Brandon Delehoy
### for the Audio Department of the Video Game Development Club at UC Irvine
### twitter: @_brandolf

# CSV format for each row:
# row[0]: timestamp (not really needed)
# row[1]: submitter's name
# row[2]: 'Yes'/'No' (attending the workshop?)
# row[3]: ***THE LINK***

# change this to whatever path the csv is located in
my_csv_path = './example_form.csv'

print("Please open this python script and edit my_csv_path with the path of your survey results in CSV form.")

with open(my_csv_path) as f:
    my_reader = reader(f)
    print("CSV file successfully read: {}".format(my_csv_path))
    #print("CSV file successfully read: {}\nFound {} videos to download".format(my_csv_path, sum(1 for row in my_reader)-1))
    # wanted to print out amount of entries, but... generators.... (cannot read anymore since we exhausted it)
    input("Press Enter to continue...")
    count = 1
    for row in my_reader:
        # skip the first row (it's a header)
        if row[3] != 'Streaming link to your song choice:':
            # if the person is attending, place them higher in the file order (so their submission shows up first)
            if row[2] == "Yes":
                # add an "_" at the beginning to their file to put them at the top
                debug_print = "{} (who is attending) submitted: {}\n   Downloading now....".format(row[1], row[3])
                path_to_download_to = "~/Downloads/_{}_{}_%(title)s_%(id)s.%(ext)s".format(count, row[1].replace(" ", "_"))
            else:
                # there's no "_" at the beginning, so their file will be at the bottom
                debug_print = "{} (NOT attending) submitted: {}\n   Downloading now....".format(row[1], row[3])
                path_to_download_to = "~/Downloads/{}_{}_%(title)s_%(id)s.%(ext)s".format(count, row[1].replace(" ", "_"))
            
            youtube_dl_string = 'youtube-dl -x --audio-format mp3 -o {} --no-check-certificate --no-playlist '.format(path_to_download_to)
            print ("\n{}\n".format(count))
            print(debug_print)
            print("EXECUTE:", youtube_dl_string)
            subprocess.call(youtube_dl_string+row[3])
            count += 1
    print("\n\nDone!")
    print("If youtube-dl spat out any errors, try updating it with\n   youtube-dl -U")
    print("(you might need to run cmd or Powershell in Administrator Mode to do that)")
