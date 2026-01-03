from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    options = (
        ('drafts', 'Drafts'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts" )
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    # bookauthor = models.CharField(max_length=250, unique=True)
    # status = models.IntegerField(choices=STATUS, default=0)
    # excerpt = models.TextField(blank=True)
    # updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title