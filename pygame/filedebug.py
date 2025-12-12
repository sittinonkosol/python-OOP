import os
from pathlib import Path
import sys

# --- Constants for formatting ---
# These characters create the visual lines of the tree
SPACE = '    '
BRANCH = '│   '
TEE = '├── '
LAST = '└── '

def tree(dir_path: Path, max_depth: int = -1, prefix: str = ''):
    """
    A recursive function to print the directory tree structure.

    :param dir_path: The starting directory path object (pathlib.Path).
    :param max_depth: The maximum depth to traverse. -1 means no limit.
    :param prefix: The string prefix used for indentation and lines.
    """
    
    # Do not traverse if max_depth is reached
    if max_depth == 0:
        return
        
    # Get all entries (files and directories) and sort them alphabetically
    # Directories are listed before files for a cleaner look.
    contents = sorted(list(dir_path.iterdir()))
    
    dirs = [p for p in contents if p.is_dir()]
    files = [p for p in contents if p.is_file()]

    # Combine directories and files in a specific order
    items = dirs + files
    
    # Process each item
    for index, path in enumerate(items):
        is_last = index == len(items) - 1
        
        # Determine the pointer (TEE for middle items, LAST for the final item)
        pointer = LAST if is_last else TEE
        
        # Print the entry name with its pointer and appropriate color
        if path.is_dir():
            # Directories in Cyan color
            print(f'{prefix}{pointer}\033[96m{path.name}/\033[0m')
            
            # Recurse into the directory
            new_prefix = prefix + (SPACE if is_last else BRANCH)
            new_depth = max_depth - 1 if max_depth > 0 else -1
            yield from tree(path, new_depth, new_prefix)
        else:
            # Files in default color (with a check for common Python files)
            color = '\033[92m' if path.name.endswith('.py') else '' # Green for Python files
            print(f'{prefix}{pointer}{color}{path.name}\033[0m')

def print_tree(start_path='.', max_depth=-1):
    """
    Sets up and initiates the directory tree printout.
    """
    path = Path(start_path)
    if not path.exists():
        print(f"Error: Path not found: {start_path}", file=sys.stderr)
        return
        
    print(f"\033[1mProject Tree for: {path.resolve()}\033[0m\n")
    print(f"\033[96m{path.name}/\033[0m") # Print the root directory itself
    
    # Use the generator function
    for _ in tree(path, max_depth):
        pass

# --- Example Usage ---
if __name__ == '__main__':
    # 1. Check for command-line arguments (e.g., python show_tree.py /path/to/project)
    #    If no argument is given, it defaults to the Current Working Directory ('.').
    try:
        start_dir = sys.argv[1]
    except IndexError:
        start_dir = '.'
    
    # You can set a default maximum depth here if you want to avoid huge outputs
    # For example, to only show the first 3 levels: print_tree(start_dir, max_depth=3)
    print_tree(start_dir)