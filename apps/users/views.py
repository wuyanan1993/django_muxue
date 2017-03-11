from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login

# Create your views here.


def my_login(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get('password', "")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            data = {

            }
            return render(request, "index.html", data)
    elif request.method == 'GET':
        data = {

        }
        return render(request, "login.html", data)