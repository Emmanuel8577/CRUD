from django.contrib import admin
from .models import Candidate
# Register your models here.


class candidateadmin(admin.ModelAdmin):
    
    list_display = ['name', 'phone', 'email', 'career','gender']
    search_fields = ['name', 'phone', 'email']
    list_filter = ['career','gender']
    list_per_page = 10
    
    
admin.site.register(Candidate, candidateadmin)

