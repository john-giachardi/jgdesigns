# Generated by Django 4.1.5 on 2023-01-31 21:39

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogtagindexpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.RichTextField(),
        ),
        migrations.DeleteModel(
            name='BlogTagIndexPage',
        ),
    ]
