import boto3
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import VisitorForm
from .models import Visitor
from django.core.files.storage import default_storage


def index(request):
    return render(request, "index.html")


def register_visitor(request):
    if request.method == "POST":
        form = VisitorForm(request.POST, request.FILES)
        if form.is_valid():
            visitor = form.save(commit=False)

            # Handle the img upload to S3
            # print(visitor.img)
            # if visitor.img:
            #     # Use the default storage backend (S3)
            #     file_name = default_storage.save(visitor.img.name, visitor.img)
            #     file_url = default_storage.url(file_name)
            #     # Store S3 URL and file name in the model
            #     visitor.img = file_url  # Save the URL of the img in the model
            visitor.save()

            return redirect("visitor_list")  # Redirect after successful registration
    else:
        form = VisitorForm()

    return render(request, "register.html", {"form": form})


def visitor_logs(request):
    visitors = Visitor.objects.all()
    return render(request, "logs.html", {"visitors": visitors})
