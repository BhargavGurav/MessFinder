from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.cache import cache_control 
from django.contrib import messages 
from .models import *
import requests 

# from django.contrib.gis.utils import GeoIP
# from ip2geotools.databases.noncommercial import DbIpCity

# Create your views here.

def home(request):
    
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]

    else:
        ip = request.META.get('REMOTE_ADDR')

    # try:
    #     response = DbIpCity.get(ip, api_key='free')
    #     location = response.country + " | " + response.city
    # except:
    #     location = "Not known"

    # print(location)

    details = []
    # mess_owners = MessOwner.objects.all()
    for i in MessMenu.objects.all():
        # print(i)
        details.append([i, MessOwner.objects.get(user=i.user.user)])
    context = {}
    context['owner_detail'] = details
    context['ip'] = ip
    # context['city'] = city

    # api_key = 'aa2652a772d0410cbaf300ff7982e6da'
    # api_url = f'https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address={ip}'
    # response = requests.get(api_url)
    # print(response.content)
    return render(request, 'home.html', context)

@cache_control(no_store=True, must_revalidade=True, no_cache=True)
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        # print(username, password)
        
        if User.objects.filter(username=username):  
            usr = authenticate(username=username, password=password)
            if usr:
                login(request, usr)
                messages.success(request, 'Login successful.')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Wrong username or password.')
                return HttpResponseRedirect('loginUser')
        else:
            messages.error(request, 'No user found.')
            return HttpResponseRedirect('/')
            

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mess = request.POST.get('mess-name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        state = request.POST.get('state')
        district = request.POST.get('district')
        address = request.POST.get('address')
        password = request.POST.get('password')

        
        if len(password) < 8:
            messages.error(request, 'Password must be 8 character long.')
            return HttpResponseRedirect('/')

        if not any(x.isdigit() for x in password):
            messages.error(request, 'Password must contain at least one digit.')
            return HttpResponseRedirect('/')

        if not any(x.islower() for x in password):
            messages.error(request, 'Password must contain at least one small letter.')
            return HttpResponseRedirect('/')

        if not any(x.isupper() for x in password):
            messages.error(request, 'Password must contain at least one capital letter.')
            return HttpResponseRedirect('/')

        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = fname
            user.last_name = lname
            user.is_staff = True
            user.save()

            mess_owner = MessOwner(user=user, mess=mess, contact=mobile, state=state, district=district, address=address)
            mess_owner.save()
            mess_menu = MessMenu(user=mess_owner)
            mess_menu.save()

            messages.success(request, 'Registered successfully')
            return HttpResponseRedirect('/')

    return render(request, 'register.html')

@login_required(login_url='loginUser')
def profile(request):
    logged_user = MessOwner.objects.get(user=request.user)
    context = {}
    context['owner'] = logged_user


    if request.method == 'POST':
        item1 = request.POST.get('item1')
        item2 = request.POST.get('item2')
        item3 = request.POST.get('item3')
        item4 = request.POST.get('item4')
        item5 = request.POST.get('item5')
        item6 = request.POST.get('item6')
        item7 = request.POST.get('item7')
        item8 = request.POST.get('item8')
        item9 = request.POST.get('item9')
        item10 = request.POST.get('item10')

        mess_menu = MessMenu.objects.get(user=logged_user)
        mess_menu.item1 = item1
        mess_menu.item2 = item2
        mess_menu.item3 = item3
        mess_menu.item4 = item4
        mess_menu.item5 = item5
        mess_menu.item6 = item6
        mess_menu.item7 = item7
        mess_menu.item8 = item8
        mess_menu.item9 = item9
        mess_menu.item10 = item10
        mess_menu.save()
        messages.success(request, 'Menu Updated successfully')
        return HttpResponseRedirect('/')

    mess_menu = MessMenu.objects.get(user=logged_user)
    context['menu'] = mess_menu
    return render(request, 'profile.html', context)

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def logoutuser(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return HttpResponseRedirect('/')