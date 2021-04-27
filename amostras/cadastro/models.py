from django.db import models

# Create your models here.

from django.db import models

class Inscricao(models.Model):
        model = models.CharField(max_length=100)
        number = models.CharField('number', max_length=15, unique=True)
        hardware = models.CharField(max_length=100)
        supplier = models.CharField(max_length=100)
        location = models.CharField(max_length=100)
        created = models.DateTimeField('created in', auto_now_add=True)

        class Meta:
                ordering = ['created']
                verbose_name = (u'model')
                verbose_name_plural = (u'models')

        def __unicode__(self):
                return self.model

