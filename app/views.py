from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

def string_by_fbv(request):
    return HttpResponse('<h1> string_by_fbv </h1>')


class Stringby_cbv(View):
    def get(self,request):
        return HttpResponse('<h1>stringby_cbv </h1>')


def htmlbyfbv (request):
    return render(request,'htmlbyfbv.html')

class htmlbycbv(View):
    def get(request):
        return render(request,'htmlbycbv.html')

def insert_data_fbv(request):
    d={'ESFO':SchoolForm()}
    if request.method=='POST':
        EFDO=SchoolForm(request.POST)
        if EFDO.is_valid():
            EFDO.save()
            return HttpResponse('insert_data_fbv is done')
        else:
            return render('not done')
    return render(request,'insert_data_fbv.html',d)



class insert_data_cbv(View):
    def get(self,request):
        d={'ESCO':SchoolForm()}
        return render(request,'insert_data_cbv.html',d)

    def post(self,request):
        EFDO=SchoolForm(request.POST)
        if EFDO.is_valid():
            EFDO.save()
            return HttpResponse('insert_data_cbv is done')
        else:
            return HttpResponse('Invalid data')

class Template_View(TemplateView):
    template_name='Template_View.html'