from django import forms

from catalogapp.models import ProductCatalog, Section


class ProductCreateForm(forms.ModelForm):
    """Чтение и изменение объекта каталога"""

    class Meta:
        model = ProductCatalog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Название товара'
        self.fields['name'].widget.attrs['type'] = 'text'
        self.fields['name'].widget.attrs['name'] = 'name'
        self.fields['dates'].widget.attrs['name'] = 'dates'
        self.fields['dates'].widget = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})
        self.fields['price'].widget.attrs['name'] = 'price'
        self.fields['price'].widget.attrs['placeholder'] = 'Цена товара'
        self.fields['unit'].widget.attrs['name'] = 'unit'
        self.fields['unit'].widget.attrs['placeholder'] = 'шт'
        self.fields['name_supplier'].widget.attrs['name'] = 'name_supplier'
        self.fields['name_supplier'].widget.attrs['placeholder'] = 'Название поставщика'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['class'] = 'inputFild'


class SectionForm(forms.ModelForm):
    """Чтение и изменение объекта каталога"""

    class Meta:
        model = Section
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(SectionForm, self).__init__(*args, **kwargs)
    #
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'
