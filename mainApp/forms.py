from django import forms
from .models import Resume


GERNDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female')
]

JOB_CITY_CHOICES = [
    ('Delhi','Delhi'),
    ('Pune','Pune'),
    ('Mumbai','Mumbai'),
    ('Banglore','Banglore'),
    ('Hyderabad','Hyderabad')

]
class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GERNDER_CHOICES,widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferrd Job Locations',choices=JOB_CITY_CHOICES,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields =  ['name','dob','gender','locality','city',
    'pin','state','mobile','email','job_city','profile_image','my_file']
        
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),


        }
        
        labels = {'name':'Full Name','dob':'Date Of Birth','gender':'Gender','locality':'Locality','city':'City',
    'pin':'Pin Code','state':'State','mobile':'Mobile','email':'Email ID','profile_image':'Profile Image','my_file':'Document'}