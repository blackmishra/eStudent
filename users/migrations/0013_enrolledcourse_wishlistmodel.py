# Generated by Django 3.2.5 on 2021-07-11 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210711_0730'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.course')),
            ],
        ),
        migrations.CreateModel(
            name='EnrolledCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.course')),
            ],
        ),
    ]
