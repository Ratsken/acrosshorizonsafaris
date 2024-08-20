from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Contact, Booking, BlogPost, TourPackage

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['package', 'full_name', 'email', 'date']

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'featured_image', 'tags']

class TourPackageForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = TourPackage
        fields = ['title', 'description', 'duration', 'price', 'cover_image', 'category', 'photo_gallery', 'video_gallery', 'tags']
