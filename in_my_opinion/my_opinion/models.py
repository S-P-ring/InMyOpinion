from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Вид насильства', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"
        managed = False

class Appeal(models.Model):
    appeal_id = models.IntegerField('ID', primary_key=True)
    date_of_creation = models.DateTimeField('Дата створення', auto_now_add=True)
    number_of_likes = models.IntegerField('Кількість лайків', null=True,)
    title = models.CharField('Заголовок', max_length=100)
    email = models.CharField('Email', max_length=100)
    history = models.TextField('Історія', )
    category = models.ManyToManyField(Category, verbose_name='Категорії', related_name='category')
    status = models.CharField('Статус', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "appeal"
        managed = False

