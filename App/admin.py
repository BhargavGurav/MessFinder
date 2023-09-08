from django.contrib import admin
from .models import * 
# Register your models here.
admin.site.site_header = "Mess'er Administration"


class MessOwnerAdmin(admin.ModelAdmin):
    list_display = ['mess', 'user', 'contact']
    search_fields = ['state', 'district', 'address', 'mess']


class MessMenuAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user']

admin.site.register(MessOwner, MessOwnerAdmin)
admin.site.register(MessMenu, MessMenuAdmin)

