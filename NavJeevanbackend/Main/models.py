from django.db import models


class Doctor(models.Model):
    doctor_id = models.CharField(max_length=100, unique=True)
    doctor_name = models.CharField(max_length=200)
    doctor_photo = models.ImageField(upload_to='doctor_photos/', null=True, blank=True)
    doctor_sign_photo = models.ImageField(upload_to='doctor_photos/', null=True, blank=True)
    doctor_status = models.CharField(max_length=20)
    doctor_age = models.CharField(max_length=20)
    doctor_gender = models.CharField(max_length=20)
    doctor_number = models.CharField(max_length=100)
    doctor_designation = models.CharField(max_length=100)

    def __str__(self):
        return self.doctor_name

class Patent(models.Model):
    patent_number = models.CharField(max_length=100)
    patent_title = models.CharField(max_length=200)
    patent_id = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    inventor_name = models.CharField(max_length=100)
    filing_date = models.DateField()
    patent_status = models.CharField(max_length=20)
    patent_age = models.CharField(max_length=20)
    patent_gender = models.CharField(max_length=20)
    patent_doctor = models.CharField(max_length=20)

    # Bed allotment fields
    bed_allotted = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')], default='no')
    bed_number = models.CharField(max_length=100, blank=True, null=True)
    icu = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')], default='no')
    billing_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='patient_photos/', null=True, blank=True)

    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.patent_title



class Medicine(models.Model):
    medicine_name = models.CharField(max_length=200)
    medicine_Avail = models.CharField(max_length=200)
    def __str__(self):
        return self.medicine_name

class Organ(models.Model):
    organ_name = models.CharField(max_length=200)
    organ_Avail = models.CharField(max_length=200)
    organ_donars = models.CharField(max_length=200)
    def __str__(self):
        return self.organ_name

class Blood(models.Model):
    blood_group = models.CharField(max_length=200)
    blood_Avail = models.CharField(max_length=200)
    blood_donars = models.CharField(max_length=200)
    def __str__(self):
        return self.blood_group