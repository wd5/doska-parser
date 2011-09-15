# coding: utf8
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from time import strptime
from django.utils import simplejson

class Adv(models.Model):
    group_name = models.CharField(max_length=30)
    adv_data = models.TextField()
    with_images = models.BooleanField(default=False)
    adv_id = models.IntegerField()
    imported = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    order_id = models.IntegerField()
    blocked_by = models.ForeignKey(User, blank=True, null=True)
    blocked_when = models.DateTimeField(blank=True, null=True)

    def parse(self, ad, adsource):
        self.group_name = adsource.group_name
        if ad.get('images'):
            self.with_images = True
        self.adv_data = simplejson.dumps(ad)
        self.adv_id = adsource.get_current_id()
        self.order_id = 1
        self.save()

class E1AutoAdv(models.Model):
    group_name = 'auto'

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
    
    def parse(self, ad, adsource):
        self.mark = ad.get('mark', '')
        self.model = ad.get('model', '')
        self.year = ad.get('year', 0)
        self.price = ad.get('price', 0)
        self.probeg = ad.get('probeg', 0)
        self.volume = ad.get('volume', 0)
        self.state = ad.get('state', '')
        updated = ad.get('updated', None)
        if updated:
            self.updated = datetime(*strptime(updated, '%d.%m.%Y %H:%M')[:5])
        valid_till = ad.get('valid_till', None)
        if valid_till:
            self.valid_till = datetime(*strptime(valid_till, '%d.%m.%Y')[:5])
        self.color = ad.get('color', '')
        self.type = ad.get('type', '')
        self.engine_type = ad.get('engine_type', '')
        self.privod = ad.get('privod', '')
        self.kpp = ad.get('kpp', '')
        self.rul = ad.get('rul', '')
        self.seller = ad.get('seller', '')
        self.phone = ad.get('phone', '')
        self.email = ad.get('email', '')
        self.address = ad.get('address', '')
        self.fax = ad.get('fax', '')
        self.images = ad.get('images', '')
        self.adv_id = adsource.get_current_id()
        self.order_id = 1
        self.save()

    def title(self):
        return '%s %s' % (self.mark, self.model)

    def __unicode__(self):
        return self.title()

class DoskaField(models.Model):
    group_name = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.field_name

    class META:
        unique_together = (('group_name', 'field_name'),)

class Map(models.Model):
    imported_adv_class = models.CharField(max_length=200)
    doska_field_name = models.CharField(max_length=50)
    imported_field_name = models.CharField(max_length=50, blank=True, null=True)