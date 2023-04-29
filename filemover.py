import os
import shutil
picturedir = 'pictures here'
pdfdir = "pdfs here"
images = [f for f in os.listdir() if (".png" in f.lower()or ".jpg" in f.lower())]
pdfs = [f for f in os.listdir() if (".pdf" in f.lower() )]
if not(os.path.exists(picturedir)):
    os.mkdir(picturedir)
if not(os.path.exists(pdfdir)):
    os.mkdir(pdfdir)


for image in images:
    new_path = picturedir + '/' + image
    shutil.move(image, new_path)
for pdf in pdfs:
    new_path = pdfdir + '/' + pdf
    shutil.move(pdf, new_path)
