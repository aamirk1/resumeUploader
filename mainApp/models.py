from django.db import models

# Create your models here.
STATE_CHOICES = [
('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh','Arunachal Pradesh'),
('Assam','Assam'),
('Bihar','Bihar'),
('Chandigarh','Chandigarh'),
('Chattishgarh','Chattishgarh'),
('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
('Daman & Diu','Daman & Diu'),
('Delhi','Delhi'),
('Goa','Goa'),
('Gujrat','Gujrat'),
('Haryana','Haryana'),
('Himachal Pradesh','Himachal Pradesh'),
('Jammu & Kashmir','Jammu & Kashmir'),
('Jharkhand','Jharkhand'),
('Karnataka','Karnataka'),
('Kerala','Kerala'),
('Lashhadweep','Lashhadweep'),
('Madhya Pradesh','Madhya Pradesh'),
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),
('Meghalaya','Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Odisha','Odisha'),
('Puducherry','Puducherry'),
('Punjab','Punjab'),
('Tamil Nadu','Tamil Nadu'),
('Rajasthan','Rajasthan'),
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'),
('Telangana','Telangana'),
('Tripura','Tripura'),
('Uttarakhan','Uttarakhan'),
('Utter Pradesh','Utter Pradesh'),
('West Bengal','West Bengal'),
]
class Resume(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices = STATE_CHOICES,max_length=100) 
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileImg',blank=True)
    my_file = models.FileField(upload_to='doc',blank=True)
