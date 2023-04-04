from django import forms

from items.models import Item, Category


INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class ItemForm(forms.ModelForm):    
    class Meta:
        model = Item
        fields = ("name", "description", "price", "image")
        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "Name"}),
            "category": forms.Select(attrs={"class": INPUT_CLASSES, "placeholder": "Category"}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES, "placeholder": "Description"}),
            "price": forms.NumberInput(attrs={"class": INPUT_CLASSES, "placeholder": "Price"}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES, "placeholder": "Image"}),
        }
    
    category = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        choices = [(cat.pk, cat.name) for cat in categories]
        self.fields["category"].choices = choices
    
class ItemPatchForm(forms.ModelForm):    
    class Meta:
        model = Item
        fields = ("name", "description", "price")
        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "Name"}),
            "category": forms.Select(attrs={"class": INPUT_CLASSES, "placeholder": "Category"}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES, "placeholder": "Description"}),
            "price": forms.NumberInput(attrs={"class": INPUT_CLASSES, "placeholder": "Price"}),
        }
    
    category = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        choices = [(cat.pk, cat.name) for cat in categories]
        self.fields["category"].choices = choices
