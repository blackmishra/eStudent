# Generated by Django 3.2.5 on 2021-07-11 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_wishlistmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistmodel',
            name='course_name',
        ),
        migrations.DeleteModel(
            name='EnrolledCourse',
        ),
        migrations.DeleteModel(
            name='WishlistModel',
        ),
    ]
