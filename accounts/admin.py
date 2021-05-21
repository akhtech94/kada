from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import CustomUser

class CustomUserAdmin(UserAdmin):
    username = ''

    list_display = ('email', 'is_active', 'is_shop', 'is_delivery_person', 'is_customer')

    list_filter = ()

    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_shop', 'is_delivery_person', 'is_customer', )}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        # (None, {
            # 'classes': ('wide',),
            # 'fields': ('email', 'name', 'password1', 'password2'),
        # }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
