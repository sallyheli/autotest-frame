from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json

# Create your views here.
def Login(request):
    if request.method == 'GET':
        username = request.GET.get("username")
        password = request.GET.get("password")
        dic_list ={
            "username" : username,
            "password" : password
        }
        return HttpResponse(json.dumps(dic_list),content_type="application/json;charset=utf-8")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        dic_list = {
            "username": username,
            "password": password
        }
        return HttpResponse(json.dumps(dic_list), content_type="application/json;charset=utf-8")
    else:
        return render_to_response('denglu.html')