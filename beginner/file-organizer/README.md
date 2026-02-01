# File Management Automation

This project contains a Python script that automatically organizes files in your `Downloads` folder by moving them into categorized subdirectories based on their file type.

## How It Works

The script monitors the `Downloads` folder for new files. When a file is added or modified, it checks its extension and moves it to one of the following folders:

- `Download Music`
- `Download Video`
- `Download Image`
- `Download Docs`

If a file with the same name already exists in the destination, the script will rename the new file to make it unique (e.g., `report[1].pdf`).

## Supported File Types

- **Video:** `.webm`, `.mpg`, `.mp4`, `.avi`, `.wmv`, `.mov`, etc.
- **Audio:** `.m4a`, `.flac`, `.mp3`, `.wav`, `.wma`, `.aac`
- **Documents:** `.doc`, `.docx`, `.pdf`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
- **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.tiff`, `.bmp`, `.svg`

## Requirements

- Python 3
- `watchdog` library

## Installation

1.  **Install Python:** If you don't have it, download and install Python from [python.org](https://www.python.org/).
2.  **Install watchdog:** Open a terminal or command prompt and run:
    ```bash
    pip install watchdog
    ```

## How to Run

1.  Open a terminal or command prompt.
2.  Navigate to the project directory:
    ```bash
    cd "e:\Projects\Python Automation Projects\File Management Automation"
    ```
3.  Run the script:
    ```bash
    python fileAutomator.py
    ```

### Running in the Background (Windows)

To run the script silently without a console window, use `pythonw`:

```bash
pythonw fileAutomator.py
```

To stop the background process, you will need to end the `pythonw.exe` task in the **Task Manager**.

## Disclaimer

The file moving operations are **permanent**. Once a file is moved, the script does not track its original location. It is recommended to test the script with a temporary folder before running it on your main `Downloads` directory.
