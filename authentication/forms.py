from django import forms
from .models import Students


# Student Form for new student addition
class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('student_id', 'student_name', 'phone_no_field', 'date_of_birth', 'address', 'parent', 'classroomid')
        labels = {
            'student_id' : 'Student ID',
            'student_name': 'Student Name',
            'phone_no_field' : 'Phone Number',
            'date_of-birth' : 'Date of Birth (yyyy-mm-dd)',
            'address' : 'Address',
            'parent' : 'Parent ID',
            'classroomid' : 'Classroom ID'
        }

    def clean_stu(self):
        stuid = self.cleaned_data.get('student_id')

        # Check to see if any users already exist with this same student id
        try:
            match = Students.objects.get(student_id=stuid)
        except Students.DoesNotExist:
            # Unable to find a user
            return stuid

        raise forms.ValidationError('This Student ID is already in use.')

    def __init__(self,*args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['parent'].widget = forms.TextInput()
        self.fields['classroomid'].widget = forms.TextInput()



