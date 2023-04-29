from django.shortcuts import render, redirect # new
from .models import Image
from .form import ImageUploadForm # new 

def uploadView(request):                                      
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
            form = ImageUploadForm()
    return render(request, 'upload_news.html', {'form': form})


def upload_news_admin(request):
     return render(request,'index.html')