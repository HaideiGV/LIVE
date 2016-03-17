from django.shortcuts import render
from liveupdate.models import Update, ViewAllTypeFields, Links, Category
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.core import serializers
from django.views.generic import ListView
import os
from forms import AllFields, NewLink
from django.contrib.auth import authenticate, login
from urlparse import urlparse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def update(request):
    object_list = Update.objects.all()
    return render_to_response('update_list.html', {'object_list': object_list})

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

# @login_required
def allLinksPage(request):
    error = []
    category = Category.objects.all()
    links = Links.objects.all()
    if request.GET.get('search') != None or '':
        try:
            cat_id = Category.objects.get(category=request.GET.get('search').lower())
            links_by_cat = Links.objects.filter(category=cat_id)
        except:
            error.append("We have not such category. Please try again or send me a letter for add new category.")
            links_by_cat = Links.objects.all()
        return render(request, "allLinksPage.html", {'links': links_by_cat, 'category': category, 'error': error})
    elif request.GET.get('category') != None or '':
        cat_id = Category.objects.get(category=request.GET['category'])
        links_by_cat = Links.objects.filter(category=cat_id)
        return render(request, "allLinksPage.html", {'links': links_by_cat, 'category': category})
    else:
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

def about(request):
    return render(request, "about.html")


def likes(request):
    context = RequestContext(request)
    rate = None
    link = request.GET.get('name_link')
    print(link)
    if request.method == 'GET':
        rate = request.GET.get('rate')
        link_id = request.GET.get('name_link')
        print(rate)
        print(link_id)
    like = 0
    if rate:
        rate = Links.objects.get(linkUrl=link_id).get('rating')
        print(rate)
        if rate:
            like = rate.rating + 1
            rate.rating = like
            rate.save()

    return HttpResponse(like)
