from django.contrib import admin
from .models import Students, Parents, Classrooms, FinalExamMarks, Exammarks
# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    raw_id_fields = ("parent",)

admin.site.register(Students)
admin.site.register(Exammarks)
admin.site.register(FinalExamMarks)
