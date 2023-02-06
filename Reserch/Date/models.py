from django.db import models

# Create your models here.
# class Date(models.Model):
#     GENDER_CHOIСES = [('m', 'mal'), ('f', 'femal')]
#     STATUS_CHOICES = [('s', 'single'), ('m', 'married'), ('d', 'divosed'), ('w', 'widow/er')]
#     created = models.DateTimeField(auto_now_add=True, verbose_name='Дата заполнения')
#     case = models.CharField(max_length=200, db_index=True, verbose_name='ФИО')
#     gender = models.CharField(max_length=1, choices=GENDER_CHOIСES, verbose_name='пол')
#     age = models.IntegerField(min_value=16, verbose_name='возраст')
#     status = models.CharField(min_lenth=1, choices=STATUS_CHOICES, verbose_name='социальный статус')
#     efficiency = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='эффективность работы')
#     workability = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='врабатываемость')
#     menstab = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='устойчивость')
#     IQV = models.IntegerField(min_value=20, max_value=160, verbose_name='IQверб')
#     IQN = models.IntegerField(min_value=20, max_value=160, verbose_name='IQневерб')
#     iq = models.IntegerField(min_value=20, max_value=160, verbose_name='IQобщ')
#     resercher = models.ForeignKey('User', on_delete=models.PROTECT, related_name='base_date', null=True, blank=True,
#     verbose_name='Исследователь')
#
#     def __str__(self):
#         return self.case
#     def get_absolute_url(self):
#         return reverse('post', kwargs={'post_id': self.pk})
# class User(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
