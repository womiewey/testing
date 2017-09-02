from django.db import models

# Create your models here.

class Accounts(models.Model):
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Accounts'