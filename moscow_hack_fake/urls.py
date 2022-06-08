"""moscow_hack_fake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main.views import *
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/fakecards/', FakeCardGameAPIList.as_view()),
    path('api/v1/fakenews/', FakeNewsAPIListCreate.as_view()),
    path('docs/', include_docs_urls(title='Fake News API')),
    path('api/schema/', get_schema_view(
        title='Fake News API',
        description='API for fake news, Moscow Hack',
        version='1.0',
    ), name='openapi-schema'),
]
