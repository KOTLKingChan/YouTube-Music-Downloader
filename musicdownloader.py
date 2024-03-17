import os
import sys
from pytube import YouTube

# Arguments validation
num_arguments = len(sys.argv)

if(num_arguments<1 or num_arguments>3):
    print("Please input valid arguments.\nSyntax: python musicdownloader.py {url} {file path (optional)}")
    os._exit(0)

def menu_link():
    print('Use txt file? (Y/N)')
    usetxtfile = input()

    links = list()

    if(usetxtfile=='Y'):
        if not os.path.exists("links.txt"):
            # Create the file if it does not exist
            with open("links.txt", "w") as file:
                file.write("")

        with open("links.txt", "r") as file:
            for line in file:
                # Process each line here
                links.append(line.strip())  # Remove newline characters       
    
    elif(usetxtfile=='N'):
        print('Input YouTube Link: ')
        link = input()
        links = list(link)
    else:
        menu_link()
    
    return links
    
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

# Ask for Arguments
def menu(num_arguments):
    if(num_arguments==1):
        print('YouTube Music Downloader')
        links = menu_link()
        destination = menu_filepath()
    else:
        # Get arguments
        links = list(sys.argv[1])
        if(num_arguments==3):
            destination = sys.argv[2]
        else:
            destination = "Downloads/"

    return links, destination

def download(links, destination):
    for link in links:
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

links, destination = menu(num_arguments)
download(links, destination)
