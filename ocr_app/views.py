# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageUploadForm
from .models import UploadedImage
from .utils import preprocess_image, extract_text, extract_dates

def upload_aadhar(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image_path = image.image.path

            processed_img = preprocess_image(image_path)
            extracted_text = extract_text(processed_img)
            dates = extract_dates(extracted_text)

            return JsonResponse({"dates": dates})
    else:
        form = ImageUploadForm()
    
    return render(request, "upload.html", {"form": form})
