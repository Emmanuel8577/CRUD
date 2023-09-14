from django.db import models

# Create your models here.
#Tables of Candidate

GENDER = (
    ('M','Male'),
    ('F', 'Female')
)
    
CAREER = (
    ('Frontend', 'Frontend'),
    ('Backend', 'Backend'),
    ('Fullstack', 'Fullstack'),
    ('Intern', 'Intern')
)


class Candidate(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    career = models.CharField(max_length=50, null=True, choices=CAREER)
    
    
    def __str__(self):
        
        return self.name
    
    