from django.db import models

# Create your models here.

class EmpModel(models.Model):
    CHOICES =(('1','Developer'),('2','System Admin'),('3','HR'),
                ('4','Data Analyst'),('5','Finance')
            )
    first_name = models.CharField(max_length=60,null=False, blank=False)
    last_name = models.CharField(max_length=60, blank=True)
    department = models.CharField(max_length=20,choices=CHOICES,blank=False)
    image = models.ImageField(max_length=255,upload_to='static/images/')

    def __str__(self):
        if(self.last_name):
            return self.first_name +" "+self.last_name
        else:
            return self.first_name
