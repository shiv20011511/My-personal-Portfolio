from django import forms 
from portfolio.models import query

class shivpquery(forms.ModelForm):

    class Meta:
        model=query
        fields=['Name','contact','message']