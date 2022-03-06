import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

def ImagetopdfDeleteImagesTrigger():
    print("ImagetopdfDeleteImagesTrigger triggered")
    dir = os.path.join(BASE_DIR,'imagetopdf/files/images')
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    print("ImagetopdfDeleteImagesTrigger completed")
 

def ImagetopdfDeletePDFTrigger():
    print("ImagetopdfDeletePDFTrigger triggered")
    dir = os.path.join(BASE_DIR,'imagetopdf/files/pdfs')
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    print("ImagetopdfDeletePDFTrigger completed")