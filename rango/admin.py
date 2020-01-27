from django.contrib import admin
from rango.models import Category, Page, UserProfile


admin.site.register(UserProfile)



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'views', 'likes', 'slug']


# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url', 'views']


admin.site.register(Page, PageAdmin)
