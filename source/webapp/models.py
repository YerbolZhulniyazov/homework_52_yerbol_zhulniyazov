from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=40, null=False, blank=False, default='new', verbose_name='Статус')
    completion_date = models.CharField(max_length=50, default="", verbose_name="Дата")

    def __str__(self):
        return f"{self.title} - {self.status}"
