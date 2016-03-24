from django.shortcuts import render
from liveupdate.models import Update, ViewAllTypeFields, Links, Category
from django.http import HttpResponse,  HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import ListView, FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from urlparse import urlparse
from django.core import serializers
from forms import NewLink, AllFields


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

@login_required
def new_link(request):
    form = NewLink(request.POST or None)
    if form.is_valid():
        p = Links(
            category=Category.objects.get(pk=request.POST.get('category')),
            linkUrl='http://'+urlparse(request.POST['linkUrl']).hostname,
            rating=0,
            description=request.POST['description']
        )
        p.save()
        return HttpResponseRedirect('/')
    return render(request, 'new_link.html', {'form': form})


class allView(ListView):
    model = ViewAllTypeFields
    template_name = 'detail_list.html'


class UserView(FormView):
    model = User
    form_class = UserCreationForm
    success_url = '/register_success/'
    template_name = 'register_form.html'


def register_success(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            p = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, "register_form.html", {'form': form})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")

def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return render(request, "login_page.html")

@login_required
def allLinksPage(request):
    error = []
    category = Category.objects.all()
    links = Links.objects.all()
    if request.GET.get('search') != None or '':
        try:
            query = request.GET.get('search').lower()
            cat_id = Category.objects.filter(category__icontains=query).values('id')
            print(cat_id)
            links_by_cat = Links.objects.filter(category__in=cat_id)
        except:
            error.append("We have not such category. Please try again or send me a letter for add new category.")
            links_by_cat = []
        return render(request, "allLinksPage.html", {'links': links_by_cat, 'category': category, 'error': error})
    elif request.GET.get('category') != None or '':
        cat_id = Category.objects.get(category=request.GET['category'])
        links_by_cat = Links.objects.filter(category=cat_id)
        return render(request, "allLinksPage.html", {'links': links_by_cat, 'category': category})
    else:
        return render(request,"allLinksPage.html", {'links': links,'category': category})


def ajax_update(request):
    if request.is_ajax():
        print(request.is_ajax())
        request_data = request.POST
        print(request_data)
        return HttpResponse("OK")

def about(request):
    return render(request, "about.html")


def likes(request):
    rate = 0
    error = []
    if request.method == 'GET':
        link = request.GET.get('link_id')
        like = request.GET.get('like')
        dislike = request.GET.get('dislike')
        link_data = Links.objects.filter(pk=int(link))[0]
        if link_data and like:
            link_data.rating += 1
            rate = int(link_data.rating)
            link_data.save()
            return HttpResponse(rate, {'error': error})
        elif link_data and dislike:
            link_data.rating -= 1
            rate = int(link_data.rating)
            link_data.save()
            return HttpResponse(rate, {'error': error})
        else:
            error.append("You are already vote this link!")
            link_data = Links.objects.filter(pk=int(link))[0]
            rate = link_data.rating
            return HttpResponse(rate, {'error': error})
    else:
        return HttpResponse(rate, {'error': error})


def filter_rate(request):
    if request.is_ajax():
        rate_value = request.GET.get('filter_value')
        lnk = Links.objects.filter(rating__lt=int(rate_value))
        return HttpResponse(lnk)
    else:
        lnk = Links.objects.all()
        return HttpResponse(lnk)