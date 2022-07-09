from tabnanny import verbose
from django.db import models

# Create your models here.


class Homebg(models.Model):
    name = models.CharField('Homebg name', max_length=30)
    about = models.TextField('Homebg about')
    img = models.ImageField('Homebg image ', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Homebg'
        verbose_name_plural = 'Homebgs'