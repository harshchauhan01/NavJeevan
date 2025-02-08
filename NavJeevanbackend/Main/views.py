from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatentForm
from django.contrib import messages
from django.template.loader import render_to_string
from .models import *
from django.conf import settings


def home(request):
    return render(request, 'home.html')

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

def PatientFile(request, patient_id):
    patient = get_object_or_404(Patent, patent_id=patient_id)
    doctor = patient.patent_doctor  

    return render(request, 'PatientFile.html', {
        'patient': patient,
        'doctor': doctor 
    })



from xhtml2pdf import pisa

def download_patient_pdf(request, patient_id):
    patient = Patent.objects.get(patent_id=patient_id)
    doctor = patient.patent_doctor  
    media_url = request.build_absolute_uri(settings.MEDIA_URL)

    html = render_to_string('patient_pdf_template.html', {'patient': patient,'doctor': doctor,'media_url': media_url })

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="patient_report.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Error generating PDF", status=500)
    
    return response
