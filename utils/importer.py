# coding: utf8

def parser_import(parser_name):
    try:
        module, class_name = parser_name.rsplit('.', 1)
    except ValueError:
        raise Exception('Wrong parser in settings.py')
    try:
        module = __import__(module, globals(), locals(), ['*'])
        parser = getattr(module, class_name)
    except ImportError, e:
        raise Exception('Can not import parser. %s' % e)

    return parser