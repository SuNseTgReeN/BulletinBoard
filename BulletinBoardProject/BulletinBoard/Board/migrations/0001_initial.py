# Generated by Django 4.1.7 on 2023-03-12 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date creation')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('rating', models.SmallIntegerField(default=0, verbose_name='Rating')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo')),
                ('notification_category', models.ManyToManyField(to='Board.category', verbose_name='Notification category')),
                ('notification_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='The user who wants to become the author of the notification')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Response text')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date the response was created')),
                ('responses_advertising', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Board.notification', verbose_name='Response')),
                ('responses_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Response',
                'verbose_name_plural': 'Responses',
            },
        ),
    ]
