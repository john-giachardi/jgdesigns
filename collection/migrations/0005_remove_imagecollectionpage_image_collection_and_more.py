# Generated by Django 4.1.5 on 2023-02-04 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('collection', '0004_imagecollectionpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagecollectionpage',
            name='image_collection',
        ),
        migrations.AddField(
            model_name='imagecollectionpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]