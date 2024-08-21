from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import TourPackage, PhotoAlbum, BlogPost, HomePageBanner
from .forms import ContactForm, BookingForm, BlogPostForm, TourPackageForm

def homepage_view(request):
    packages = TourPackage.objects.all()
    albums = PhotoAlbum.objects.all()
    blog_posts = BlogPost.objects.all()
    homepage_images = HomePageBanner.objects.all()  # Fetch all homepage images

    return render(request, 'across/homepage.html', {
        'packages': packages,
        'albums': albums,
        'blog_posts': blog_posts,
        'homepage_images': homepage_images,  # Pass all images to the template
    })

def blog_post_create_view(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_post_list')
    else:
        form = BlogPostForm()
    return render(request, 'across/blog_post_form.html', {'form': form})

def tour_package_create_view(request):
    if request.method == 'POST':
        form = TourPackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tour_package_list')
    else:
        form = TourPackageForm()
    return render(request, 'across/tour_package_form.html', {'form': form})

def blog_post_list_view(request):
    posts = BlogPost.objects.all()
    return render(request, 'across/blog_post_list.html', {'posts': posts})

def tour_package_list_view(request):
    packages = TourPackage.objects.all()
    return render(request, 'across/tour_package_list.html', {'packages': packages})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'across/contact.html', {'form': form})

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking request has been submitted.')
            return redirect('booking')
    else:
        form = BookingForm()

    return render(request, 'across/booking.html', {'form': form})

def blog_post_detail_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'across/blog_post_detail.html', {'post': post})

def tour_package_detail_view(request, slug):
    package = get_object_or_404(TourPackage, slug=slug)
    return render(request, 'across/tour_package_detail.html', {'package': package})
