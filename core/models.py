# coding: utf8
from django.db import models

# Create your models here.

class E1AutoAdv(models.Model):
    mark = models.CharField(verbose_name="Марка", max_length=30)
    model = models.CharField(verbose_name="Модель", max_length=30)
    year = models.IntegerField(verbose_name="Год выпуска")
    price = models.FloatField(verbose_name="Цена в рублях")
    probeg = models.IntegerField(verbose_name="Пробег", blank=True, null=True)
    volume = models.FloatField(verbose_name="Объем двигателя", blank=True, null=True)
    state = models.CharField(verbose_name="Состояние", max_length=50, blank=True, null=True)
    updated = models.DateTimeField(verbose_name="Последнее изменение")
    valid_till = models.DateTimeField(verbose_name="Срок публикации, до")
    color = models.CharField(verbose_name="Цвет", max_length=50, blank=True, null=True)
    type = models.CharField(verbose_name="Тип кузова", max_length=50, blank=True, null=True)
    engine_type = models.CharField(verbose_name="Тип двигателя", max_length=50, blank=True, null=True)
    privod = models.CharField(verbose_name="Привод", max_length=50)
    kpp = models.CharField(verbose_name="КПП", max_length=50)
    rul = models.CharField(verbose_name="Руль", max_length=50)
    seller = models.CharField(verbose_name="Продавец", max_length=200, blank=True, null=True)
    phone = models.CharField(verbose_name="Телефон", max_length=30, blank=True, null=True)
    email = models.EmailField(verbose_name="Адрес e-mail", blank=True, null=True)
    address = models.CharField(verbose_name="Адрес", max_length=300, blank=True, null=True)
    fax = models.CharField(verbose_name="Факс", max_length=30, blank=True, null=True)
    images = models.CharField(max_length=1000, blank=True, null=True)
    adv_id = models.IntegerField()
    imported = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    order_id = models.IntegerField()

    def title(self):
        return '%s %s' % (self.mark, self.model)

    def __unicode__(self):
        return self.title()