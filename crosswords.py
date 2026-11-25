from pdf2image import convert_from_path
from PIL import Image
import subprocess
import sys
import os

in_dir = "c:\\users\\robert\\downloads"
output_dir = 'c:\\users\\robert\\downloads'

os.makedirs(output_dir, exist_ok=True)

def combine_images(jpg1, jpg2, outfile):
    first = Image.open(jpg1)
    width, height = first.size
    mainc = (0, 352, width, height - 234)
    datec = (2100, 8, width, 124)
    titlec = (0, 164, width, 272)
    overflowc = (0, 60, width, height - 1500)
    topgrid = 252
    topcrop2 = 60
    bottomcrop = 235
    overflow = Image.open(jpg2)
    datecrop = first.crop(datec)
    titlecrop = first.crop(titlec)
    firstcrop = first.crop(mainc)
    overflowcrop = overflow.crop(overflowc)
    jpg_merge = Image.new(firstcrop.mode, (width, height))
    jpg_merge.paste(titlecrop, (0, 0))
    jpg_merge.paste(datecrop, ((width - 380), 0))
    jpg_merge.paste(firstcrop, (0, 272 - 164))
    jpg_merge.paste(overflowcrop, (0, (height - 272 - 234)))
    jpg_merge.save(os.path.join(output_dir, outfile))
    os.remove(jpg1)
    os.remove(jpg2)

def process_pdf(pdf_path, outfile):
    jpgs = convert_from_path(pdf_path, dpi=300)
    for i, jpg in enumerate(jpgs):
        if len(jpgs) > 1:
            image_path = os.path.join(output_dir, f'page_{i+1}.jpg')
        else:
            image_path = os.path.join(output_dir, outfile)
        jpg.save(image_path, 'JPEG')
    if len(jpgs) > 1:
        combine_images(os.path.join(output_dir, 'page_1.jpg'), os.path.join(output_dir, 'page_2.jpg'), outfile)

for entry in os.scandir(in_dir):  
    if entry.is_file():  # check if it's a file
        if entry.name.find('cryptic-crossword') >= 0 or entry.name.find('toughie-crossword') >= 0:
            pre, ext = os.path.splitext(entry.name)
            if ext == ".pdf":
                outfile = pre + '.jpg'
                process_pdf(entry.path, outfile)
                cp = subprocess.run(["powershell", os.path.join(os.path.dirname(__file__), "print.ps1"), os.path.join(output_dir, outfile)])
                os.remove(os.path.join(output_dir, outfile))
                os.remove(entry.path)

