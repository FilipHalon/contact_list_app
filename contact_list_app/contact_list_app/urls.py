"""contact_list_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from contact_list_app.contacts.views import Index, AddANewContact, ModifyAContact, DeleteAContact, ContactDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', Index.as_view(), name='index'),
    path('new/', AddANewContact.as_view(), name='new'),
    re_path(r'^modify/(?P<contact_id>\d+)$', ModifyAContact.as_view(), name='modify'),
    re_path(r'^delete/(?P<contact_id>\d+)$', DeleteAContact.as_view(), name='delete'),
    re_path(r'^details/(?P<contact_id>\d+)$', ContactDetails.as_view(), name='details'),
]
