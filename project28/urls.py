"""
URL configuration for project28 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),

    path('string_by_fbv/',string_by_fbv,name='string_by_fbv'),
    path('Stringby_cbv/',Stringby_cbv.as_view(),name='Stringby_cbv'),


    path('htmlbyfbv/',htmlbyfbv,name='htmlbyfbv'),
    path('htmlbycbv/',htmlbycbv.as_view(),name='htmlbycbv'),


    path('insert_data_fbv/',insert_data_fbv,name='insert_data_fbv'),
    path('insert_data_cbv/',insert_data_cbv.as_view(),name='insert_data_cbv'),
    path('Template_View/',Template_View.as_view(),name='Template_View'),

]
