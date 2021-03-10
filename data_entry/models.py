from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Darbar(models.Model):
    darbar_name = models.CharField(max_length=500)
    darbar_city = models.CharField(max_length=500)


class Post(models.Model):
    Occupation_CHOICES = (
        ('Healthcare and medicine', 'Healthcare and medicine'),
        ('Arts and entertainment', 'Arts and entertainment'),
        ('Business', 'Business'),
        ('Industrial and manufacturing', 'Industrial and manufacturing'),
        ('Engineer', 'Engineer'),
        ('Law enforcement and armed forces', 'Law enforcement and armed forces'),
        ('Science and technology', 'Science and technology'),
        ('Transport', 'Transport'),
        ('Service(Labour)', 'Service(Labour)')
    )
    Darbar_Choices = (('Shri Anand Niwas Satsang, Memnagar', 'Shri Anand Niwas Satsang, Memnagar',),
                      ('Shri Anand Niwas Satsang, Maninagar', 'Shri Anand Niwas Satsang, Maninagar'),
                      ('Shri Anand Niwas Satsang, SardarNagar', 'Shri Anand Niwas Satsang, Sardarnagar'),
                      ('Shri Anand Niwas Satsang, Sahjpur', 'Shri Anand Niwas Satsang, Sahjpur'))
    Blood_Choices = (
        ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('Not Known', 'Not Known'))
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
    full_Name = models.CharField(max_length=300)
    spouse_Name = models.CharField(max_length=300, blank=True, null=True)
    father_Name = models.CharField(max_length=300)
    mother_Name = models.CharField(max_length=300)
    Occupation = models.CharField(max_length=500, null=True, choices=Occupation_CHOICES)
    Gender = models.CharField(null=True, max_length=100)
    blood_Group = models.CharField(max_length=100, null=True, choices=Blood_Choices)
    birth_date = models.DateField()
    phone = PhoneNumberField(blank=True)
    Darbar = models.CharField(max_length=500, default='Please Select Darbar', null=True, choices=Darbar_Choices)
    Address = models.CharField(max_length=500, default="Please Enter Address")
    Pincode = models.CharField(max_length=6, default="Please Enter Pincode")
    image = models.ImageField(upload_to="images/")
    publishing_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    flag = models.BooleanField(default=True)
    city = models.CharField(max_length=200, default=None)

    class Meta:
        db_table = "post"

    def __str__(self):
        return self.full_Name
