import os
import argparse

print("Yorlin Creator whl")

def list_files(directory):
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    print(entry.name)
    except FileNotFoundError:
        print(f"Directory {directory} does not exist.")

def main():
    parser = argparse.ArgumentParser(description="List files in a directory")
    parser.add_argument('--directory', type=str, required=True, help='Directory to list files from')
    parser.add_argument('--file', type=str, help='File to perform operation on (not implemented)')
    
    args = parser.parse_args()
    
    if args.directory:
        list_files(args.directory)
    
    if args.file:
        print(f"File flag is set with value: {args.file}")

if __name__ == "__main__":
    main()