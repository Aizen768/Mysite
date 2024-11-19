


from django.db import models





class News(models.Model):
    image = models.ImageField(null=True, blank=True, verbose_name= 'Изображение')
    title = models.CharField(null=True, blank=True, max_length=100, verbose_name= 'Название')
    discription = models.TextField(null=True, blank=True, verbose_name= 'Описание')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
          











