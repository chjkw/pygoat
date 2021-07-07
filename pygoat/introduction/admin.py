from django.contrib import admin

from .models import FAANG, comments, info, login, otp

# Register your models here.
admin.site.register(FAANG)
admin.site.register(info)
admin.site.register(login)
admin.site.register(comments)
admin.site.register(otp)
