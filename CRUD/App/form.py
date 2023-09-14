from .models import Candidate
from django import forms




class CandidateList(forms.ModelForm):
    
    class Meta:
       models = Candidate
       fieds = '__all__'
       
    