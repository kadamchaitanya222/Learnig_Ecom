from django.db import models

# Create your models here.
class sign_up(models.Model):

    name=models.CharField(max_length=45)
    email=models.EmailField()
    def __str__(self):

        return self.name
