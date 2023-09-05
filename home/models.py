from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import FieldPanel
from blog.models import BlogPage


class HomePage(Page):
    body = RichTextField(blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def blogs(self):
        blogs = BlogPage.objects.filter(tags__name='home')
        blogs = blogs.order_by('-date')
        return blogs

    content_panels = Page.content_panels + [
        InlinePanel('hero_images', label="Hero images"),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context

class AboutPage(Page):
    hero = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+',
    )
    about = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+',
    )
    intro = models.CharField(max_length=1000)
    body = RichTextField()

    content_panels = Page.content_panels + [
    FieldPanel('hero'),
    FieldPanel('about'),
    FieldPanel('intro', classname='full'),
    FieldPanel('body', classname='full'),
    ]

class ProcessPage(Page):
    hero = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+',
    )
    intro = models.CharField(max_length=1000)


    content_panels = Page.content_panels + [
    FieldPanel('hero'),
    FieldPanel('intro', classname='full'),
    InlinePanel('phase_images', label="Phase images"),
    ]

class ProcessPagePhaseImage(Orderable):
    page = ParentalKey(ProcessPage, on_delete=models.CASCADE, related_name='phase_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    phase = models.TextField(blank=True, max_length=250)
    title = models.TextField(blank=True, max_length=250)
    caption = models.CharField(blank=True, max_length=1000)

    panels = [
        FieldPanel('image'),
        FieldPanel('phase'),
        FieldPanel('title'),
        FieldPanel('caption'),
    ]

class HomePageHeroImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='hero_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

class HomePageGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    title = models.TextField(blank=True, max_length=250)
    caption = models.CharField(blank=True, max_length=500)
    link = models.TextField(blank=True, max_length=100)

    panels = [
        FieldPanel('image'),
        FieldPanel('title'),
        FieldPanel('caption'),
        FieldPanel('link'),
    ]

class ContactPage(Page):    
    intro = RichTextField()
    body = RichTextField()
    contact1 = models.TextField(blank=True, max_length=100)
    contact2 = models.TextField(blank=True, max_length=100)

    content_panels = Page.content_panels + [
    InlinePanel('contact_images', label="Contact images"),
    FieldPanel('intro', classname='full'),
    FieldPanel('body', classname='full'),
    FieldPanel('contact1'),
    FieldPanel('contact2'),
    ]

class ContactPageImage(Orderable):
    page = ParentalKey(ContactPage, on_delete=models.CASCADE, related_name='contact_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    title = models.TextField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('title'),
    ]

class InformationPage(Page):   
    hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    ) 
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('hero', classname='full'),
        FieldPanel('body', classname='full'),
    ]

