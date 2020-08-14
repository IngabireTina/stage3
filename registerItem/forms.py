from django.forms import ModelForm
from .models import Item
from .models import Stock


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['device'].queryset = Stock.objects.exclude(item__counting='Available')
