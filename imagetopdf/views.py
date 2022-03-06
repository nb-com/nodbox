from pathlib import Path
from email.policy import default
from django.shortcuts import render, redirect
from .forms import ImagePDF
from .models import imagetopdf
from django.core.files.storage import FileSystemStorage
import os
import uuid
import mimetypes
from django.http import HttpResponse, Http404,FileResponse
import img2pdf
from PIL import Image




image_array=[]
pdf_array=[]


def imgtopdfUpload(request):
    if request.method == 'POST':
        image_array.clear()
        print(f'the image array is {image_array}')
        fs = FileSystemStorage()
        form = ImagePDF(request.POST, request.FILES)
        images = request.FILES.getlist('images')
        
        if form.is_valid():
            for image in images:
                filename=fs.save(image.name,image)
                
                BASE_DIR = Path(__file__).resolve().parent.parent
                dir = os.path.join(BASE_DIR, 'imagetopdf/files/images', filename)
                image_array.append(dir)
                print(f'the image array is after {image_array}')
            return redirect('imgtopdfconvert')
        else:
            form = ImagePDF()
    return render(request, 'imgtopdf-upload.html',{'form':ImagePDF()})


def imgtopdfConvert(request):
    if request.method == 'POST':
        
        uuidFilename=str(uuid.uuid4())
        uuidFilenamepdf=uuidFilename+".pdf"
        BASE_DIR = Path(__file__).resolve().parent.parent
        pdf_file=os.path.join(BASE_DIR,'imagetopdf/files/pdfs',uuidFilenamepdf)
        pdf_bytes = img2pdf.convert(image_array)
        file = open(pdf_file, "wb")
        file.write(pdf_bytes)
        file.close()
        print("Successfully made pdf file") 
        pdf_array.append(pdf_file)

        path=open(pdf_file,'rb')
        mime_type, _ = mimetypes.guess_type(pdf_file)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = 'attachment; filename=%s' % uuidFilenamepdf
        #asyncPDFDeleteFile(pdf_file)
        #asyncImageDeleteFile(image_array)

        return response 
    return render(request, 'imgtopdf-convert.html')




def asyncPDFDeleteFile(filePath):
    for pdf in filePath:
        if os.path.exists(filePath):                           
            os.remove(filePath)
        else:
            print("Can not delete the file as it doesn't exists")



def asyncImageDeleteFile(filePath):
    for image in filePath:
        if os.path.exists(image):
            os.remove(image)
        else:
            print("Can not delete the file as it doesn't exists")


def onquit(request):
    print("testcall triggered and window closed")
    return render(request, 'home.html')
  

def home(request):
    image_array.clear()
    return render(request, 'home.html')



def getStarted(request):
    return render(request, 'convert-home.html')

