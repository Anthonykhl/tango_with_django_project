from django.contrib import admin
from rango.models import Category, Page

class adminCategory(admin.ModelAdmin):
    list_display=('name','views','likes')

class adminPage(admin.ModelAdmin):
    list_display=('category','title','url')



admin.site.register(Category,adminCategory)
admin.site.register(Page, adminPage)
