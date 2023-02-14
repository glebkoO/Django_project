from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Date(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата заполнения')
    name = models.CharField(max_length=200, db_index=True, blank=True, verbose_name='фамилия')
    
    class Gender(models.TextChoices):
        MALE = 'm', 'мужской'
        FEMAL = 'f', 'женский'
        __empty__ = 'уточнить пол'

    gender = models.CharField(max_length=1, choices=Gender.choices, verbose_name='пол')
    age = models.IntegerField(verbose_name='возраст')

    class Status(models.TextChoices):
        SINGLE = 's', 'холост/не замужем'
        MARRIED = 'm', 'в браке'
        DIVORSED = 'd', 'в разводе'
        WIDOW_ER = 'w', 'вдов_а'
    status = models.CharField(max_length=1, choices=Status.choices, verbose_name='социальный статус')
    efficiency = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default='some_value', verbose_name='эффективность работы')
    workability = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='врабатываемость')
    mentalstab = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='устойчивость')
    IQV = models.IntegerField(verbose_name='IQверб')
    IQN = models.IntegerField(verbose_name='IQневерб')
    iq = models.IntegerField(verbose_name='IQобщ')
    slug = models.SlugField(unique=True)
    resercher = models.CharField(max_length= 200, blank=True, null=True, verbose_name='Исследователь')

    class Meta:
        verbose_name = 'исследуемый'
        verbose_name_plural = 'исследуемые'
    def __str__(self):
        return '%s %s %s %s' % (self.created, self.name, self.age, self.iq)

    def get_absolute_url(self):
        return reverse('myurl', kwargs={'name': self.slug, 'id': self.pk})
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#
#     def __str__(self):
#         return f'{self.user.username} Profile'