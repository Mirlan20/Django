from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    work = models.CharField(max_length=255, verbose_name=u"Рабочий номер", null=True, blank=True)

    def __str__(self):
        return self.name