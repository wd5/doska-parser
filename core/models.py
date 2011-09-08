# coding: utf8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class E1AutoAdv(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    probeg = models.CharField(max_length=30, blank=True, null=True)
    volume = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    updated = models.DateTimeField()
    valid_till = models.DateTimeField()
    color = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    engine_type = models.CharField(max_length=50, blank=True, null=True)
    privod = models.CharField(max_length=50)
    kpp = models.CharField(max_length=50)
    rul = models.CharField(max_length=50)
    seller = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    images = models.CharField(max_length=1000, blank=True, null=True)
    adv_id = models.IntegerField()
    imported = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    order_id = models.IntegerField()
    blocked_by = models.ForeignKey(User, blank=True, null=True)
    blocked_when = models.DateTimeField(blank=True, null=True)

    def title(self):
        return '%s %s' % (self.mark, self.model)

    def __unicode__(self):
        return self.title()