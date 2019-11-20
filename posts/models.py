from django.db import models
from tinymce import HTMLField
from django.contrib.auth import get_user_model
from django.db.models.signals import  pre_save
from django.urls import reverse
from blog.util import unique_slug_generator


User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
     title = models.CharField(max_length=20)

     def __str__(self):
         return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null = True, blank=True)
    overview = models.TextField()
    content = HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default = 0)
    view_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    top10 = models.BooleanField()
    prev_post = models.ForeignKey('self', related_name='previous_post', on_delete=models.SET_NULL, blank=True, null=True)
    nex_post = models.ForeignKey('self', related_name='next_post', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'slug': self.slug,
            'id': self.id
        })

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def get_comments(self):
        return self.comments.order_by('-timestamp')

def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender = Post)
       
class Comment(models.Model):
    user = models.CharField(max_length=75)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user
