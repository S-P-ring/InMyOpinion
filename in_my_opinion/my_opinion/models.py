from django.db import models

"""STATUS_CHOICES for Appeal.status"""
STATUS_CHOICES = [
    ('n', 'Не опубліковано'),
    ('o', 'Опубліковано'),
]


class Category(models.Model):
    name = models.CharField('Вид насильства', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        verbose_name = "Категорії"
        verbose_name_plural = "Категорії"


class Appeal(models.Model):
    id = models.CharField('ID', primary_key=True, max_length=50)
    date_of_creation = models.DateTimeField('Дата створення', auto_now_add=True)
    number_of_likes = models.IntegerField('Кількість лайків', null=True,)
    title = models.CharField('Заголовок', max_length=50)
    email = models.EmailField('Email', )
    history = models.TextField('Історія', )
    category = models.ManyToManyField(Category, verbose_name='Категорії', related_name='category')
    status = models.CharField('Статус', max_length=1, choices=STATUS_CHOICES, default='Не опубліковано')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date_of_creation"]
        db_table = "appeal"
        verbose_name = "Звернення"
        verbose_name_plural = "Звернення"

