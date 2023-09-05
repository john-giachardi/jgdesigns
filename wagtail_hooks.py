from django.contrib import admin
from wagtail.admin import edit_handlers
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel

from collection.models import ImageCollection

class ImageCollectionAdmin(admin.ModelAdmin):
    model = ImageCollection
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description'),
    ]

admin.site.register(ImageCollection, ImageCollectionAdmin)