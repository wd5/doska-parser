from django.template.context import RequestContext
from models import E1AutoAdv, DoskaField
import settings
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
from datetime import datetime, timedelta

def _go_back(request):
    ref = request.META.get('HTTP_REFERER')
    if ref:
        return redirect(ref)
    else:
        return redirect(reverse('core.views.list'))

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
def list(request):
    advs = E1AutoAdv.objects.filter(imported=False, deleted=False).order_by('-order_id', '-updated')
    advs = advs.filter(Q(blocked_when__lt=datetime.now()-timedelta(minutes=settings.ADV_BLOCK_MINUTES))|Q(blocked_by=request.user)|Q(blocked_by=None))
    return render_to_response('list.html', locals(), context_instance=RequestContext(request))

@login_required
def next(request):
    advs = E1AutoAdv.objects.filter(imported=False, deleted=False).order_by('-order_id', '-updated')
    adv = advs.filter(Q(blocked_when__lt=datetime.now()-timedelta(minutes=settings.ADV_BLOCK_MINUTES))|Q(blocked_by=request.user)|Q(blocked_by=None))[0]
    adv.blocked_by = request.user
    adv.blocked_when = datetime.now()
    adv.save()
    return render_to_response('adv_show.html', locals(), context_instance=RequestContext(request))

@login_required
def adv_show(request, id):
    adv = E1AutoAdv.objects.get(adv_id=id, deleted=False)
    adv.blocked_by = request.user
    adv.blocked_when = datetime.now()
    adv.save()
    return render_to_response('adv_show.html', locals(), context_instance=RequestContext(request))

@login_required
def adv_import(request, id):
    adv = E1AutoAdv.objects.get(adv_id=id, deleted=False)
    adv.imported = True
    adv.blocked_by = adv.blocked_when = None
    adv.save()
    return _go_back(request)

@login_required
def adv_delete(request, id):
    adv = E1AutoAdv.objects.get(adv_id=id)
    adv.deleted = True
    adv.blocked_by = adv.blocked_when = None
    adv.save()
    return _go_back(request)

@login_required
def adv_wait(request, id):
    last_order_id = E1AutoAdv.objects.all().order_by("order_id")[0].order_id
    adv = E1AutoAdv.objects.get(adv_id=id)
    adv.order_id = last_order_id - 1
    adv.save()
    return _go_back(request)

@login_required
def mapping(request):
    doska_fields = DoskaField.objects.filter(group_name='auto').order_by('field_name')
    imported_fields = sorted([''] + [f.name for f in E1AutoAdv._meta.fields])
    return render_to_response('mapping.html', locals())