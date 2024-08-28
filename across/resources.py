from import_export import resources
from .models import VideoAlbum, PhotoAlbum, HomePageBanner, BlogPost, Contact, TourPackage, Booking, Tag, Photo, Video, Category

class VideoAlbumResource(resources.ModelResource):
    class Meta:
        model = VideoAlbum

class PhotoAlbumResource(resources.ModelResource):
    class Meta:
        model = PhotoAlbum

class HomePageBannerResource(resources.ModelResource):
    class Meta:
        model = HomePageBanner

class BlogPostResource(resources.ModelResource):
    class Meta:
        model = BlogPost

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact

class TourPackageResource(resources.ModelResource):
    class Meta:
        model = TourPackage

class BookingResource(resources.ModelResource):
    class Meta:
        model = Booking

class TagResource(resources.ModelResource):
    class Meta:
        model = Tag

class PhotoResource(resources.ModelResource):
    class Meta:
        model = Photo

class VideoResource(resources.ModelResource):
    class Meta:
        model = Video

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
