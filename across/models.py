import os
import uuid
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join(instance.__class__.__name__.lower(), filename)

class SEOModel(models.Model):
    meta_title = models.CharField(max_length=150, blank=True)
    meta_description = models.TextField(blank=True)
    og_title = models.CharField(max_length=150, blank=True)
    og_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.meta_title)
        super().save(*args, **kwargs)

class VideoAlbum(SEOModel):
    title = models.CharField(max_length=200)
    description = RichTextField()
    videos = models.ManyToManyField('Video', related_name='video_albums')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='videos', null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='video_albums')

    def __str__(self):
        return self.title

class PhotoAlbum(SEOModel):
    title = models.CharField(max_length=200)
    description = RichTextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='photos', null=True, blank=True)
    images = models.ManyToManyField('Photo', related_name='photo_albums')
    tags = models.ManyToManyField('Tag', related_name='photo_albums')

    def __str__(self):
        return self.title

class HomePageBanner(SEOModel):
    image = models.ForeignKey('Photo', related_name='photo_banner', on_delete=models.CASCADE)
    text = RichTextField(blank=True)

    def __str__(self):
        return self.meta_title or "Home Page Banner"

class BlogPost(SEOModel):
    title = models.CharField(max_length=200)
    content = RichTextField()  # Using CKEditor for content field
    featured_image = models.ImageField(upload_to=upload_to)
    tags = models.ManyToManyField('Tag', related_name='blog_posts')

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = RichTextField()

    def __str__(self):
        return self.name

class TourPackage(SEOModel):
    title = models.CharField(max_length=200)
    description = RichTextField()  # Using CKEditor for description field
    duration = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to=upload_to)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='packages')
    photo_gallery = models.ForeignKey('PhotoAlbum', on_delete=models.SET_NULL, null=True, blank=True)
    video_gallery = models.ForeignKey('VideoAlbum', on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='tour_packages')

    def __str__(self):
        return self.title

class Booking(models.Model):
    package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return f"Booking for {self.package.title} by {self.full_name}"

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    image = models.ImageField(upload_to=upload_to)
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.alt_text

class Video(models.Model):
    video = models.FileField(upload_to=upload_to)
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.alt_text

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name