from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class Parents(models.Model):
    parent_id = models.IntegerField(db_column='Parent_ID', primary_key=True)  # Field name made lowercase.
    parent_name = models.CharField(db_column='Parent Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Parents'

class Classrooms(models.Model):
    classroom_id = models.IntegerField(db_column='Classroom_ID', primary_key=True)  # Field name made lowercase.
    standard = models.IntegerField(db_column='Standard')  # Field name made lowercase.
    section = models.TextField(db_column='Section')  # Field name made lowercase. This field type is a guess.
    no_of_students = models.IntegerField(db_column='No_of_students', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Classrooms'

class Students(models.Model):
    student_id = models.IntegerField(db_column='Student_ID', primary_key=True, unique= True)  # Field name made lowercase.
    student_name = models.CharField(db_column='Student Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_no_field = models.BigIntegerField(db_column='Phone No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    date_of_birth = models.DateField(db_column='Date of Birth')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parent = models.ForeignKey(Parents, models.DO_NOTHING, db_column='Parent_ID')  # Field name made lowercase.
    classroomid = models.ForeignKey(Classrooms, models.DO_NOTHING, db_column='ClassroomID', null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Students'


class Exammarks(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    studentid = models.ForeignKey('Students', models.DO_NOTHING, db_column='StudentID')  # Field name made lowercase.
    classroomid = models.ForeignKey(Classrooms, models.DO_NOTHING, db_column='ClassroomID')  # Field name made lowercase.
    science = models.IntegerField(db_column='Science')  # Field name made lowercase.
    maths = models.IntegerField(db_column='Maths')  # Field name made lowercase.
    english = models.IntegerField(db_column='English')  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ExamMarks'

    def __str__(self):
        return self.studentid.student_name


# Auth token generation on User creation
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
