from django.urls import path
from catalogapp.views import ProductCatalogListView, ProductCreateView

app_name = 'catalogapp'

urlpatterns = [
    path('', ProductCatalogListView.as_view(), name='product'),
    # path('', ProductCatalogListView.as_view(), name='main'),
    # path('catalog-add/', ProductCreateView.as_view(), name='catalog_add')
    path('catalog-add/', ProductCreateView.as_view(), name='catalog_add')

]