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
    
    conclusion = models.TextField(default=False)
    core_concepts = models.TextField(default=False)
    partial_applications = models.TextField(default=False)
    


    def save(self, *args, **kwargs):
        # Generate slug only if it's not already set (e.g., for new objects)
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            num = 1
            # Check for uniqueness and append a number if necessary
            while Blog.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs) # Call the "real" save method


    def __str__(self):
        return f"title of the blog is : {self.title}"
    
class Blog_Image(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images')
    image = models.URLField(max_length=1000, default=False)

    def __str__(self):
        return f"Image for blog: {self.blog.title}"
