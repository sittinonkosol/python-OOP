import os
import sys
from pathlib import Path

try:
    from PIL import Image
    has_pil = True
except ImportError:
    has_pil = False
    print('Pillow (PIL) is not installed. Install with: pip install pillow')
    sys.exit(1)

# Directory where this script resides
script_dir = os.path.dirname(os.path.abspath(__file__))

# Image file extensions to convert
source_exts = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.tiff', '.ico', '.heic', '.heif', '.avif')

def convert_image_to_png(input_path, output_path):
    """Convert an image file to PNG format."""
    try:
        with Image.open(input_path) as im:
            # Convert RGBA to RGB if saving as PNG (some formats might need this)
            if im.mode in ('RGBA', 'LA', 'P'):
                # Keep transparency for formats that support it
                if im.mode == 'P':
                    # Convert palette mode, keeping transparency if available
                    if 'transparency' in im.info:
                        im.putalpha(im.getchannel('A'))
                im_rgb = im.convert('RGBA')
            else:
                im_rgb = im.convert('RGB')
            
            # Save as PNG
            if im_rgb.mode == 'RGBA':
                im_rgb.save(output_path, 'PNG')
            else:
                im_rgb.convert('RGB').save(output_path, 'PNG')
        return True
    except Exception as e:
        print(f"Error converting {input_path}: {e}")
        return False

def main():
    # Find all image files recursively
    image_files = []
    for root, _, filenames in os.walk(script_dir):
        for filename in filenames:
            if filename.lower().endswith(source_exts):
                full_path = os.path.join(root, filename)
                image_files.append(full_path)
    
    if not image_files:
        print("No image files found in the directory tree.")
        return
    
    image_files.sort()
    print(f"Found {len(image_files)} image file(s):")
    for i, full_path in enumerate(image_files, 1):
        rel_path = os.path.relpath(full_path, script_dir)
        print(f"{i}: {rel_path}")
    
    # Ask user which files to convert
    print("\nEnter file numbers to convert (comma-separated), 'all' for all, or 'q' to quit:")
    choice = input("> ").strip().lower()
    
    if choice == 'q':
        return
    
    if choice == 'all':
        to_convert = image_files
    else:
        to_convert = []
        try:
            indices = [int(x.strip()) - 1 for x in choice.split(',')]
            for idx in indices:
                if 0 <= idx < len(image_files):
                    to_convert.append(image_files[idx])
                else:
                    print(f"Invalid index: {idx + 1}")
            if not to_convert:
                print("No valid files selected.")
                return
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            return
    
    print(f"\nConverting {len(to_convert)} file(s)...")
    converted_count = 0
    skipped_count = 0
    
    for full_path in to_convert:
        rel_path = os.path.relpath(full_path, script_dir)
        
        # Skip if already PNG
        if full_path.lower().endswith('.png'):
            print(f"⊘ {rel_path} (already PNG, skipping)")
            skipped_count += 1
            continue
        
        # Create output path: replace extension with .png
        base_path = os.path.splitext(full_path)[0]
        output_path = base_path + '.png'
        
        # Check if output already exists
        if os.path.exists(output_path):
            print(f"⊘ {rel_path} → {os.path.basename(output_path)} (output exists, skipping)")
            skipped_count += 1
            continue
        
        # Convert
        if convert_image_to_png(full_path, output_path):
            rel_output = os.path.relpath(output_path, script_dir)
            print(f"✓ {rel_path} → {os.path.basename(output_path)}")
            converted_count += 1
        else:
            skipped_count += 1
    
    print(f"\nConversion complete: {converted_count} converted, {skipped_count} skipped")

if __name__ == '__main__':
    main()
