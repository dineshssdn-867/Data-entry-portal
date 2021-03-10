from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['full_Name', 'spouse_Name', 'father_Name', 'mother_Name', 'Occupation', 'Gender', 'blood_Group', 'birth_date', 'phone', 'Darbar','Address','Pincode','image']