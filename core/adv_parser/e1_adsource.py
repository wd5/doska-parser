# -*- coding: UTF-8 -*-
import re
from base.base import *
from lxml import etree

class E1AdSource(BaseAdSource):
    url = 'http://www.e1.ru/auto/sale/%s.html'
    description = 'Парсер автообъявлений Е1'
    group_name = 'auto'

    last_id = 935574

    img_dir = settings.PARSER_IMAGES_STORAGE
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)

    keys= {
        u'Год выпуска:': u'year',
        u'Цена в рублях:': u'price',
        u'Пробег:': u'probeg',
        u'Объем двигателя:': u'volume',
        u'Состояние:': u'state',
        u'Последнее изменение:': u'updated',
        u'Срок публикации, до:': u'valid_till',
        u'Цвет:': u'color',
        u'Тип кузова:': u'type',
        u'Тип двигателя:': u'engine_type',
        u'Привод:': u'privod',
        u'КПП:': u'kpp',
        u'Руль:': u'rul',
        u'Продавец': u'seller',
        u'Телефон:': u'phone',
        u'Адрес e-mail:': u'email',
        u'Адрес:': u'address',
        u'Факс:': u'fax'
    }

    def parse(self, source):
        """
        parse(source) -> dict
        """
        res = {}

        #добираемся до таблиц с нужной информацией
        html = etree.HTML(source.decode('cp1251'))
        body = html.find('body')
        table = body[10]
        tr = table[0]
        td = tr[3]
        tables = td.findall('table')

        res['mark'] = tables[0][0][1][0][-3].find('font')[0].text
        res['model'] = tables[0][0][1][0][-1][0].text

        self._parse_auto_info(res, tables[1][1])

        #если есть блок "Комплектация"
        if len(tables[2]) > 1:
            res['description'] = tables[5][1][0][0].text if tables[5][1][0][0].text else ''

            #Если есть блок фотографий
            if len(tables[6]) > 1:
                self._parse_auto_images(res, tables[6])
                self._parse_contacts(res, tables[9][1][0].find('table'))
            else:
                self._parse_contacts(res, tables[8][1][0].find('table'))
        else:
            res['description'] = tables[4][1][0][0].text if tables[4][1][0][0].text else ''

            #Если есть блок фотографий
            if len(tables[5]) > 1:
                self._parse_auto_images(res, tables[5])
                self._parse_contacts(res, tables[8][1][0].find('table'))
            else:
                self._parse_contacts(res, tables[7][1][0].find('table'))
        
        return res

    def _parse_contacts(self, d, table):
        #объявление подано компанией
        if len(table) > 4:
            for item in table[1:]:
                key = item[0].find('strong').text
                try:
                    item[0].text
                    d[self.keys[key]] = item[0].text
                except KeyError:
                    pass

        #объявление простых смертных
        else:
            for item in table:
                try:
                    value = item[1].text
                    if value is None:
                        continue
                    key = item[0].text
                    d[self.keys[key]] = value

                except KeyError:
                    pass

    def _parse_auto_info(self, d, tr):
        for i in (0, 1):
            for item in tr[i].find('table'):
                try:
                    key = item[0].text
                    d[self.keys[key]] = item[1][0].text
                except KeyError:
                    pass

    def _parse_auto_images(self, d, table):
        script = table[1][0].find('center').find('script').text
        reg = re.compile(ur'http://www.e1.ru/auto/sale/show_pic.php/b/\d+/f/pict.jpg')
        urls = reg.findall(script)
        imgs = []

        for url in urls:
            img_id = int(url.split('/')[-3])
            img_res = urllib2.urlopen(url)
            img_path = os.path.join(
                    self.img_dir,
                    '.'.join((str(img_id), 'jpg'))
            )
            img = open(img_path,'wb')
            img.write(img_res.read())
            img.close()

            imgs.append('.'.join((str(img_id),'jpg')))

        d['images'] = ';'.join(imgs)