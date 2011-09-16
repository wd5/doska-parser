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

    def parse(self, ad, adsource, map_schema=None):
        self.group_name = adsource.group_name
        if ad.get('images'):
            self.with_images = True

        if map_schema:
            map_dict = dict([(m.imported_field_name, m.doska_field_name) for m in map_schema])
            mapped_ad = {}
            for k, v in ad.items():
                mapped_field = map_dict.get(k, k)
                mapped_ad[mapped_field] = v
            self.adv_data = simplejson.dumps(mapped_ad)
        else:
            self.adv_data = simplejson.dumps(ad)
            
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