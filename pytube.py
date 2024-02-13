from pytube import YouTube
import os
import colorama
import pyfiglet

colorama.init(autoreset=True)

B = colorama.Fore.RED

result = pyfiglet.figlet_format("PyTube")

# Add color to the result
colored_result = f"{B}{result}{colorama.Style.RESET_ALL}"

print(colored_result)

X = colorama.Fore.YELLOW
Z = colorama.Fore.RED
F = colorama.Fore.GREEN
A = colorama.Fore.BLUE
C = colorama.Fore.MAGENTA
B = colorama.Fore.CYAN
Y = colorama.Fore.LIGHTBLUE_EX

link = input("Link of the video: ")

# Set download location to user's "Downloads" folder
filename = os.path.join(os.path.expanduser("~"), "Downloads")

yt = YouTube(link)

download_type = input("[1] Video\n[2] Audio\n")

if download_type == "Video" or int(1):
    yt.streams.get_highest_resolution().download(filename)

elif download_type == "Audio" or int(2):
    yt.streams.get_audio_only().download(filename)

else:
    print("Invalid option!")

        