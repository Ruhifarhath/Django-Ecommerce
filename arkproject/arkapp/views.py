from django.shortcuts import render

# Create your views here.

#note that the pth to this file is in a seperate tmeplates directory in the projects folder, and not in the app folder
# but the path name still works arkapp/index.html or templates/arkaapp/index.html or ./arkapp/index.html

def first_view(request):
    return render(request,'arkapp/index.html')
