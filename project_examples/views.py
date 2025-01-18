from django.shortcuts import render
from django.http import HttpResponse

import os

def display(request, file_name):
    if file_name == "exit-image":
        return HttpResponse(f"File '{file_name}.html' not found.")

    folder_path = os.path.join(os.path.dirname(__file__), "templates/project_examples")
    
    if os.path.exists(os.path.join(folder_path, f"{file_name}.html")):        
        return render(request, f"project_examples/{file_name}.html")
    else:
        return HttpResponse(f"File '{file_name}.html' not found.")
