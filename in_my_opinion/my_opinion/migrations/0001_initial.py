# Generated by Django 3.2.4 on 2021-07-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Вид насильства')),
            ],
            options={
                'verbose_name': 'Категорії',
                'verbose_name_plural': 'Категорії',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('number_of_likes', models.IntegerField(null=True, verbose_name='Кількість лайків')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('history', models.TextField(verbose_name='Історія')),
                ('status', models.CharField(choices=[('n', 'Не опубліковано'), ('o', 'Опубліковано')], default='Не опубліковано', max_length=1, verbose_name='Статус')),
                ('category', models.ManyToManyField(related_name='category', to='my_opinion.Category', verbose_name='Категорії')),
            ],
            options={
                'verbose_name': 'Звернення',
                'verbose_name_plural': 'Звернення',
                'db_table': 'appeal',
                'ordering': ['date_of_creation'],
            },
        ),
    ]
