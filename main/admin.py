from django.contrib import admin
from .models import *


# Register your models here.


class FakeNewsAdmin(admin.ModelAdmin):
    list_display = ('description', 'answer', 'correct')
    list_filter = ('description',)
    search_fields = ['description', ]


class FakeCardGameAdmin(admin.ModelAdmin):
    list_display = ('description', 'answer', )
    list_filter = ('description',)
    search_fields = ['description', ]


admin.site.register(FakeNews, FakeNewsAdmin)
admin.site.register(FakeCardGame, FakeCardGameAdmin)
