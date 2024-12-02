import os
import sys
import shutil
import logging
from typing import List, Dict


if getattr(sys, 'frozen', False):
    APPLICATION_PATH = os.path.dirname(sys.executable)
else:
    APPLICATION_PATH = os.path.dirname(os.path.abspath(__file__))

def setup_logging():
    log_path = os.path.join(APPLICATION_PATH, 'file_organizer.log')
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler()
        ]
    )

def get_file_categories() -> Dict[str, tuple]:
    return {
        'docs': ('.pdf', '.docx', '.txt', '.pptx', '.xlsx', '.csv', '.ppt', '.doc', '.xls'),
        'images': ('.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp', '.svg', '.ico', '.tiff', '.tif'),
        'videos': ('.mp4', '.avi', '.mkv', '.m4a', '.flv', '.mov', '.wmv'),
        'archives': ('.zip', '.rar', '.7z'),
        'music': ('.mp3', '.wav', '.flac'),
        'executables': ('.exe', '.msi', '.apk'),
        'code': ('.py', '.js', '.html', '.htm', '.css', '.java', '.cpp', '.c', '.h', '.cs', '.php', '.ipynb'),
        'others': ('.dat', '.db', '.log', '.sql', '.xml', '.json', '.md', '.cfg', '.ini', '.bak', '.iso', '.torrent'),
        'miscellaneous' : ()
    }

def create_directories(categories: Dict[str, tuple]) -> None:
    for category in categories:
        try:
            os.makedirs(category, exist_ok=True)
            logging.info(f"Created or verified directory: {category}")
        except Exception as e:
            logging.error(f"Error creating directory {category}: {str(e)}")

def get_files_to_move(categories: Dict[str, tuple]) -> Dict[str, List[str]]:
    files_dict = {category: [] for category in categories}
    
    try:
        for file_name in os.listdir(APPLICATION_PATH):
            if file_name.startswith('organize') or file_name == 'file_organizer.log':
                continue
            
            full_path = os.path.join(APPLICATION_PATH, file_name)
            if os.path.isdir(full_path):
                continue
            
            file_ext = os.path.splitext(file_name)[1].lower()
            file_categorized = False
            
            for category, extensions in categories.items():
                if category != 'miscellaneous' and file_ext in extensions:
                    files_dict[category].append(file_name)
                    file_categorized = True
                    break
            
            if not file_categorized:
                files_dict['miscellaneous'].append(file_name)
    
    except Exception as e:
        logging.error(f"Error getting files to move: {str(e)}")
    
    return files_dict

def move_files(files_dict: Dict[str, List[str]]) -> None:
    for category, files in files_dict.items():
        for file_name in files:
            try:
                target_path = os.path.join(category, file_name)
                shutil.move(file_name, target_path)
                logging.info(f"Moved {file_name} to {target_path}")
            except Exception as e:
                logging.error(f"Error moving {file_name}: {str(e)}")
                
    # remove thee empty directories
    for item in os.listdir(APPLICATION_PATH):
        item_path = os.path.join(APPLICATION_PATH, item)
        if os.path.isdir(item_path) and not os.listdir(item_path):
            try:
                os.rmdir(item_path)
                logging.info(f"Removed empty directory: {item}")
            except Exception as e:
                logging.error(f"Error removing directory {item}: {str(e)}")

def main():
    setup_logging()
    logging.info("Starting file organization...")
    
    categories = get_file_categories()
    create_directories(categories)
    files_dict = get_files_to_move(categories)
    
    for category, files in files_dict.items():
        print(f"{category.capitalize()}: {len(files)} files")
    
    move_files(files_dict)
    logging.info("File organization completed!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        sys.exit(1)