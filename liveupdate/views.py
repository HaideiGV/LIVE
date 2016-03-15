from django.shortcuts import render
from liveupdate.models import Update, ViewAllTypeFields, Links, Category
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core import serializers
from django.views.generic import ListView
import os
from forms import AllFields, NewLink
from django.contrib.auth import authenticate, login
from urlparse import urlparse

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
    # print(str(Category.objects.get(category=request.POST['category']).id))
    if form.is_valid():
        p = Links(
            category=Category.objects.get(pk=request.POST.get('category')),
            linkUrl='http://'+urlparse(request.POST['linkUrl']).hostname,
            rating=0,
            description=request.POST['description']
        )
        p.save()
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
    category = Category.objects.all()
    if request.GET.get('search') != None or '':
        cat_id = Category.objects.get(category=request.GET.get('search'))
        links_by_cat = Links.objects.filter(category=cat_id)
        return render(request, "allLinksPage.html", {'links': links_by_cat, 'category': category})
    elif request.GET.get('category') != None or '':
        cat_id = Category.objects.get(category=request.GET['category'])
        links_by_cat = Links.objects.filter(category=cat_id)
        return render(request, "allLinksPage.html", {'links': links_by_cat, 'category': category})
    else:
        links = Links.objects.all()
        return render(request,"allLinksPage.html", {'links': links,'category': category})


def updateRate(request):
    if request.method == 'POST':
        if 'rateValue' in request.POST:
            rateValue = request.POST.get('rateValue')
            print(rateValue)
            if request.POST.get('up'):
                print(rateValue)
                return HttpResponse('up')
            elif request.POST.get('down'):
                print(rateValue)
                return HttpResponse('down')
    return HttpResponse('Error')


def ajax_update(request):
    if request.is_ajax():
        print(request.is_ajax())
        request_data = request.POST
        print(request_data)
        return HttpResponse("OK")


