from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa
from .models import *
from .forms import PatentForm

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def patientrecord(request):
    if request.method == 'POST':
        form = PatentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient record added successfully!")
            return redirect('patientrecord')
        else:
            messages.error(request, "Form submission failed. Please check the input fields.")
    else:
        form = PatentForm()
    return render(request, 'patientrecord.html', {'form': form})

@login_required
def PatientFile(request, patient_id):
    patient = get_object_or_404(Patent, patent_id=patient_id)
    doctor = patient.patent_doctor
    return render(request, 'PatientFile.html', {'patient': patient, 'doctor': doctor})

@login_required
def download_patient_pdf(request, patient_id):
    patient = get_object_or_404(Patent, patent_id=patient_id)
    doctor = patient.patent_doctor
    media_url = request.build_absolute_uri(settings.MEDIA_URL)

    html = render_to_string('patient_pdf_template.html', {'patient': patient, 'doctor': doctor, 'media_url': media_url})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="patient_report.pdf"'

    if pisa.CreatePDF(html, dest=response).err:
        return HttpResponse("Error generating PDF", status=500)
    
    return response

@login_required
def CheckRecord(request):
    query = request.GET.get('search', '').strip()
    patients = Patent.objects.filter(patient_id__icontains=query) if query else Patent.objects.all()[:5]
    return render(request, 'CheckPatientRecord.html', {'patients': patients, 'query': query})

def Login(request):
    if request.user.is_authenticated:  
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'hospitalAuth.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')


def checkResource(request):
    return render(request, 'checkResource.html')

def BloodTable(request):
    return render(request, 'bloodGroupTable.html')

def organTable(request):
    organs = Organ.objects.all()
    return render(request, 'OrganTable.html', {'organs': organs})

def Medicine(request):
    return render(request, 'Medicine.html')