# ESTI Project - Setup Checklist

## ✅ Completed

- [x] Created folder structure:
  - `assets/css/` - for stylesheets
  - `assets/js/` - for JavaScript files  
  - `assets/images/` - for all images
  - `pages/` - (optional) for HTML pages

- [x] Updated some file references (CSS link in ESTIhome.html)

## ⚠️ TODO

### Priority 1: Manual Steps (if automated script doesn't work)

1. **Copy Files to New Locations:**
   ```
   Copy ESTI.css → assets/css/ESTI.css
   Copy ESTI.js → assets/js/ESTI.js
   Copy all *.png, *.jpg, *.gif, *.webp files → assets/images/
   ```

2. **Update All HTML Files** with these patterns:

   **CSS Link:** Change from `href="ESTI.css"` to `href="assets/css/ESTI.css"`
   
   **JS Script:** Change from `src="ESTI.js"` to `src="assets/js/ESTI.js"`
   
   **Image Sources:** Change every `src="imagename.ext"` to `src="assets/images/imagename.ext"`

3. **Files to Update:**
   - [  ] ESTIhome.html
   - [  ] ESTIintro.html
   - [  ] ESTIlogIn.html
   - [  ] ESTIlogNext.html
   - [  ] ESTInext.html
   - [  ] ESTIsignNext.html
   - [  ] ESTIsignUp.html

### Priority 2: Alternative - Use Automated Script

Run the Python script to update all references:
```bash
cd c:\Code\ESTI\elective-project\ESTI
python3 update_paths.py
```

Then move the files manually:
```bash
move ESTI.css assets\css\
move ESTI.js assets\js\
move *.png assets\images\
move *.jpg assets\images\
move *.gif assets\images\
move *.webp assets\images\
```

### Priority 3: Verification

After setup, verify:
- [ ] All images load correctly
- [ ] CSS styling is applied
- [ ] JavaScript functionality works (dropdown menu, etc.)
- [ ] No console errors in browser dev tools

## File Mapping

All image files to move to `assets/images/`:
- EstiAutumn.jpg, try3.webp, home.jpg, try5.jpg, EstiPotter.jpg, home2.1.webp
- cat1.png - cat14.png  
- bannerMOOO.gif, vanLogin.gif, vanLoginsEQUEL.gif, logIn.gif, logdupp.gif
- line-removebg-preview.png, line-removebg-preview1.png
- facebookMo.png, googlemo2.png, googleMo.jpg, googleMo1.png
- All other PNG, JPG, GIF, WebP files

## Current Status

- Folder structure: ✅ Created
- Python update script: ✅ Created (update_paths.py)
- HTML/CSS/JS references: ⏳ Partially complete (CSS link updated in ESTIhome.html)
- Guide documentation: ✅ Created (STRUCTURE_GUIDE.md)

## Next Action

Choose one of these approaches:

**Option A (Automated):**
1. Ensure Python 3 is installed
2. Run: `python update_paths.py`
3. Move files to new folders

**Option B (Manual):**
1. Follow STRUCTURE_GUIDE.md
2. Search and replace in each HTML file
3. Move files to new folders

**Option C (Ask me):**
I can manually update each HTML file for you if needed
