from django.contrib import admin
from testapp.models import student
class studentAdmin(admin.ModelAdmin):
    list_display=["rollno","name","dob","marks","email","phonenumber","address"]
admin.site.register(student,studentAdmin)
