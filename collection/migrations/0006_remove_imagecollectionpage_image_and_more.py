# Generated by Django 4.1.5 on 2023-02-04 18:49

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_remove_imagecollectionpage_image_collection_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagecollectionpage',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='collection_page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='collection.imagecollectionpage'),
        ),
        migrations.AddField(
            model_name='imagecollectionpage',
            name='body',
            field=wagtail.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, use_json_field=None),
        ),
    ]