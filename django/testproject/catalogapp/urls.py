from django.urls import path
from catalogapp.views import ProductCatalogListView, ProductCreateView, SectionListView, PartKeyListView  # , get_page

app_name = 'catalogapp'

urlpatterns = [
    # path('', ProductCatalogListView.as_view(), name='product'),
    # path('', ProductCatalogListView.as_view(), name='main'),
    path('catalog-add/', ProductCreateView.as_view(), name='catalog_add'),
    # path('part/', SectionListView.as_view(), name='part'),
    path('', SectionListView.as_view(), name='product'),
    path('part/<str:pk>/', PartKeyListView.as_view(), name='part_key'),
    # path('get', get_page)


]