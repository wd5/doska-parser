# -*- coding: UTF-8 -*-

import urllib2
import httplib
import shelve
import os, sys
import random
import settings

class NoProxyException(StopIteration):
    pass

class BaseAdSource(object):
    """Базовый класс для источников объявлений"""

    #URL объявления. Необходимо переопределить в дочернем классе
    url = ''

    #Стартовый номер объявления. Берется при первом использовании.
    last_id = 1

    def __init__(self, total_num_404=50, total_adv_num=Ellipsis):
        self.total_num_404 = total_num_404
        self.total_adv_num = total_adv_num
        self.adv_count = 0
        self._proxy_list = []

        try:
            path = os.path.dirname(__file__)
            f = shelve.open(os.path.join(path, 'states.db'))
            self.last_id = int(f[self.__class__.__name__])
            f.close()
        except KeyError:
            pass

        self.curr_id = self.last_id

    def __iter__(self):
        return self

    def next(self):
        if self.adv_count >= self.total_adv_num:
            self._write_state()
            raise StopIteration

        res = self._do_request_until_success()
        self.last_id = self.curr_id
        
        if self.total_adv_num is not Ellipsis:
            self.adv_count += 1

        return self.parse(res.read())

    def _do_request_until_success(self):
        """
        Выполняет запросы, пока не получит успешный
        ответ или не превысит число ошибок 404
        """
        count_404 = 0

        if not self._proxy_list:
            try:
                proxy_list = [host[:-1] for host in urllib2.urlopen(settings.PROXY_LIST_URL).readlines()]
                self._proxy_list = filter(self._nonzero_port, proxy_list)
            except urllib2.URLError:
                raise NoProxyException

        proxy_count = len(self._proxy_list)

        while count_404 < self.total_num_404:
            proxy_num = random.randint(0, proxy_count - 1)

            http_proxy = 'http://%s:%s@%s' % (
                settings.PROXY_USER,
                settings.PROXY_PASS,
                self._proxy_list[proxy_num]
            )

            proxy_handler = urllib2.ProxyHandler({
                'http': http_proxy
            })
            opener = urllib2.build_opener(proxy_handler)
            urllib2.install_opener(opener)

            self.curr_id += 1

            try:
                return urllib2.urlopen(self.url % str(self.curr_id))
            except urllib2.HTTPError, e:
                if e.code == 404:
                    count_404 += 1
            except urllib2.URLError:
                pass
            except httplib.BadStatusLine:
                pass

        self._write_state()
        raise StopIteration

    def _nonzero_port(self, host):
        l = host.split(':')
        return not bool( (len(l) < 2) or (l[-1] in ('0','0000')) )

    def _write_state(self):
        path = os.path.dirname(__file__)
        f = shelve.open(os.path.join(path, 'states.db'))
        f[self.__class__.__name__] = self.last_id
        f.close()

    def parse(self, source):
        """Парсит ответ"""
        pass