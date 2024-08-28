from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import (
    BlogPost, Contact, TourPackage, Booking, Tag, Photo, Video,
    PhotoAlbum, VideoAlbum, Category, HomePageBanner
)
from ckeditor.widgets import CKEditorWidget
from django import forms
from .resources import (
    BlogPostResource, ContactResource, TourPackageResource, BookingResource, 
    TagResource, PhotoResource, VideoResource, PhotoAlbumResource, 
    VideoAlbumResource, CategoryResource, HomePageBannerResource
)

# Custom Admin Form for CKEditor integration
class BlogPostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }

class TourPackageAdminForm(forms.ModelForm):
    class Meta:
        model = TourPackage
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }

class HomePageBannerAdminForm(forms.ModelForm):
    class Meta:
        model = HomePageBanner
        fields = '__all__'
        widgets = {
            'text': CKEditorWidget(),
        }

# Inline admin classes for related models (adjusted to match your models)
class BookingInline(admin.StackedInline):
    model = Booking
    extra = 1

# Admin classes with ImportExportModelAdmin
class BlogPostAdmin(ImportExportModelAdmin):
    form = BlogPostAdminForm
    resource_class = BlogPostResource
    list_display = ('title', 'meta_title', 'meta_description', 'slug')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

class ContactAdmin(ImportExportModelAdmin):
    resource_class = ContactResource
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')

class TourPackageAdmin(ImportExportModelAdmin):
    form = TourPackageAdminForm
    resource_class = TourPackageResource
    list_display = ('title', 'price', 'category', 'duration')
    list_filter = ('category', 'tags')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

class BookingAdmin(ImportExportModelAdmin):
    resource_class = BookingResource
    list_display = ('package', 'full_name', 'email', 'date')
    list_filter = ('date', 'package')
    search_fields = ('full_name', 'email')

class TagAdmin(ImportExportModelAdmin):
    resource_class = TagResource
    list_display = ('name',)
    search_fields = ('name',)

class PhotoAdmin(ImportExportModelAdmin):
    resource_class = PhotoResource
    list_display = ('alt_text', 'image')
    search_fields = ('alt_text',)

class VideoAdmin(ImportExportModelAdmin):
    resource_class = VideoResource
    list_display = ('alt_text', 'video')
    search_fields = ('alt_text',)

class PhotoAlbumAdmin(ImportExportModelAdmin):
    resource_class = PhotoAlbumResource
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

class VideoAlbumAdmin(ImportExportModelAdmin):
    resource_class = VideoAlbumResource
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ('name', 'slug')
    search_fields = ('name',)

class HomePageBannerAdmin(ImportExportModelAdmin):
    form = HomePageBannerAdminForm
    resource_class = HomePageBannerResource
    list_display = ('meta_title',)
    search_fields = ('meta_title', 'text')

# Register models with admin site
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(TourPackage, TourPackageAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(PhotoAlbum, PhotoAlbumAdmin)
admin.site.register(VideoAlbum, VideoAlbumAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(HomePageBanner, HomePageBannerAdmin)
