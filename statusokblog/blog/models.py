from django.db import models


def upload_image_post (instance, filename):
    return 'post_{}/{}'.format(instance.pk, filename)


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

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=80)
    email = models.EmailField()
    comment_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user_name, self.post)

