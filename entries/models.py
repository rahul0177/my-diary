from django.db import models
from django.urls import reverse

# Create your models here.
class Entry(models.Model):
    text=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True) 
    
    

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural='entries'
    
    def get_absolute_url(self):
        return reverse('detail_entry', args=[str(self.id)])
