# -*- coding: UTF-8 -*-

import e1_adsource
from lxml import etree

class E1PrintAdSource(e1_adsource.E1AdSource):
    url = 'http://www.e1.ru/auto/sale/print/%s.html'

    def parse(self, source):
        """
        parse(source) -> dict
        """
        res = {}

        #добираемся до таблиц с нужной информацией
        html = etree.HTML(source.decode('cp1251'))
        body = html.find('body')
        tables = body.findall('table')

        l = tables[0][0][0].find('font').text.split()
        if len(l) > 2:
            res['mark'] = ' '.join(l[:-1])
            res['model'] = l[-1]
        else:
            res['mark'], res['model'] = l

        self._parse_auto_info(res, tables[0][1])

        #если есть блок "Комплектация"
        if len(tables[1][1]) > 1:
            res['description'] = tables[2][1][0][0].text if tables[2][1][0][0].text else ''

            #если есть картинки
            if len(tables[3][1][0]) > 1:
                self._parse_auto_images(res, tables[3])
                self._parse_contacts(res, tables[4][1][0].find('table'))
            else:
                self._parse_contacts(res, tables[3][1][0].find('table'))
        else:
            res['description'] = tables[1][1][0][0].text if tables[1][1][0][0].text else ''

            #если есть картинки
            if len(tables[2][1][0]) > 1:
                self._parse_auto_images(res, tables[2])
                self._parse_contacts(res, tables[3][1][0].find('table'))
            else:
                self._parse_contacts(res, tables[2][1][0].find('table'))

        return res

for ad in E1PrintAdSource(50, 15):
    print ad
    print '*'*50
    print