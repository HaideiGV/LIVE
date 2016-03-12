from django.shortcuts import render
from liveupdate.models import Update, ViewAllTypeFields, Links, Category
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core import serializers
from django.views.generic import ListView
import os
from forms import AllFields, NewLink
from django.contrib.auth import authenticate, login

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


def new_link(request):
    form = NewLink(request.POST or None)
    if form.is_valid():
        if Links.objects.filter(request.POST['linkUrl']) == None:
            p = Links(
                category=Category.objects.get(id=int(request.POST['category'])),
                linkUrl=request.POST['linkUrl'],
                description=request.POST['description']
            )
            p.save()
    # print(Links.objects.get(linkUrl=request.POST['linkUrl']))
    return render(request, 'new_link.html', {'form': form})


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
        return render(request,"allLinksPage.html", {'links': links,'res': res,'category': category})

def linkVote(request, id):
    if request.method == 'POST' and request.GET.get('up'+id):
        pass




