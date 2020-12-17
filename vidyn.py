import os
import shutil
import subprocess

# mpc binary path
mpc_path = ""
# where to run script
working_directory = ""

# checks if file ends with a video file extension
def is_video_file(filename: str):
    file_ext = (".mp4", ".mkv", ".avi", ".wmv", ".flv", ".webm", ".mov", ".m4v")
    return filename.lower().endswith(file_ext)


# moves file to a separate folder
def mov_file(file):
    rel_path = "./!keep"
    os.makedirs(rel_path, exist_ok=True)
    shutil.move(file.path, rel_path)
    print(f"Keeping: {file.path}")


# moves file to a separate folder
def rem_file(file):
    rel_path = "./!rem"
    os.makedirs(rel_path, exist_ok=True)
    shutil.move(file.path, rel_path)
    print(f"Removing: {file.path}")


os.chdir(working_directory)

for b in os.scandir(os.getcwd()):
    if b.is_dir():
        continue
    elif is_video_file(b.name) is False:
        continue

    print(f"Opening: ", b.path)

    subprocess.call([mpc_path,
                     b.path])

    while True:
        usr_input = input("Keep?\n")
        if usr_input == "y":
            mov_file(b)
            break
        elif usr_input == "n":
            rem_file(b)
            break
        else:
            continue

print("\nDONE")
