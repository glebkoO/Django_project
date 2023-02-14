from django.db import models

class Desk(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Тема')
    context = models.TextField(max_length=250, verbose_name='Сообщение')
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ='важная новость'
        verbose_name_plural ='новости проекта'

    def __str__(self):
        return self.context
