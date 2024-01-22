import os
import sys
from pytube import YouTube

# Arguments validation
num_arguments = len(sys.argv)

if(num_arguments<1 or num_arguments>3):
    print("Please input valid arguments.\nSyntax: python musicdownloader.py {url} {file path (optional)}")
    os._exit(0)

# Ask for Arguments
def menu(num_arguments):
    if(num_arguments==1):
        def menu_link():
            print('Input YouTube Link: ')
            link = input()
            return link

        def menu_filepath():
            print('Specify file path? (Y/N)')
            usefilepath = input()

            if(usefilepath=='Y'):
                print('Input file path: ')
                destination = input()
                return destination
            elif(usefilepath=='N'):
                destination = "Downloads/"
                return destination
            else:
                menu_filepath()

        print('YouTube Music Downloader')
        link = menu_link()
        destination = menu_filepath()
    else:
        # Get arguments
        link = sys.argv[1]
        if(num_arguments==3):
            destination = sys.argv[2]
        else:
            destination = "Downloads/"

    return link, destination

def download(link, destination):
    # Download the file
    yt = YouTube(link)
    audio = yt.streams.filter(only_audio=True).first()

    out_file = audio.download(output_path=destination)

    # Rename the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # Print file location
    print(f"Music downloaded to :{new_file}")

link, destination = menu(num_arguments)
download(link, destination)
