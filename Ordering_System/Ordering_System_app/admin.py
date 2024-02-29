from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Restaurant, dish, category, Contact_msg, WebsiteInfo, Area, CustomOwnerCreationForm


class CustomOwnerAdmin(admin.ModelAdmin):
    # Add your custom admin configuration for the Restaurant model here
    # For example:
    list_display = ['Res_Name', 'Res_Email', 'Res_Phone']
    search_fields = ['Res_Name', 'Res_Email', 'Res_Phone']


admin.site.register(Restaurant, CustomOwnerAdmin)
# Register your models here.
# admin.site.register(Restaurant)
admin.site.register(dish)
admin.site.register(category)
admin.site.register(Contact_msg)
admin.site.register(WebsiteInfo)
admin.site.register(Area)
admin.site.site_header = "OFOSA"
admin.site.site_title = "Online Food Ordering System"
admin.site.index_title = "Online Food Ordering System"
