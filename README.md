Here's a markdown README for the file organizer application:

# File Organizer

A Python utility that automatically organizes files in the current directory into categorized folders based on their file extensions.

## Description

This application scans the directory where it's run and automatically sorts files into appropriate folders based on their file types. It helps keep your directories clean and organized by categorizing files into the following folders:

- **docs** - Documents (`.pdf`, `.docx`, `.txt`, `.pptx`, `.xlsx`, `.csv`, `.ppt`, `.doc`, `.xls`)
- **images** - Image files (`.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.bmp`, `.svg`, `.ico`, `.tiff`, `.tif`)
- **videos** - Video files (`.mp4`, `.avi`, `.mkv`, `.m4a`, `.flv`, `.mov`, `.wmv`)
- **archives** - Compressed files (`.zip`, `.rar`, `.7z`)
- **music** - Audio files (`.mp3`, `.wav`, `.flac`)
- **executables** - Executable files (`.exe`, `.msi`, `.apk`)
- **code** - Source code files (`.py`, `.js`, `.html`, `.htm`, `.css`, `.java`, `.cpp`, `.c`, `.h`, `.cs`, `.php`, `.ipynb`)
- **others** - Other known formats (`.dat`, `.db`, `.log`, `.sql`, `.xml`, `.json`, `.md`, `.cfg`, `.ini`, `.bak`, `.iso`, `.torrent`)
- **miscellaneous** - Any files that don't match the above categories

## Usage

1. Download the executable
2. Run the application in the directory you want to organize
3. The program will automatically:
   - Create necessary folders
   - Sort files into appropriate categories
   - Display the number of files moved to each category
   - Create a log file (`file_organizer.log`) with detailed operation information

## Notes

- The application will not move itself or its log file
- Files are moved based on their extensions
- A detailed log of all operations is maintained in `file_organizer.log`

## Requirements

- Windows operating system (for `.exe` version)
- No additional requirements for the executable version
- Python 3.6+ (if running from source)

## Building from Source

To build the executable (run this in the root):

```sh
pyinstaller --noconfirm --onefile --windowed --icon "subfolder.ico"  "organize.py"
```

This will create a standalone executable using PyInstaller.