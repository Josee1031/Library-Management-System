# Generated by Django 5.1.3 on 2024-12-03 02:54

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo electrónico')),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Admin')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField(default=datetime.date(1001, 1, 1))),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('copies_available', models.IntegerField(default=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('author_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='library.author')),
                ('genre_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='library.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Book_Copies',
            fields=[
                ('copy_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_copy_num', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('book_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(default=datetime.date(2025, 1, 2))),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('copy_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='library.book_copies')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Waitlist',
            fields=[
                ('queue_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_placed', models.DateField(auto_now_add=True)),
                ('limit_date', models.DateField(blank=True, null=True)),
                ('book_lent', models.BooleanField(default=False)),
                ('next_in_line', models.BooleanField(default=False)),
                ('book_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
