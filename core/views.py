from django.template.context import RequestContext
from django.utils import simplejson
from models import DoskaField, Map, Adv
import settings
from utils.importer import parser_import
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
from datetime import datetime, timedelta

def _go_back(request):
    ref = request.META.get('HTTP_REFERER')
    if ref and '/next/' in ref:
        return redirect(ref)
    else:
        return redirect(reverse('core.views.adv_list'))

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
def adv_list(request):
    advs = Adv.objects.filter(imported=False, deleted=False).order_by('-order_id')
    advs = advs.filter(Q(blocked_when__lt=datetime.now()-timedelta(minutes=settings.ADV_BLOCK_MINUTES))|Q(blocked_by=request.user)|Q(blocked_by=None))
    return render_to_response('list.html', locals(), context_instance=RequestContext(request))

@login_required
def next(request):
    advs = Adv.objects.filter(imported=False, deleted=False).order_by('-order_id')
    if not advs:
        queue_is_empty = True
    else:
        adv = advs.filter(Q(blocked_when__lt=datetime.now()-timedelta(minutes=settings.ADV_BLOCK_MINUTES))|Q(blocked_by=request.user)|Q(blocked_by=None))[0]
        adv.blocked_by = request.user
        adv.blocked_when = datetime.now()
        adv.save()
        adv_data = []
        for k, v in simplejson.loads(adv.adv_data).items():
            if isinstance(v, list):
                v = '[%s]' % ', '.join(v)
            adv_data.append((k, v))
#        adv_data = [(k, v) for k, v in simplejson.loads(adv.adv_data).items()]
    return render_to_response('adv_show.html', locals(), context_instance=RequestContext(request))

@login_required
def adv_show(request, id):
    adv = Adv.objects.get(adv_id=id, deleted=False)
    adv.blocked_by = request.user
    adv.blocked_when = datetime.now()
    adv.save()
    adv_data = [(k, v) for k, v in simplejson.loads(adv.adv_data).items()]
    return render_to_response('adv_show.html', locals(), context_instance=RequestContext(request))

@login_required
def adv_import(request, id):
    adv = Adv.objects.get(adv_id=id, deleted=False)
    adv.imported = True
    adv.blocked_by = adv.blocked_when = None
    adv.save()
    return _go_back(request)

@login_required
def adv_delete(request, id):
    adv = Adv.objects.get(adv_id=id)
    adv.deleted = True
    adv.blocked_by = adv.blocked_when = None
    adv.save()
    return _go_back(request)

@login_required
def adv_wait(request, id):
    last_order_id = Adv.objects.all().order_by("order_id")[0].order_id
    adv = Adv.objects.get(adv_id=id)
    adv.order_id = last_order_id - 1
    adv.save()
    return _go_back(request)

@login_required
def mapping(request, parser_name):
    parser = parser_import(parser_name)

    doska_fields = [f.field_name for f in DoskaField.objects.filter(group_name='auto').order_by('field_name')]
    imported_fields = sorted([''] + parser.all_fields)
    
    if request.method == 'POST':
        for f_name in doska_fields:
            m_rule, _ = Map.objects.get_or_create(imported_adv_class=parser_name, doska_field_name=f_name)
            m_rule.imported_field_name = request.POST.get(f_name, '')
            m_rule.save()

        return redirect(reverse('core.views.mapping_list'))

    maps = Map.objects.filter(imported_adv_class=parser_name)
    maps_dict = dict([(m.doska_field_name, m.imported_field_name) for m in maps])
    map_fields = [(df, maps_dict.get(df)) for df in doska_fields]

    return render_to_response('mapping.html', locals(), context_instance=RequestContext(request))

@login_required
def mapping_list(request):
    parser_names = zip(settings.PARSERS_ENABLED, [parser_import(p).description for p in settings.PARSERS_ENABLED])
    return render_to_response('mapping_list.html', locals(), context_instance=RequestContext(request))