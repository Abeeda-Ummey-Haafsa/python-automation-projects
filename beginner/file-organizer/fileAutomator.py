import os, shutil, logging
from os import scandir, rename
from os.path import exists, splitext
from time import sleep

from shutil import move

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


source_dir = "C:/Users/Dell/Downloads"
dest_dir_music = "C:/Users/Dell/Downloads/Download Music"
dest_dir_sfx = "C:/Users/Dell/Downloads/Download Wav"
dest_dir_video = "C:/Users/Dell/Downloads/Download Video"
dest_dir_image = "C:/Users/Dell/Downloads/Download Image"
dest_dir_documents = "C:/Users/Dell/Downloads/Download Docs"

# supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


def make_unique(dest, name):
    # os.path.splitext() method is used to split the pathname into a pair (root, ext)
    # where root is the part of the path before the file extension
    # and ext is the file extension itself
    # if name = "report.pdf" then after spliting 
    # fileName = report and extension = .pdf
    fileName, extension = splitext(name)
    counter = 1
    
    while exists(f"{dest}/{name}"):
        # name = f"{fileName}({str(counter)}{extension})" # name = "report(1).pdf"
        name = f"{fileName}[{counter}]{extension}"
        counter += 1

    return name

def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = os.path.join(dest, name)
        newName = os.path.join(dest, unique_name)
        # os.path.join() method is a function in the os module that joins one or more path components intelligently
        # constructs a full path by concatenating various components
        # while automatically inserting the appropriate path separator 
        # (/ for Unix-based systems and \ for Windows).
        rename(oldName, newName) #Rename the file or directory src to dst

    shutil.move(entry.path, dest)


class MoverHandler(FileSystemEventHandler):

    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_doc_files(entry, name)

    def check_image_files(self, entry, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved Image File: {name}")

    def check_video_files(self, entry, name):
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved Video File: {name}")

    def check_doc_files(self, entry, name):
        for doc_extension in document_extensions:
            if name.endswith(doc_extension) or name.endswith(doc_extension.upper()):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved Document: {name}")

    def check_audio_files(self, entry, name):
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                if entry.stat().st_size < 10_000_000 or "SFX" in name:
                    dest = dest_dir_sfx
                else:
                    dest = dest_dir_music
                move_file(dest, entry, name)
                logging.info(f"Moved Audio File: {name}")


# This driver code was taken from -> 
# https://pythonhosted.org/watchdog/quickstart.html#quickstart
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()