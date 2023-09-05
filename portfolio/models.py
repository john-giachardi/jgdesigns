from django.db import models
# Create your models here.
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index


class PortfolioIndexPage(Page):
    hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        portfoliopages = self.get_children().live().order_by('-first_published_at')
        context['portfoliopages'] = portfoliopages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('hero'),
        FieldPanel('intro')
    ]

class PortfolioPage(Page):
    date = models.DateField("Post date")
    hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='portfolio_page',
    )
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('hero'),
        FieldPanel('date'),
        FieldPanel('intro'),
        InlinePanel('gallery_images', label="Gallery images"),
        FieldPanel('body'),
    ]

class PortfolioPageGalleryImage(Orderable):
    page = ParentalKey(PortfolioPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        FieldPanel('image'),
    ]

