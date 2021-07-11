# Generated by Django 3.2.5 on 2021-07-11 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_delete_wishlistmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.course')),
            ],
        ),
    ]
