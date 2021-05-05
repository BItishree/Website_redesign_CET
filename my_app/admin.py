from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from  .models import *



admin.site.register(SuperUser)
admin.site.register(Notice)
admin.site.register(facultydb)
admin.site.register(eventsdb)
admin.site.register(resultdb)
admin.site.register(careerdb)
admin.site.register(tenderdb)
admin.site.register(Resume)
admin.site.register(hod)