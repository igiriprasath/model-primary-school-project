from django.db import models

class data(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mob_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name
