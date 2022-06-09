from django.contrib import admin

# Register your models here.
# python manage.py makemigrations
# python manage.py migrate

from .models import User,Mycar,CarData

admin.site.register(User)
admin.site.register(Mycar)
admin.site.register(CarData)