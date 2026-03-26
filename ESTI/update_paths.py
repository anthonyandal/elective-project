#!/usr/bin/env python3
"""
Script to update file paths in HTML, CSS, and JS files
This script updates image, CSS, and JS references to point to the new assets folder structure
"""

import os
import re
from pathlib import Path

# Define the root directory
ROOT_DIR = Path(__file__).parent

# Image files that need path updates
IMAGE_FILES = [
    'EstiAutumn.jpg', 'try3.webp', 'home.jpg', 'try5.jpg', 'EstiPotter.jpg',
    'cat1.png', 'cat2.png', 'cat3.png', 'cat4.png', 'cat5.png',
    'cat6.png', 'cat7.png', 'cat8.png', 'cat9.png', 'cat10.png',
    'cat11.png', 'cat12.png', 'cat13.png', 'cat14.png',
    'bannerMOOO.gif', 'home2.1.webp',
    'vanLogin.gif', 'vanLoginsEQUEL.gif',
    'line-removebg-preview.png', 'line-removebg-preview1.png',
    'facebookMo.png', 'googlemo2.png',
    'logIn.gif', 'logdupp.gif'
]

def update_html_files():
    """Update all HTML files to use new asset paths"""
    html_files = list(ROOT_DIR.glob('*.html'))
    
    for html_file in html_files:
        print(f"Updating {html_file.name}...")
        content = html_file.read_text(encoding='utf-8')
        original_content = content
        
        # Update CSS link
        content = re.sub(r'href="ESTI\.css"', r'href="assets/css/ESTI.css"', content)
        
        # Update JS script
        content = re.sub(r'src="ESTI\.js"', r'src="assets/js/ESTI.js"', content)
        
        # Update image sources
        for img_file in IMAGE_FILES:
            pattern = f'src="{img_file}"'
            replacement = f'src="assets/images/{img_file}"'
            content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            html_file.write_text(content, encoding='utf-8')
            print(f"  ✓ Updated {html_file.name}")
        else:
            print(f"  - No changes needed for {html_file.name}")

def update_css_file():
    """Update CSS file to use new asset paths"""
    css_file = ROOT_DIR / 'ESTI.css'
    
    if css_file.exists():
        print(f"Updating {css_file.name}...")
        content = css_file.read_text(encoding='utf-8')
        original_content = content
        
        # Update image references in CSS
        for img_file in IMAGE_FILES:
            pattern = f'url\\(["\']?{img_file}["\']?\\)'
            replacement = f'url("assets/images/{img_file}")'
            content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            css_file.write_text(content, encoding='utf-8')
            print(f"  ✓ Updated {css_file.name}")
        else:
            print(f"  - No changes needed for {css_file.name}")

def main():
    print("=" * 60)
    print("Updating project structure for ESTI project")
    print("=" * 60)
    
    update_html_files()
    print()
    update_css_file()
    
    print()
    print("=" * 60)
    print("✓ Path updates complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Ensure/assets/images/ folder exists with all image files")
    print("2. Ensure assets/css/ folder exists with ESTI.css")
    print("3. Ensure assets/js/ folder exists with ESTI.js")
    print("4. Move image files to assets/images/")
    print("5. Move ESTI.css to assets/css/")
    print("6. Move ESTI.js to assets/js/")

if __name__ == '__main__':
    main()
