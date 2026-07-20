from django.db import models
from django.contrib.auth.models import User
from PIL import Image as p_img


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    
    
class Image(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = p_img.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (100,100)
            img.thumbnail(output_size)
            img.save(self.image.path)

