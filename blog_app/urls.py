from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
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




)

from . import views






urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryListView.as_view(), name='category-detail'),
    path('categories/<int:category_id>/blogs/', BlogListView.as_view(), name='blog-list'),
    path('categories/<int:category_id>/blogs/<int:blog_id>/', BlogDetailView.as_view(), name='blog-detail'),
    path('categories/<int:category_id>/blogs/<int:blog_id>/images/', BlogImageView.as_view(), name='blog-image-list'),
    path('categories/<int:category_id>/blogs/<int:blog_id>/images/<int:image_id>/', BlogImageView.as_view(), name='blog-image-detail'),
    path('all/blogs/', Get_all_Blogs.as_view(), name='all-blogs'),





    #path('', home_view, name='home'),
    path('all-blogs/', all_blogs_view, name='all-blogs'),
    path('category/<int:category_id>/blogs/', category_blogs_view, name='category-blogs'),
    path('blog/<int:category_id>/<int:blog_id>/', blog_detail_view, name='blog-detail'),
    path('create-blog/', create_blog_view, name='create-blog'),
    path('edit-blog/<int:category_id>/<int:blog_id>/', edit_blog_view, name='edit-blog'),
    path('categories/', categories_view, name='categories'),



   

    path('', views.home, name='home'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),

]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





