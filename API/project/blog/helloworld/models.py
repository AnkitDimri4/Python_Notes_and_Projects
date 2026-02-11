from django.db import models
from django.contrib.auth.models import User 
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here
class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
# class Portfolio(models.Model):

#     # class Meta:
#     #     verbose_name_plural = 'Portfolio Profiles'
#     #     verbose_name = 'Portfolio'
#     #     ordering = ["name"]
#     date = models.DateTimeField(blank=True, null=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     description = models.CharField(max_length=500, blank=True, null=True)
#     body = RichTextField(blank=True, null=True)
#     image = models.ImageField(blank=True, null=True, upload_to="portfolio")
#     slug = models.SlugField(null=True, blank=True)
#     is_active = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.slug = slugify(self.name)
#         super(Portfolio, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return f"/portfolio/{self.slug}"