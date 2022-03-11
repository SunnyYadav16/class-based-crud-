from django.contrib import admin
from .models import UserData

# Register your models here.
@admin.register(UserData)
class UderDataAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')