from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def Login(request):
    return render(request,'sidenav.html')

def upload_details(request):
    return render(request, 'upload_details.html')

def patient_records(request):
    return render(request, 'patient_records.html')