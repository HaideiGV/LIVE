from django.shortcuts import render
from liveupdate.models import Update
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
from django.core import serializers
import math
import os


def update(request):
    object_list = Update.objects.all()
    return render_to_response('update_list.html', {'object_list': object_list})

def scripts(request, name):
    data = open(os.path.join('media/js',name), 'rb').read()
    return HttpResponse(data)

def updates_after(request, id):
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(serializers.serialize("json", Update.objects.filter(pk__gt=id)))
    return response

def type_post(request):
    num = sum(Update.objects.get())
    if request.method == 'post':
        p = Update(text=request.POST['type_post'], id = num+1)
        p.save()
    object_list = Update.objects.all()
    return render_to_response('update_list.html', {'object_list': object_list})
