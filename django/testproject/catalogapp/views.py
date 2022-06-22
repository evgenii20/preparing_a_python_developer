from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from catalogapp.forms import ProductCreateForm
from catalogapp.models import ProductCatalog

# Create your views here.


class ProductCatalogListView(ListView):
    model = ProductCatalog
    template_name = 'catalog.html'

    def get_queryset(self):
        queryset = ProductCatalog.objects.all()
        return queryset


class ProductCatalogListView(ListView):
    model = ProductCatalog
    template_name = 'catalog.html'

    def get_queryset(self):
        queryset = ProductCatalog.objects.all()
        return queryset


# def index(request):
#     user = {"name": "Ноутбук", "price": 1500}
#     data = {"user": user}
#     return render(request, "catalog.html", context=data)

class ProductCreateView(CreateView):
    model = ProductCatalog
    template_name = 'updateCatalog.html'
    form_class = ProductCreateForm
    success_url = reverse_lazy('catalogapp:product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = 'Заполнение карточки товара'
        context['title'] = title
        return context

    # def get_context_data(self, **kwargs):
    #     # context = super(Index, self).get_context_data(**kwargs)
    #     data = {"name": "Ноутбук", "dates": "2022-05-30", "price": 1500, "unit": "шт", "name_supplier": "ООО Ноутбук опт"}
    #     context.update({
    #         'object_list': data
    #     })
    #     return context

