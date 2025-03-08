import os
import glob

def count_characters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return len(content)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def main():
    # Get all .txt files in current directory and subdirectories
    txt_files = glob.glob('**/*.txt', recursive=True)
    
    # Sort files for consistent output
    txt_files.sort()
    
    total_chars = 0
    
    # Process each file
    for file_path in txt_files:
        char_count = count_characters(file_path)
        print(f"{file_path}: {char_count}文字")
        total_chars += char_count
    
    # Print total
    print(f"\n合計: {total_chars}文字")

if __name__ == '__main__':
    main()
