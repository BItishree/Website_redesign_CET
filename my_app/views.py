from django.shortcuts import render
from django.contrib.auth.models import auth,User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Notice,facultydb,resultdb,careerdb,eventsdb,tenderdb,Resume,hod
# Create your views here.


def home(request):
    return render(request, 'index.html')
def academics(request):
    return render(request, 'academics.html')
def admission(request):
    return render(request, 'admission.html')
def autonomous(request):
    return render(request, 'autonomous.html')
def departments(request):
    return render(request, 'departments.html')


def career(request):
    n = careerdb.objects.order_by('career_id')
    return render(request, 'career.html',{'n':n})


def student(request):
    return render(request, 'student.html')
def faculty(request):
    return render(request, 'faculty.html')
def about(request):
    return render(request, 'about.html')
def bggoverning(request):
    return render(request, 'bggoverning.html')
def contactus(request):
    return render(request, 'contactus.html')
def gallery(request):
    return render(request, 'gallery.html')
def teqip(request):
    return render(request, 'teqip.html')


def tender(request):
    n = tenderdb.objects.order_by('tender_id')
    return render(request, 'tender.html',{"n":n})


def rti(request):
    return render(request, 'rti.html')


def noticeboard(request):
    n = Notice.objects.order_by('notice_id')
    for i in n:
        print(i.month)
        print(i.time)
        print(i.day)
    return render(request, 'noticeboard.html',{'n':n})


def upcomingevents(request):
    n = eventsdb.objects.order_by('events_id')
    return render(request, 'upcomingevents.html',{"n":n})
def facilities(request):
    return render(request, 'facilities.html')


def ugsyllabus(request):
    return render(request, 'ugsyllabus.html')

def pgsyllabus(request):
    return render(request, 'pgsyllabus.html')
def acadregulationforug(request):
    return render(request, 'acadregulationforug.html')
def acadregulationforpg(request):
    return render(request, 'acadregulationforpg.html')
def calendar(request):
    return render(request, 'calendar.html')
def result(request):
    return render(request, 'resultUI.html')
def examschedule(request):
    return render(request, 'examscedule.html')
def phd(request):
    return render(request, 'phd.html')
def individual_faculty(request):
    return render(request, 'individual_faculty.html')

def UGExamSchedule(request):
    return render(request, 'UGExamSchedule.html')
def PGExamSchedule(request):
    return render(request, 'PGExamSchedule.html')



def superuser_homepage(request):
    if request.user.is_authenticated:
        return render(request,'panel_admin.html')
    else:
        return redirect('superuser_login')

def superuser_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,"    ", password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            try:
                    auth.login(request, user)
                    print("admin Login successfully")
                    return redirect(superuser_homepage)

            except:
                return redirect('superuser_login')


        else:
            return redirect('superuser_login')


    else:
        return render(request ,'superuser_login.html')



def superuser_logout(request):
    auth.logout(request)
    return render(request,'index.html')



def adminNoticeUI(request):
    n=Notice.objects.order_by('notice_id')
    return render(request,'adminNoticeUI.html',{"n":n})
def adminFacultyUI(request):
    n=facultydb.objects.order_by('faculty_id')
    return render(request,'adminFacultyUI.html',{"n":n})
def adminEventsUI(request):
    n=eventsdb.objects.order_by('events_id')
    return render(request,'adminEventsUI.html',{"n":n})
def adminResultUI(request):
    n=resultdb.objects.order_by('result_id')
    return render(request,'adminResultUI.html',{"n":n})
def adminCareerUI(request):
    n=careerdb.objects.order_by('career_id')
    return render(request,'adminCareerUI.html',{"n":n})
def adminTenderUI(request):
    n=tenderdb.objects.order_by('tender_id')
    return render(request,'adminTenderUI.html',{"n":n})

@login_required
def adminNoticeForm(request):

    if request.method == 'POST' :
        title = request.POST.get('notice_title')
        desc = request.POST.get('notice_description')
        newnotice =Notice(notice_title=title,notice_description=desc)
        newnotice.save()
        if 'upload' in request.FILES:
            attachment = request.FILES['upload']
            newnotice.upload = attachment
        print("saved in database")
        newnotice.save()
        return redirect(adminNoticeUI)

    else:
        return render(request, 'adminNoticeForm.html')



@login_required
def adminFacultyForm(request):

    if request.method == 'POST' :
        name = request.POST.get('faculty_name')
        print(name)
        dept = request.POST.get('faculty_department')
        print(dept)
        email = request.POST.get('faculty_email')
        designation = request.POST.get('designation')

        newfaculty = facultydb(faculty_name=name , faculty_department=dept,faculty_email=email,designation=designation)

        newfaculty.save()
        resume = Resume(faculty=newfaculty)

        #save in faculty resume
        address = request.POST.get('address')
        mob = request.POST.get('mob')
        faculty_contact_info = request.POST.get('faculty_contact_info')
        faculty_qualification = request.POST.get('faculty_qualification')
        faculty_bio = request.POST.get('faculty_bio')

        resume.address = address
        resume.mob = mob
        resume.faculty_contact_info = faculty_contact_info
        resume.faculty_qualification = faculty_qualification
        resume.designation = designation
        resume.faculty_bio = faculty_bio

        resume.save()
        if 'faculty_pic' in request.FILES:
            attachment = request.FILES['faculty_pic']
            resume.faculty_pic = attachment

        resume.save()

        print("saved in database")
        return redirect(adminFacultyUI)
    else:
        return render(request, 'adminFacultyForm.html')



@login_required
def adminEventsForm(request):

    if request.method == 'POST' :
        events_title = request.POST.get('events_title')
        start_time= request.POST.get('start_time')
        end_time= request.POST.get('end_time')
        location = request.POST.get('location')
        date = request.POST.get('date')

        newevents = eventsdb(events_title=events_title,start_time=start_time,end_time=end_time,location=location,date=date)
        newevents.save()
        if 'upload' in request.FILES:
            attachment = request.FILES['upload']
            print(attachment)
            newevents.upload=attachment
        print("saved in database")

        newevents.save()
        return redirect(adminEventsUI)

    else:
        return render(request, 'adminEventsForm.html')



@login_required
def adminResultForm(request):

    if request.method == 'POST' :
        result_title = request.POST.get('result_title')
        result_description = request.POST.get('result_description')
        # date = request.POST.get('date')

        newresult = resultdb(result_title=result_title, result_description=result_description)
        newresult.save()
        if 'upload' in request.FILES:
            attachment = request.FILES['upload']
            newresult.upload = attachment
        print("saved in database")

        newresult.save()
        return redirect(adminResultUI)

    else:
        return render(request, 'adminResultForm.html')




@login_required
def adminTenderForm(request):

    if request.method == 'POST' :
        tender_department = request.POST.get('tender_department')
        tender_name_no = request.POST.get('tender_name_no')
        tender_contactinfo = request.POST.get('tender_contactinfo')

        opening_date = request.POST.get('opening_date')
        last_date = request.POST.get('last_date')

        newtender = tenderdb(tender_department=tender_department,tender_name_no=tender_name_no,tender_contactinfo=tender_contactinfo,opening_date=opening_date,last_date=last_date)
        newtender.save()
        if 'upload' in request.FILES:
            attachment = request.FILES['upload']
            newtender.upload=attachment
        newtender.save()
        print("saved in database")
        return redirect(adminTenderUI)

    else:
        return render(request, 'adminTenderForm.html')




@login_required
def adminCareerForm(request):

    if request.method == 'POST' :
        career_department = request.POST.get('career_department')
        name_of_the_post = request.POST.get('name_of_the_post')
        no_of_vacancies = request.POST.get('no_of_vacancies')
        last_date = request.POST.get('last_date')
        qualification = request.POST.get('qualification')

        newcareer = careerdb(career_department=career_department,name_of_the_post=name_of_the_post,no_of_vacancies=no_of_vacancies,last_date=last_date,qualification=qualification)
        newcareer.save()
        if 'full_notification' in request.FILES:
            attachment = request.FILES['full_notification']
            newcareer.full_notification = attachment

        if 'application_form' in request.FILES:
            attachment = request.FILES['application_form']
            newcareer.application_form = attachment

        newcareer.save()
        print("saved in database")
        return redirect(adminCareerUI)

    else:
        return render(request, 'adminCareerForm.html')

def faculty_dept(request,dept_name):
    print(dept_name)
    Lecturer = facultydb.objects.filter(faculty_department=dept_name,designation="Lecturer")
    Assistant_Professor = facultydb.objects.filter(faculty_department=dept_name,designation="Assistant Professor")
    Associate_Professor = facultydb.objects.filter(faculty_department=dept_name,designation="Associate Professor")
    Professor = facultydb.objects.filter(faculty_department=dept_name,designation="Professor")
    head= hod.objects.filter(dept=dept_name)

    # for i in depttt:
    #     print(i.faculty_email)
    #     print(i.designation)
    print(head)
    print(head[0])

    return render(request,"faculty_dept.html",{'hod':head[0],'dept_name':dept_name,'l':Lecturer,'asstp':Assistant_Professor,'assop':Associate_Professor})


def faculty_more(request,faculty_id):
    f = facultydb.objects.get(faculty_id=faculty_id)
    return render(request,'faculty_more.html',{"f":f})



def dept_chem(request):
    return render(request,'dept_chem.html')
def dept_phy(request):
    return render(request,'dept_phy.html')
def dept_math(request):
    return render(request,'dept_math.html')
def dept_planning(request):
    return render(request,'dept_planning.html')
def dept_te(request):
    return render(request,'dept_te.html')
def dept_me(request):
    return render(request,'dept_me.html')
def dept_iee(request):
    return render(request,'dept_iee.html')
def dept_fat(request):
    return render(request,'dept_fat.html')
def dept_cse(request):
    return render(request,'dept_cse.html')
def dept_it(request):
    return render(request,'dept_it.html')
def dept_civil(request):
    return render(request,'dept_civil.html')
def dept_bio(request):
    return render(request,'dept_bio.html')
def dept_ee(request):
    return render(request,'dept_ee.html')
def dept_mca(request):
    return render(request,'dept_mca.html')
def dept_arch(request):
    return render(request,'dept_arch.html')


