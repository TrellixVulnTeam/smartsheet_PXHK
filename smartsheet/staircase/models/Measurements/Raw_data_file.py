from django.db import models
from django.utils import timezone
from .. import Foup

def add_raw_data_file(instance,filename):
    #define the location of the file to upload to
    return f'{instance.type}/{timezone.now().strftime("%Y-%m-%d")}/{filename}'

class Raw_data_file(models.Model):
    type=models.CharField(max_length=200,default='thickness')
    foup=models.ForeignKey(Foup, on_delete=models.SET_NULL,blank=True,null=True)
    rawDataFile=models.FileField(upload_to=add_raw_data_file,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)    #creation time
    note=models.CharField(max_length=200,null=True,blank=True)