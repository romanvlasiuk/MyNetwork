from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

admin.site.unregister(User)

class UserProfileInline(admin.TabularInline):
        model = UserProfile
        fk_name = 'user'
        max_num = 1

class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline,]
    list_display = ('username', 'email', 'is_staff','is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active',)


admin.site.register(User, CustomUserAdmin)