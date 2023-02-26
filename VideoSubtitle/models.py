#
# # Create your models here.
from django.db import models
# from django.forms import ModelForm
# from django.forms import forms
#
#


class VideoSubtitle(models.Model):
    name= models.CharField(max_length=500)
    video= models.FileField(upload_to='videos/%y', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.video)
#
#
