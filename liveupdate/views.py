from django.shortcuts import render
from liveupdate.models import Update
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response

def update(request):
    object_list = Update.objects.all()
    return render_to_response('update_list.html', {'object_list': object_list})
