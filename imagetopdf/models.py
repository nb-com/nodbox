from django.db import models

class imagetopdf(models.Model):
    
    images = models.ImageField(upload_to='files/images/')
    
    def __str__(self):
        return self.images