from django.contrib import admin
from blog_app.models import Blog, Blog_category, Blog_Image

# Register your models here.
admin.site.register(Blog)
admin.site.register(Blog_category)
admin.site.register(Blog_Image)

