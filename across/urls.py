from django.urls import path
from .views import (
    homepage_view,
    blog_post_create_view, blog_post_list_view, blog_post_detail_view,
    tour_package_create_view, tour_package_list_view, tour_package_detail_view,
    contact_view, booking_view
)

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('blogs/', blog_post_list_view, name='blog_post_list'),
    path('blogs/create/', blog_post_create_view, name='blog_post_create'),
    path('blogs/<slug:slug>/', blog_post_detail_view, name='blog_post_detail'),
    path('tours/', tour_package_list_view, name='tour_package_list'),
    path('tours/create/', tour_package_create_view, name='tour_package_create'),
    path('tours/<slug:slug>/', tour_package_detail_view, name='tour_package_detail'),
    path('contact/', contact_view, name='contact'),
    path('booking/', booking_view, name='booking'),
]
