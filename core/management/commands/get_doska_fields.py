# coding: utf8
from django.core.management.base import BaseCommand
from core.models import DoskaField
from utils.importer import parser_import
import settings
import urllib2
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        for enabled_parser in settings.PARSERS_ENABLED:
            parser = parser_import(enabled_parser)
            group_name = parser.group_name
            response = urllib2.urlopen('http://localhost:5000/doska/ajax/get_adv_fields/%s/' % group_name)
            if response.getcode() == 200:
                data = json.loads(response.read())
                if data.get('status') == 0:
                    fields = data.get('value')
                    DoskaField.objects.filter(group_name=group_name).delete()
                    for f in fields:
                        d_field = DoskaField(group_name=group_name, field_name=f)
                        d_field.save()
        