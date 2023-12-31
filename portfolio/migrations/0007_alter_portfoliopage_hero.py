# Generated by Django 4.1.5 on 2023-02-03 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('portfolio', '0006_portfoliopagegalleryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliopage',
            name='hero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='portfolio_page', to='wagtailimages.image'),
        ),
    ]
