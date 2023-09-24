# Generated by Django 4.2.5 on 2023-09-24 03:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books_catlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.UUIDField(default=uuid.uuid4)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
                ('genere', models.CharField(choices=[('LITERATURE', 'literature'), ('TRADITIONAL-LITERATURE', 'trafitional'), ('OTHER', 'other'), ('FICTION', 'fiction'), ('NON-FICTION', 'non-fictinonon')], max_length=255)),
                ('description', models.TextField()),
                ('book_image', models.ImageField(blank=True, null=True, upload_to='booksimg/')),
                ('avialable_free', models.BooleanField(default=True)),
                ('avialable_paid', models.BooleanField(default=False)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('additional', models.TextField(blank=True, null=True)),
            ],
        ),
    ]