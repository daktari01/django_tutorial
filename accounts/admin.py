from django.contrib import admin
from accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'phone', 'website', 'user_info')

    def user_info(self, obj):
        return obj.description 

    user_info.short_description = 'Info'

admin.site.register(UserProfile, UserProfileAdmin)