from pdf2image import convert_from_path
from PIL import Image
import subprocess
import sys
import os

in_dir = "c:\\users\\robert\\downloads"
output_dir = 'c:\\users\\robert\\downloads'

os.makedirs(output_dir, exist_ok=True)

def combine_images(jpg1, outfile):
    first = Image.open(jpg1)
    width, height = first.size

    datec = (2112, 72, 2412, 120)
    titlec = (776, 196, 1722, 250)
    gridc = (846, 350, 1650, 1150)
    acrossc = (140, 1240, 1150, 2100)
    downc = (1278, 1240, 2288, 2100)
    overflowc = (0, 60, width, height - 1500)
    imagesz = (height, width)
    gridsz = 150
    cluesz = 140
    titlepos = (1600, 0)
    datepos = (1600, 64)
    gridpos = (150, 0)
    acrosspos = (75, 1205)
    downpos = (1754, 1205)
    topcrop2 = 60
    bottomcrop = 235
    datecrop = first.crop(datec)
    titlecrop = first.crop(titlec)
    gridcrop = first.crop(gridc)
    w, h = gridcrop.size
    gridcrop = gridcrop.resize(((int((w * gridsz) / 100)), int((h * gridsz) / 100)))
    acrosscrop = first.crop(acrossc)
    w, h = acrosscrop.size
    acrosscrop = acrosscrop.resize(((int((w * cluesz) / 100)), int((h * cluesz) / 100)))
    downcrop = first.crop(downc)
    w, h = downcrop.size
    downcrop = downcrop.resize(((int((w * cluesz) / 100)), int((h * cluesz) / 100)))
    jpg_merge = Image.new(gridcrop.mode, imagesz, color = (255, 255, 255))
    jpg_merge.paste(titlecrop, titlepos)
    jpg_merge.paste(datecrop, datepos)
    jpg_merge.paste(gridcrop, gridpos)
    jpg_merge.paste(acrosscrop, acrosspos)
    jpg_merge.paste(downcrop, downpos)
    jpg_merge.save(os.path.join(output_dir, outfile))
    os.remove(jpg1)

def process_pdf(pdf_path, outfile):
    jpgs = convert_from_path(pdf_path, dpi=300)
    for i, jpg in enumerate(jpgs):
        image_path = os.path.join(output_dir, f'page_{i+1}.jpg')
        jpg.save(image_path, 'JPEG')
        combine_images(os.path.join(output_dir, 'page_1.jpg'), outfile)

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

