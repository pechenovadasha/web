"""askme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('question/<int:question_id>', views.question, name='question'),
    path('log_in', views.log_in, name='log_in'),
    path('settings', views.settings, name='settings'),
    path('new_question', views.new_question, name='new_question'),
    path('filter_tag', views.filter_tag, name='filter_tag'),
    path('registration', views.registration, name='registration'),
    path('tag/<str:tag_id>', views.tag, name='tag'),
    path('hot', views.hot, name='hot'),


]
