from email.policy import default
from django.shortcuts import render, redirect
from .forms import ImagePDF
from .models import imagetopdf
from django.core.files.storage import FileSystemStorage
from pathlib import Path
import os
import uuid
import mimetypes
from django.http import HttpResponse, Http404,FileResponse
import img2pdf
from PIL import Image


image_array=[]


def index(request):
    if request.method == 'POST':
        image_array.clear()
        print(f'the image array is {image_array}')
        fs = FileSystemStorage()
        form = ImagePDF(request.POST, request.FILES)
        images = request.FILES.getlist('images')
        
        if form.is_valid():
            for image in images:
                filename=fs.save(image.name, image)
                
                BASE_DIR = Path(__file__).resolve().parent.parent
                dir = os.path.join(BASE_DIR, 'imagetopdf/files/images', filename)
                image_array.append(dir)
                print(f'the image array is after {image_array}')
            return redirect('convert')
        else:
            form = ImagePDF()
    return render(request, 'index.html',{'form':ImagePDF()})


def convert(request):
    if request.method == 'POST':
        
        uuidFilename=str(uuid.uuid4())
        BASE_DIR = Path(__file__).resolve().parent.parent
        pdf_file=os.path.join(BASE_DIR,'imagetopdf/files/pdfs',uuidFilename+'.pdf')
        pdf_bytes = img2pdf.convert(image_array)
        file = open( pdf_file, "wb")
        file.write(pdf_bytes)
        file.close()
        print("Successfully made pdf file") 

        path=open( pdf_file,'rb')
        mime_type, _ = mimetypes.guess_type( pdf_file)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = 'attachment; filename=%s' % uuidFilename
        return response

    return render(request, 'convert.html')




    



def testcall(request):
    print("testcall")
    return render(request, 'convert.html')