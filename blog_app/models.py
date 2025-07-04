from django.db import models
from django.utils.text import slugify

# Create your models here.


class Blog_category(models.Model):
    name = models.CharField(max_length=100, unique=True, default=False)

    def __str__(self):
        return f"name of the category is : {self.name}"
    

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True, default=False)
    content = models.TextField()
    category = models.ForeignKey(Blog_category, on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"title of the blog is : {self.title}"
    
class Blog_Image(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images')
    image = models.URLField(max_length=1000, default=False)

    def __str__(self):
        return f"Image for blog: {self.blog.title}"
