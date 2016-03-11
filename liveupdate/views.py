from django.shortcuts import render
from liveupdate.models import Update, ViewAllTypeFields, Links, Category
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core import serializers
from django.views.generic import ListView
import os
from forms import AllFields, NewPost
from datetime import datetime
from django.contrib.auth import authenticate, login
from tasks import add

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

def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print("log/pass = ", username, password)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/detail/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        print("The username and password were incorrect.")
        return render(request, "login_page.html")


def allLinksPage(request):
    if request.method == 'GET' and request.GET.get('search') != None and request.GET.get('search') != '':
        category = Category.objects.all()
        if request.GET.get('search') != None:
            cat_id = Category.objects.get(category=request.GET.get('search'))
            links_by_cat = Links.objects.filter(category=cat_id)
        else:
            links_by_cat = None
        return render(request, "allLinksPage.html", {'links': links_by_cat, 'category': category})
    elif request.method == 'GET' and request.GET.get('category') != None and request.GET.get('category') != '':
        category = Category.objects.all()
        cat_id = Category.objects.get(category=request.GET['category'])
        links_by_cat = Links.objects.filter(category=cat_id)
        return render(request, "allLinksPage.html", {'links': links_by_cat, 'category': category})
    else:
        links = Links.objects.all()
        category = Category.objects.all()
        res = add(1)
        return render(request,"allLinksPage.html", {'links': links,'res': res,'category': category})

def linkVote(request, id):
    if request.method == 'POST' and request.GET.get('up'+id):
        pass




