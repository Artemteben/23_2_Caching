from django.urls import path, include
from django.views.decorators.cache import cache_page
from django.views.generic import ListView

from catalog.apps import CatalogConfig
from catalog.views import (
    contacts,
    home,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/create/", BlogCreateView.as_view(), name="blog_create"),
    path(
        "blog/<int:pk>/<slug:slug>/update/",
        BlogUpdateView.as_view(),
        name="blog_update",
    ),
    path(
        "blog/<int:pk>/<slug:slug>/delete/",
        BlogDeleteView.as_view(),
        name="blog_delete",
    ),
]

# path("", home, name="home"),
# path("contacts/", contacts, name="contacts"),
