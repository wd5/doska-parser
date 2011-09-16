# coding: utf8
from django.core.management.base import BaseCommand
import settings
from utils.importer import parser_import
from core.models import Adv, Map

class Command(BaseCommand):
    def handle(self, *args, **options):

        try:
            advs_to_parse = int(args[0])
        except:
            advs_to_parse = 20

        for enabled_parser in settings.PARSERS_ENABLED:
            map_schema = Map.objects.filter(imported_adv_class=enabled_parser)
            if not map_schema:
                raise Exception('Необходимо создать схему соответствия полей досок объявлений.')

            parser = parser_import(enabled_parser)

            adsource = parser(50, advs_to_parse)
            for ad in adsource:
                new_adv = Adv()
                new_adv.parse(ad, adsource, map_schema)