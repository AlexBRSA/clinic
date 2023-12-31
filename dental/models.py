from django.db import models
from django.urls import reverse

# Create your models here.
class Dental(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    
    
    
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/%Y/%m/%d/', verbose_name="Галерея фото")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return str(self.image)
