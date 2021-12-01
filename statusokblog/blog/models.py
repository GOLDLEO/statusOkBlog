from django.db import models

class Tag(models.Model):
    name = models.CharField("Название тега", max_length=120)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField("Название статьи", max_length=255)
    content = models.TextField("Текст статьи")
    meta_keywords = models.CharField("Ключевые слова", max_length=255)
    meta_description = models.CharField("Краткое описание", max_length=255)
    date_create = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активно", default=False)
    count_view = models.PositiveIntegerField("Просмотры", default=0)
    tag_name = models.ManyToManyField(Tag)

