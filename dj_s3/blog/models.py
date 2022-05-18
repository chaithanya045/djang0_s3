from distutils.command import upload
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    image=models.ImageField(upload_to='Blog_images/')

    def __str__(self):
        return self.title
    def delete(request, id):
        post = Post.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('posts.views.all_posts'))


    