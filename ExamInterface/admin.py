from django.contrib import admin
from .models import Exam,UserExam,Question

# Register your models here.
admin.site.register(Exam)
admin.site.register(UserExam)
admin.site.register(Question)