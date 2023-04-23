from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    middle_name = models.CharField(_('По батькові'), max_length=100, blank=True, null=True)


specAn_CHOICES = (
    ('', 'Вид тварини'),
    ('Собака', 'Собака'),
    ('Кіт', 'Кіт'),
    ('Інше', 'Інше'),
)

reason_CHOICES = (
    ('', 'Причина візиту:'),
    ('Вакцинація', 'Вакцинація'),
    ('Огляд', 'Огляд'),
    ('Косметичні процедури', 'Косметичні процедури'),
    ('Лікування', 'Лікування'),
)


class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specAn = models.CharField(max_length=255, choices=specAn_CHOICES, verbose_name='Вид тварини')
    nameAnim = models.CharField(max_length=255, verbose_name='Кличка вихованця')
    reason = models.CharField(max_length=255, choices=reason_CHOICES, verbose_name='Причина візиту')
    phone = models.CharField(max_length=255)
    textArea = models.CharField(max_length=255, null=True, blank=True)

    def str(self):
        return self.phone
