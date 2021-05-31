from django.contrib import admin
from .models import Poll, Option


class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'date_create', 'date_finish')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'author')


class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'poll', 'text', 'number_of_voices')
    list_display_links = ('id', 'text')
    search_fields = ('text', 'poll')
    list_filter = ('poll',)


admin.site.register(Poll, PollAdmin)
admin.site.register(Option, OptionAdmin)
