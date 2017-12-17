"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login

from mysite.views import HomeView, NewsView, LifeView, KonkursView, AboutView, SignView, ProfilePage, RegisterView
from django.conf.urls.static import static

urlpatterns = [
    url(r'accounts/login/$', login, name="login"),
    url(r'accounts/profile/$', ProfilePage.as_view(), name="profile"),
    url(r'accounts/register/$', RegisterView.as_view(), name="register"),
    url(r'^$', HomeView.as_view()),
    url(r'^news/$', NewsView.as_view()),
    url(r'^life/$', LifeView.as_view()),
    url(r'^kurs/$', KonkursView.as_view()),
    url(r'^about/$', AboutView.as_view()),
    url(r'^sign/$', SignView.as_view()),
    url(r'^admin/', admin.site.urls),
]