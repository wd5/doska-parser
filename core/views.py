from django.template.context import RequestContext
from models import E1AutoAdv
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def _go_back(request):
    ref = request.META.get('HTTP_REFERER')
    if ref:
        return redirect(ref)
    else:
        return redirect(reverse('core.views.list'))

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required()
def list(request):
    advs = E1AutoAdv.objects.filter(imported=False, deleted=False).order_by('-order_id', 'updated')
    return render_to_response('list.html', locals(), context_instance=RequestContext(request))

@login_required()
def next(request):
    adv = E1AutoAdv.objects.filter(imported=False, deleted=False).order_by("-order_id")[0]
    return render_to_response('adv_show.html', locals(), context_instance=RequestContext(request))

@login_required()
def adv_show(request, id):
    adv = E1AutoAdv.objects.get(adv_id=id, deleted=False)
    return render_to_response('adv_show.html', locals(), context_instance=RequestContext(request))

@login_required()
def adv_import(request, id):
    adv = E1AutoAdv.objects.get(adv_id=id, deleted=False)
    adv.imported = True
    adv.save()
    return _go_back(request)

@login_required()
def adv_delete(request, id):
    adv = E1AutoAdv.objects.get(adv_id=id)
    adv.deleted = True
    adv.save()
    return _go_back(request)

@login_required()
def adv_wait(request, id):
    last_order_id = E1AutoAdv.objects.all().order_by("order_id")[0].order_id
    adv = E1AutoAdv.objects.get(adv_id=id)
    adv.order_id = last_order_id - 1
    adv.save()
    return _go_back(request)