# coding: utf8
from django.core.management.base import BaseCommand
import settings
from utils.importer import parser_import
from core.models import Adv

class Command(BaseCommand):
    def handle(self, *args, **options):

        for enabled_parser in settings.PARSERS_ENABLED:
            parser = parser_import(enabled_parser)
            adsource = parser(50, 30)
            for ad in adsource:
                new_adv = Adv()
                new_adv.parse(ad, adsource)