# Problem 1: Accessing files on Windows using Python

**Decision:** Use os.scandir() for accessing files and directories.

**Implementation Details:**
The script needs to efficiently scan a directory and retrieve file information such as file name, path, and type. Python provides multiple options for this task, including os.listdir() and glob.

os.scandir() was selected because:

It provides directory entries along with file metadata

It is more efficient for iterating through large directories

It works reliably on Windows file systems

This makes os.scandir() suitable for repeatedly scanning the source directory during monitoring.

# Problem 2: Monitoring a directory for changes

**Decision:** Use Python’s watchdog module for directory monitoring.

**Implementation Details:**
Manually polling the directory in a continuous loop would be inefficient and resource-intensive. To avoid this, the project uses the watchdog library, which provides event-driven file system monitoring.

With watchdog:

The script listens for file system events such as file creation or modification

Changes are detected immediately without constant scanning

CPU usage remains low during idle periods

The Observer class is used to watch the target directory, and a custom event handler processes file changes as they occur.

# Problem 3: Handling files while directory monitoring is active

**Decision:** Automatically classify and move files based on their extensions, while safely handling duplicate file names.

**Implementation Details:**
When directory monitoring is active, the script reacts to file system changes using the watchdog observer. On each modification event, the source directory is scanned using os.scandir().

For every detected file:

The file extension is checked against predefined categories (documents, images, videos, and audio)

Based on the extension, the file is moved to its corresponding destination folder

To prevent overwriting files:

The script checks if a file with the same name already exists in the destination folder

If a conflict is found, the existing file is renamed using a counter-based format (e.g., file[1].pdf)

This logic is handled by the make_unique() function before moving the file

This ensures safe file movement while keeping duplicate files clearly distinguishable.