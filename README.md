# Telegraph Crosssword reformat

## Background
- I subscribe to Daily Telegraph Puzzles site to get my daily crosswords (cryptic and toughie)
- I prefer to print out hard copies of the puzzles rather than play on-line
- This allows sharing of solving and gives pencil working area to help n solving
- Occasionally the print out used to spill a couple of clues over a second page which was annoying
- A change they made to the formatting (Nov 2026) added a footer with branding
- This significantly reduced space for clues and made the spill over happen all the time
- I fedback this isse to Daily Telegraph but have yet to receive any response
- I decided to work around this 

## Workaround
- When going through the print process on the puzzles site one can see whether spill over is happening and choose to download a pdf rather than print 
- The pdf will contain two pages as illustrated in page_1.jpg and page_2.jpg
- I have masked out the clues to avoid any copyright issues. 
- A python script (crosswords.py) performs the following actions
    - Iterates over each matching pdf
	- Splits the pdf into jpgs using pdf2image library
	- Using PIL imaging library crops from page1 containing Title, Date, Grid + clues section. From page2 it crops the overflow clues
	- Using PIL creates a new image merging all the crops avoiding a lot of redundat white space and the footter
	- This produces jpg like cryptic-crossword-xxxxx.jpg
	- Calls a powershell script (Print.ps1) to send jg to printer.
	- The powershell script brings up an intermediate window (allowing choice of print options.
	- The defaults are fine so script automatically presses OK to allow the print to continue.
	- The python script cleans up the downloads and working files

## Notes
- The python and powershell scripts must be in same folder
- I put a shortcut to the python script in my downloads folder to make it more convenient.
- Powershell must be enabled to run ps1 script files. Set-ExectionPolicy in Powershell console
- The crop areas are defined in the combine_images function in the py file. If the format changes, these will need to be adjusted

