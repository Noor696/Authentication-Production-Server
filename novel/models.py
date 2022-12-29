from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Novel(models.Model):

    name = models.CharField(max_length=200)
    auther = models.CharField(max_length=200 , null=True)
    publisher = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    rate = models.IntegerField(default=0, null=True, blank=True)
    price = models.FloatField()
    image = models.CharField(max_length=200 , null=True)
    publisher = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-pk"]


    
