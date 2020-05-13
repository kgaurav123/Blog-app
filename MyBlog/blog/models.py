from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.CharField(max_length=130)
    timestamp = models.DateTimeField(blank=True)
  

    def __str__(self):
        return self.title