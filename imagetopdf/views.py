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






def imgtopdfUpload(request):
    if request.method == 'POST':
        
        fs = FileSystemStorage()
        form = ImagePDF(request.POST, request.FILES)
        images = request.FILES.getlist('images')
        
        if form.is_valid():
            for image in images:
                filename=fs.save(image.name,image)
                BASE_DIR = Path(__file__).resolve().parent.parent
                dir = os.path.join(BASE_DIR, 'imagetopdf/files/images', filename)
                request.session["user"].append(dir)
                request.session.save()
                for key, value in request.session.items():
                    print('{} => {}'.format(key, value))

            return redirect('imgtopdfconvert')

        else:
            print("failed at for loop of adding images to array")
            form = ImagePDF()
    return render(request, 'imgtopdf-upload.html',{'form':ImagePDF()})


def imgtopdfConvert(request):
    if request.method == 'POST':
        uuidFilename=str(uuid.uuid4())
        uuidFilenamepdf=uuidFilename+".pdf"
        BASE_DIR = Path(__file__).resolve().parent.parent
        pdf_file=os.path.join(BASE_DIR,'imagetopdf/files/pdfs',uuidFilenamepdf)
        pdf_bytes = img2pdf.convert(request.session["user"])
        file = open(pdf_file, "wb")
        file.write(pdf_bytes)
        file.close()
        print("Successfully made pdf file") 
        request.session["pdffilepath"].append(pdf_file)
        request.session["uuidfilenamepath"].append(uuidFilenamepdf)
        request.session.save()
        #path=open(pdf_file,'rb')
        #mime_type, _ = mimetypes.guess_type(pdf_file)
        #response = HttpResponse(path, content_type=mime_type)
        #response['Content-Disposition'] = 'attachment; filename=%s' % uuidFilenamepdf
        #asyncPDFDeleteFile(pdf_file)
        #asyncImageDeleteFile(image_array)
        #return response 
        return redirect('download')
    return render(request, 'imgtopdf-convert.html')

def download(request):
        pathof=request.session["pdffilepath"][0]
        filenameof=request.session["uuidfilenamepath"][0]
        path=open(pathof,'rb')
        mime_type, _ = mimetypes.guess_type(pathof)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = 'attachment; filename=%s' % filenameof
        return response
        #asyncPDFDeleteFile(pdf_file)
        #asyncImageDeleteFile(image_array)

def home(request):
    request.session["user"] = []
    request.session["pdffilepath"] = []
    request.session["uuidfilenamepath"] = []
    return render(request, 'home.html')

def getStarted(request):
    return render(request, 'convert-home.html')



def onquit(request):
    print("testcall triggered and window closed")
    return render(request, 'home.html')


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



  





