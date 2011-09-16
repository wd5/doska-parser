# coding: utf8
from django.core.management import call_command
from django.test.client import Client
from django.utils import unittest
from core.models import Adv
import settings


class ParserTest(unittest.TestCase):
    def test_parse(self):
        args = []
        kwargs = {}

        call_command('get_doska_fields', *args, **kwargs)
        call_command('parse_advs', 1, **kwargs)

        advs = Adv.objects.all()
        self.assertEqual(len(advs), len(settings.PARSERS_ENABLED))