"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main.views import Main
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import ListViews
from contacts.views import contact
from calculator.views import add


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Main.as_view(), name = 'main'),
    url(r'^portfolio/$', ListViews.as_view(), name = 'portfolio'),
    url(r'^news/', include('news.urls')),
    url(r'^contact/$', contact, name="contact"),
    url(r'^calc/$', add, name="add"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
