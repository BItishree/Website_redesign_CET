from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("academics", views.academics, name="academics"),
    path("admission", views.admission, name="admission"),
    path("autonomous", views.autonomous, name="autonomous"),
    path("departments", views.departments, name="departments"),
    path("career", views.career, name="career"),
    path("student", views.student, name="student"),
    path("faculty", views.faculty, name="faculty"),
    path("about", views.about, name="about"),
    path("bggoverning", views.bggoverning, name="bggoverning"),
    path("contactus", views.contactus, name="contactus"),
    path("gallery", views.gallery, name="gallery"),
    path("teqip", views.teqip, name="teqip"),
    path("tender", views.tender, name="tender"),
    path("rti", views.rti, name="rti"),
    path("noticeboard", views.noticeboard, name="noticeboard"),
    path("upcomingevents", views.upcomingevents, name="upcomingevents"),
    path("facilities", views.facilities, name="facilities"),

    path("ugsyllabus", views.ugsyllabus, name="ugsyllabus"),
    path("pgsyllabus", views.pgsyllabus, name="pgsyllabus"),
    path("acadregulationforug", views.acadregulationforug, name="acadregulationforug"),
    path("acadregulationforpg", views.acadregulationforpg, name="acadregulationforpg"),
    path("calendar", views.calendar, name="calendar"),
    path("result", views.result, name="result"),
    path("examschedule", views.examschedule, name="examschedule"),
    path("phd", views.phd, name="phd"),
    path("individual_faculty", views.individual_faculty, name="individual_faculty"),

    path("UGExamSchedule", views.UGExamSchedule, name="UGExamSchedule"),
    path("PGExamSchedule", views.PGExamSchedule, name="PGExamSchedule"),

    path('superuser_logout/', views.superuser_logout, name='superuser_logout'),
    path('superuser_login', views.superuser_login, name="superuser_login"),
    path('superuser_homepage', views.superuser_homepage, name="superuser_homepage"),

    path('adminNoticeUI', views.adminNoticeUI, name="adminNoticeUI"),
    path('adminFacultyUI',views.adminFacultyUI, name="adminFacultyUI"),
    path('adminResultUI', views.adminResultUI, name="adminResultUI"),
    path('adminEventsUI', views.adminEventsUI, name="adminEventsUI"),
    path('adminTenderUI', views.adminTenderUI, name="adminTenderUI"),
    path('adminCareerUI', views.adminCareerUI, name="adminCareerUI"),

    path('adminNoticeForm', views.adminNoticeForm, name="adminNoticeForm"),
    path('adminFacultyForm',views.adminFacultyForm, name="adminFacultyForm"),
    path('adminResultForm', views.adminResultForm, name="adminResultForm"),
    path('adminEventsForm', views.adminEventsForm, name="adminEventsForm"),
    path('adminTenderForm', views.adminTenderForm, name="adminTenderForm"),
    path('adminCareerForm', views.adminCareerForm, name="adminCareerForm"),


    path('faculty_dept/<slug:dept_name>/', views.faculty_dept, name="faculty_dept"),
    path('faculty_more/<int:faculty_id>/', views.faculty_more, name="faculty_more"),


    path('dept_chem', views.dept_chem, name="dept_chem"),
    path('dept_phy', views.dept_phy, name="dept_phy"),
    path('dept_math', views.dept_math, name="dept_math"),
    path('dept_planning', views.dept_planning, name="dept_planning"),
    path('dept_te', views.dept_te, name="dept_te"),
    path('dept_me', views.dept_me, name="dept_me"),
    path('dept_iee', views.dept_iee, name="dept_iee"),
    path('dept_fat', views.dept_fat, name="dept_fat"),
    path('dept_cse', views.dept_cse, name="dept_cse"),
    path('dept_it', views.dept_it, name="dept_it"),

    path('dept_civil', views.dept_civil, name="dept_civil"),
    path('dept_bio', views.dept_bio, name="dept_bio"),
    path('dept_ee', views.dept_ee, name="dept_ee"),
    path('dept_mca', views.dept_mca, name="dept_mca"),
    path('dept_arch', views.dept_arch, name="dept_arch"),




]
