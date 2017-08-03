from django.shortcuts import render
from page.models import *
from django.http import HttpResponse

# Create your views here.
def index(request,id):
    #cat_id = request.GET("id")
    if id == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk=id)
    goods = Good.objects.filter(category=cat).order_by('name')
    s = "Категория: " + cat.name + "<br><br>"
    for good in goods:
        s = s + "(" + str(good.pk) + ")" +good.name +"<br>"
    return HttpResponse(s)

def good(request):
    return ""