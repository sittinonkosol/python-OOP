import os
import re
import sys
import math

# Directory where this script resides
script_dir = os.path.dirname(os.path.abspath(__file__))
exts = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')
# find image files recursively (relative paths from script_dir)
files = []
for root, _, filenames in os.walk(script_dir):
    for name in filenames:
        if name.lower().endswith(exts):
            full = os.path.join(root, name)
            rel = os.path.relpath(full, script_dir)
            files.append(rel)
files.sort()

try:
    from PIL import Image
    has_pil = True
except Exception:
    has_pil = False

def print_ratio(width, height, name=None):
    if height == 0:
        print('Height cannot be zero')
        return
    g = math.gcd(width, height)
    rw, rh = width // g, height // g
    prefix = f"{name} -> " if name else ""
    print(f"{prefix}{width}x{height} -> ratio {rw}:{rh}")

def manual_resolution_flow():
    user_input = input('Please enter image resolution: ').strip().lower()
    m = re.match(r'^\s*(\d+)\s*[x\-\*/ ]\s*(\d+)\s*$', user_input)
    if m:
        width, height = map(int, m.groups())
        print_ratio(width, height)
    else:
        print("Please split with x,-,*,/ or ' '")

if not files:
    print('No image files found in folder:', script_dir)
    manual_resolution_flow()
    sys.exit(0)

sizes = {}
print('Image files found (recursive):')
for i, f in enumerate(files, 1):
    path = os.path.join(script_dir, f)
    size_desc = '(unknown)'
    if has_pil:
        try:
            with Image.open(path) as im:
                w, h = im.size
            sizes[f] = (w, h)
            size_desc = f'({w}x{h})'
        except Exception:
            size_desc = '(unreadable)'
    print(f"{i}: {f} {size_desc}")

choice = input('Enter number or filename (relative path or base name): ').strip()
rel = None
if choice.isdigit():
    idx = int(choice) - 1
    if 0 <= idx < len(files):
        rel = files[idx]
        filename = os.path.join(script_dir, rel)
    else:
        print('Invalid selection')
        sys.exit(1)
else:
    # absolute path
    if os.path.isabs(choice):
        filename = choice
        try:
            rel = os.path.relpath(filename, script_dir)
        except Exception:
            rel = None
    else:
        # exact relative match
        if choice in files:
            rel = choice
            filename = os.path.join(script_dir, rel)
        else:
            # try matching by basename
            matches = [f for f in files if os.path.basename(f) == choice]
            if len(matches) == 1:
                rel = matches[0]
                filename = os.path.join(script_dir, rel)
            elif len(matches) > 1:
                print('Multiple files with that name found. Use the number or relative path:')
                for m in matches:
                    print('-', m)
                sys.exit(1)
            else:
                # try treating as relative path under script_dir
                filename = os.path.join(script_dir, choice)
                if not os.path.exists(filename):
                    print('File not found:', filename)
                    sys.exit(1)
                rel = os.path.relpath(filename, script_dir)

if has_pil:
    # prefer cached size by relative path if available
    if rel and rel in sizes:
        width, height = sizes[rel]
        print_ratio(width, height, rel)
    else:
        try:
            with Image.open(filename) as im:
                width, height = im.size
            name_for_print = rel if rel else os.path.basename(filename)
            print_ratio(width, height, name_for_print)
        except Exception as e:
            print('Cannot open image with Pillow:', e)
            print('Falling back to manual resolution input')
            manual_resolution_flow()
else:
    print('Pillow (PIL) is not installed. Install with: pip install pillow')
    manual_resolution_flow()

