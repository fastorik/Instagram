from django.db import models
from instagram import settings
from django.core.validators import FileExtensionValidator
class Post(models.Model):
    postContent = models.CharField(max_length=500)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=('post_author'), related_name="post_author",
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='posts/images', default='posts/images/lake.jpg')
    video = models.FileField(
        upload_to='posts/videos', blank=True, validators=[FileExtensionValidator(allowed_extensions=['mp4','webm'])])
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, related_name='post_like',  blank=True)
    save =  models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, related_name='post_save',  blank=True)

    def __str__(self) -> str:
        return f'{self.postContent}'

    @property
    def total_likes(self):
        return self.likes.count()
