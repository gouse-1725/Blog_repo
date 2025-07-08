from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
'''
from .views import (
    CategoryListView,
    BlogListView,
    BlogDetailView,
    BlogImageView,
    Get_all_Blogs,
    home_view,
    all_blogs_view,
    category_blogs_view,
    blog_detail_view,
    create_blog_view,
    edit_blog_view,
    categories_view,




)'''

from . import views







    

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),

]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





