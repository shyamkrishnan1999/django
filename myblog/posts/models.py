from django.db import models
from django.conf import settings

# Create your models here.
class TimeStampedModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True,editable=False)
    updated_at=models.DateTimeField(auto_now_add=True,editable=False)


class Category(TimeStampedModel):
    name=models.CharField(max_length=20)
    slug=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title=models.CharField(max_length=200)
    description=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="posts",on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    categories=models.ManyToManyField(Category,related_name="posts")
    image=models.FileField(upload_to='posts/',null=True,blank=True)

    def __str__(self):
        return self.title


