from django.db import models
from django.db import models
from django.utils import timezone
from datetime import datetime

class SuperUser(models.Model):
    user = models.OneToOneField(
        'auth.user',
        on_delete=models.CASCADE,
    )
    name = models.CharField(default="", max_length=128)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=13, null=True)

    def __str__(self):
        return self.name

def getday():
 return datetime.now().day

def gettime():
 return datetime.now().time()

def AutoDateTimeField():
 return datetime.now().strftime("%b")

class Notice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    notice_title = models.CharField(default="", max_length=200)
    notice_description = models.CharField(default="", max_length=1000)

    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='notice_board/', blank=True, null=True)

    # created_at = models.DateField(default=datetime.now())
    month = models.CharField(default=AutoDateTimeField(),null=True, blank=True,max_length=12)
    time = models.CharField(default=gettime(),null=True, blank=True,max_length=200)
    day= models.CharField(default=getday(), null=True, blank=True,max_length=20)

    def __str__(self):
        return self.notice_title




class facultydb(models.Model):
    objects = models.Manager()
    faculty_id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(default="", max_length=200)
    faculty_department = models.CharField(blank=True, null=True, max_length=200)
    faculty_email = models.EmailField()
    designation = models.CharField(default="", max_length=200)

    def __str__(self):
        return self.faculty_name



class Resume(models.Model):
    objects = models.Manager()
    faculty = models.OneToOneField(facultydb, on_delete=models.CASCADE)
    address = models.CharField(blank=True, null=True, max_length=128)
    mob = models.CharField(blank=True, null=True, max_length=10)
    faculty_contact_info= models.CharField(default="", max_length=200)
    faculty_qualification = models.CharField(default="", max_length=200)
    faculty_bio = models.CharField(default="", max_length=2000)
    faculty_pic = models.FileField(upload_to='faculty/resume/', blank=True, null=True)

    def __str__(self):
        return self.faculty.faculty_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'


class resultdb(models.Model):
    result_id = models.AutoField(primary_key=True)
    result_title = models.CharField(default="", max_length=200)
    result_description = models.CharField(default="", max_length=1000,blank=True)

    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='result/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.result_title




class eventsdb(models.Model):
    events_id = models.AutoField(primary_key=True)
    events_title = models.CharField(default="", max_length=200)

    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='events/', blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(default="", max_length=200)

    month = models.CharField(default=AutoDateTimeField(), null=True, blank=True, max_length=12)
    time = models.CharField(default=gettime(), null=True, blank=True, max_length=200)
    day = models.CharField(default=getday(), null=True, blank=True, max_length=20)


    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.events_title

class tenderdb(models.Model):
    tender_id = models.AutoField(primary_key=True)
    tender_department = models.CharField(default="", max_length=200)
    tender_name_no = models.CharField(default="", max_length=200)
    tender_contactinfo = models.CharField(default="", max_length=1000)

    opening_date = models.DateTimeField(blank=True, null=True)
    last_date = models.DateTimeField(blank=True, null=True)
    upload=models.FileField(upload_to='tender/', blank=True, null=True)


    def __str__(self):
        return self.tender_name_no



class careerdb(models.Model):
    career_id = models.AutoField(primary_key=True)
    career_department = models.CharField(default="", max_length=200)
    name_of_the_post = models.CharField(default="", max_length=200)
    no_of_vacancies= models.CharField(default="", max_length=200)
    last_date = models.DateTimeField(blank=True, null=True)
    dt_of_notice=models.DateTimeField(auto_now_add=True,blank=True, null=True)

    full_notification = models.FileField(upload_to='career/', blank=True, null=True)

    qualification =models.CharField(default="", max_length=1000)

    application_form =models.FileField(upload_to='career/', blank=True, null=True)

    def __str__(self):
        return self.name_of_the_post


class hod(models.Model):
    faculty = models.OneToOneField(facultydb, on_delete=models.CASCADE)
    dept =models.CharField(default="", max_length=1000)
    def __str__(self):
        return self.faculty.faculty_name
