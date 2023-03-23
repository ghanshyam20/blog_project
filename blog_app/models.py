from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text=models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    published_at =models.DateTimeField(auto_now=True)
    author =models.ForeignKey("auth.User",on_delete=models.CASCADE)
    def __str__(self):
        return self.title
        #one author can post multiple blog
        # one blog is associated to only one author
        
