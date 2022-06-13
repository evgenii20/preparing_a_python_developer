from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from catalogapp.forms import ProductCreateForm, SectionForm
from catalogapp.models import ProductCatalog, Section


# Create your views here.

# class UserListView(ListView):
#     def get_context_data(self, *args,  **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context.update({
#             'user': {'name': 'Ivan', 'age': '31'}
#         })
#         return context


# class ProductCatalogListView(UserListView):
class ProductCatalogListView(ListView):
    """Вывод каталога на главной странице"""
    # model = ProductCatalog
    model = Section
    template_name = 'catalog.html'

    def get_queryset(self):
        queryset = ProductCatalog.objects.all()

        # object_list = ProductCatalog.objects.all()
        # # queryset = Section.objects.select_related(object_list).get()
        # queryset = Section.objects.prefetch_related(object_list).get()
        return queryset


# class ProductCatalogListView(ListView):
#     model = ProductCatalog
#     template_name = 'catalog.html'
#     # extra_context = {
#     #         'user': {'name': 'Ivan', 'age': '31'}
#     #     }
#
#     def get_queryset(self):
#         queryset = ProductCatalog.objects.all()
#         return queryset

# Перенёс в extra_context ^
# def get_context_data(self, *args,  **kwargs):
#     context = super().get_context_data(*args, **kwargs)
#     context.update({
#         'user': {'name': 'Ivan', 'age': '31'}
#     })
#     return context

# def get_page(request):
#     # user = {"name": "Ноутбук", "price": 1500}
#     # data = {"user": user}
#     return render(request, "catalog.html", context={
#         'object_list': ProductCatalog.objects.all(),
#         'user': {'name': 'Ivan', 'age': '31'}
#     })


class SectionListView(ListView):
    """Для вывода списка разделов и товаров"""
    model = Section
    template_name = 'part_list.html'
    form_class = SectionForm

    def get_queryset(self):
        # queryset = Section.objects.all()  # 6 запросов к БД

        # queryset = Section.objects.select_related('product_catalog').all()
        queryset = Section.objects.prefetch_related('product_catalog').all()
        # queryset = Section.objects.select_related('part_list').all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        title = 'Список разделов'
        context['title'] = title
        context.update({
            # 'user': {'name': 'Ivan', 'age': '31'}
        })
        return context


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


class PartKeyListView(ListView):
    """Класс для вывода списка категорий """
    model = Section
    # form_class = SectionForm
    # queryset = Section.objects.select_related('part_list').all()
    template_name = 'part.html'

    def get_queryset(self):
        sections = self.kwargs['pk']
        # queryset = Section.objects.filter(sections_id=sections).filter()
        queryset = Section.objects.filter(id=sections).prefetch_related('product_catalog')
        # queryset = Section.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        # вызов базовой реализации для получения контекста
        context = super().get_context_data(**kwargs)
        sections_id = self.kwargs['pk']
        title = 'Товары в категории'
        context['title'] = title
        context['object_list'] = Section.objects.filter(id=sections_id)
        # context['title'] = f'Раздел «{category.part}»'
        return context

# class ProductCatalogListView(ListView):
#     model = ProductCatalog
#     template_name = 'part.html'
#
#     def get_queryset(self):
#         queryset = ProductCatalog.objects.all()
#         return queryset
