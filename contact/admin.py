from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contact)

@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display=('created','email',)
    