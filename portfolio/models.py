from django.db import models
from django import forms
from django.db import models
from django.forms import ModelForm

class query(models.Model):
    Name=models.CharField(max_length=350)
    contact=models.BigIntegerField()
    message=models.CharField(max_length=400)
    Time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

    class Meta:
        db_table="shivpquery"