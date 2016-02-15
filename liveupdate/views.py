from django.shortcuts import render
from liveupdate.models import Update, ViewAllTypeFields
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
from django.core import serializers
from django.views.generic import ListView
import os
from forms import AllFields, NewPost
from datetime import datetime

def update(request):
    object_list = Update.objects.all()
    return render_to_response('update_list.html', {'object_list': object_list})

def scripts(request, name):
    data = open(os.path.join('static/js',name), 'rb').read()
    return HttpResponse(data)

def updates_after(request, id):
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(serializers.serialize("json", Update.objects.filter(pk__gt=id)))
    return response

def all_type_input_form(request):
    form = AllFields()
    return render(request, 'message.html', {'form':form})

def new_post(request):
    form = NewPost(request.POST or None)
    if form.is_valid():
        p = Update(text=form['text'].value(), timestamp=datetime.now())
        p.save()
    return render(request, 'new_post.html', {'form': form})

class allView(ListView):
    model = ViewAllTypeFields
    template_name = 'detail_list.html'




