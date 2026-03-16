from django.db import models

class Blog(models.Model):
    heading = models.CharField(
        max_length=150,
        verbose_name="Заголовок",
        unique=True,
        help_text="Заголовок поста блога",
    )
    content = models.TextField(
        blank=True,
        verbose_name="Текст блога",
        help_text="Текст поста блога",
    )
    photo_blog = models.ImageField(
        blank=True,
        upload_to="photo/",
        verbose_name="Фотография блога",
        help_text="Фотография блога",
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания поста",
        help_text="Дата создания поста",
    )
    ispublication = models.BooleanField(
        verbose_name="Опубликовано",
        help_text="Опубликовано",
        default=False,
    )
    number_views = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Количество просмотров"
    )


    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["heading"]
