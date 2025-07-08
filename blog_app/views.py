from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog, Blog_category, Blog_Image
from .serializers import BlogSerializer, BlogCategorySerializer, BlogImageSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.models import Q


# Create your views here.


'''
class CategoryListView(APIView):
    def get(self, request):
        categories = Blog_category.objects.all()
        serializer = BlogCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        try:
            category = Blog_category.objects.get(pk=pk)
        except Blog_category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND) 
        serializer = BlogCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk):
        try:
            category = Blog_category.objects.get(pk=pk)
        except Blog_category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class BlogListView(APIView):
    def get(self, request, category_id):
        try:
            category = Blog_category.objects.get(pk=category_id)
        except Blog_category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND) 
        blogs = category.blogs.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, category_id):
        try:
            category = Blog_category.objects.get(pk=category_id)
        except Blog_category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category=category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def put(self, request, category_id, blog_id):
        try:
            category = Blog_category.objects.get(pk=category_id)
        except Blog_category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            blog = category.blogs.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, category_id, blog_id):
        try:
            category = Blog_category.objects.get(pk=category_id)
        except Blog_category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            blog = category.blogs.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BlogDetailView(APIView):
    def get(self, request, category_id, blog_id):
        try:
            category = Blog_category.objects.get(pk=category_id)
        except Blog_category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            blog = category.blogs.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, category_id, blog_id):
        try:
            category = Blog_category.objects.get(pk=category_id)
        except Blog_category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            blog = category.blogs.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, category_id, blog_id):
        try:
            category = Blog_category.objects.get(pk=category_id)
        except Blog_category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            blog = category.blogs.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BlogImageView(APIView):
    def post(self, request, category_id, blog_id):
        try:
            category = Blog_category.objects.get(pk=category_id)
        except Blog_category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            blog = Blog.objects.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BlogImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(blog=blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, category_id, blog_id):
        try:
            category = Blog_category.objects.get(pk=category_id)
        except Blog_category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND) 
        try:
            blog = Blog.objects.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        images = blog.images.all()
        serializer = BlogImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, category_id, blog_id, image_id):
        try:
            category = Blog_category.objects.get(pk=category_id)
        except Blog_category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            blog = Blog.objects.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            image = blog.images.get(pk=image_id)
        except Blog_Image.DoesNotExist:
            return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BlogImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, category_id, blog_id, image_id):
        try:
            category = Blog_category.objects.get(pk=category_id)
        except Blog_category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            blog = Blog.objects.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            image = blog.images.get(pk=image_id)
        except Blog_Image.DoesNotExist:
            return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class Get_all_Blogs(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    




def home_view(request):
    return render(request, 'all_blogs.html')

def all_blogs_view(request):
    return render(request, 'all_blogs.html')

def category_blogs_view(request, category_id):
    return render(request, 'category_blogs.html', {'category_id': category_id})

def blog_detail_view(request, category_id, blog_id):
    return render(request, 'blog_detail.html', {
        'category_id': category_id,
        'blog_id': blog_id
    })

def create_blog_view(request):
    return render(request, 'blog_form.html')

def edit_blog_view(request, category_id, blog_id):
    return render(request, 'blog_form.html', {
        'category_id': category_id,
        'blog_id': blog_id
    })

def categories_view(request):
    return render(request, 'categories.html')





'''

from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Blog, Blog_category

def home(request):
    categories = Blog_category.objects.all().prefetch_related('blogs__images')
    recent_blogs = Blog.objects.order_by('-created_at')[:5]
    query = request.GET.get('q')

    if query:
        recent_blogs = Blog.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by('-created_at').distinct()
    else:
        recent_blogs = Blog.objects.order_by('-created_at')[:5]

    return render(request, 'home.html', {
        'categories': categories,
        'recent_blogs': recent_blogs
    })

# Blog detail view
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    # --- MODIFIED LOGIC FOR RELATED POSTS ---
    # Fetch all blog posts, exclude the current one, and limit
    related_posts = Blog.objects.exclude(
        slug=blog.slug          # Exclude the current post using its slug
    ).order_by(
        '-created_at'           # Order by most recent
    )[:3]                       # Limit to 3 other posts (adjust as needed)
    # --- END OF MODIFIED LOGIC ---

    context = {
        'blog': blog,
        'related_posts': related_posts,
    }
    return render(request, 'blog_detail.html', context)


def categories(request):
    categories = Blog_category.objects.all()
    return render(request, 'home.html', {'categories': categories})


def about_page(request):
    # Fetch, for example, the 5 most recent published blogs
    recent_blogs = Blog.objects.order_by('-created_at')[:3]
    categories = Blog_category.objects.all() # Fetch all categories

    context = {
        'recent_blogs': recent_blogs,
        'categories': categories,
    }
    return render(request, 'about.html', context)

def contact_page(request):
    return render(request, 'contact.html')