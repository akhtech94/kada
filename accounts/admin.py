from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_active', 'is_shop', 'is_delivery_person', 'is_customer')
    list_filter = ()
    fieldsets = ()#UserAdmin.fieldsets + (
    #     (None, {'fields': ('name',)}),
    # )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ( 'emai',)}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
