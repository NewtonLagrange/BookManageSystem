from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Book)
admin.site.register(models.Borrow)
admin.site.register(models.HotPic)
admin.site.register(models.UserImg)
