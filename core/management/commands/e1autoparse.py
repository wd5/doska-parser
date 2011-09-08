# coding: utf8
from django.core.management.base import BaseCommand
from core.models import E1AutoAdv
from core.adv_parser.e1print_adsource import E1PrintAdSource
from datetime import datetime
from time import strptime

class Command(BaseCommand):
    def handle(self, *args, **options):
        adsource = E1PrintAdSource(50, 30)
        for ad in adsource:
            print "Parsing adv %s" % adsource.get_current_id()
            new_adv = E1AutoAdv()
            new_adv.mark = ad.get('mark', '')
            new_adv.model = ad.get('model', '')
            new_adv.year = ad.get('year', 0)
            new_adv.price = ad.get('price', 0)
            new_adv.probeg = ad.get('probeg', 0)
            new_adv.volume = ad.get('volume', 0)
            new_adv.state = ad.get('state', '')
            updated = ad.get('updated', None)
            if updated:
                new_adv.updated = datetime(*strptime(updated, '%d.%m.%Y %H:%M')[:5])
            valid_till = ad.get('valid_till', None)
            if valid_till:
                new_adv.valid_till = datetime(*strptime(valid_till, '%d.%m.%Y')[:5])
            new_adv.color = ad.get('color', '')
            new_adv.type = ad.get('type', '')
            new_adv.engine_type = ad.get('engine_type', '')
            new_adv.privod = ad.get('privod', '')
            new_adv.kpp = ad.get('kpp', '')
            new_adv.rul = ad.get('rul', '')
            new_adv.seller = ad.get('seller', '')
            new_adv.phone = ad.get('phone', '')
            new_adv.email = ad.get('email', '')
            new_adv.address = ad.get('address', '')
            new_adv.fax = ad.get('fax', '')
            new_adv.images = ad.get('images', '')
            new_adv.adv_id = adsource.get_current_id()
            new_adv.order_id = 1
            new_adv.save()