from django.contrib import admin
from users.models import fb_users, gplus_users, users

admin.site.register(fb_users)
admin.site.register(gplus_users)
admin.site.register(users)
