import os
import sys
from pytube import YouTube

# Arguments validation
num_arguments = len(sys.argv)

if(num_arguments<2 or num_arguments>3):
    print("Please input valid arguments.\nSyntax: python musicdownloader.py {url} {file path (optional)}")
    os._exit(0)

# Get arguments
link = sys.argv[1]
if(num_arguments==3):
    destination = sys.argv[2]
else:
    destination = "Downloads/"

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