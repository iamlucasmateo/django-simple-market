from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect    

from items.models import Item, Category
from items.forms import ItemForm


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    category = item.category
    related_items = Item.objects.filter(category=category).exclude(pk=pk)[:4]

    return render(request, "items/detail.html", {
        "item": item,
        "related_items": related_items,
    })


def _create_item_from_form_and_save(request, item_form: ItemForm):
    category_id = item_form.cleaned_data["category"]
    category = Category.objects.get(pk=category_id)
    print("USER", request.user, category)
    item = Item.objects.create(
        name=item_form.cleaned_data["name"],
        description=item_form.cleaned_data["description"],
        price=item_form.cleaned_data["price"],
        image=request.FILES["image"],
        category=category,
        is_sold=True,
        created_by=request.user,
    )
    item.save()

    return redirect("items/detail.html", pk=item.pk)

@login_required
def create_item(request):
    if request.method == "POST":
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            try:
                _create_item_from_form_and_save(request, item_form)
            except Exception as exc:
                return render(request, "items/item_form.html", {"item_form": item_form})
        else:
            return render(request, "items/item_form.html", {"item_form": item_form})
    
    return render(request, "items/item_form.html", {"item_form": ItemForm()})


@login_required
def edit_item(request, item_id: int):
    item = get_object_or_404(Item, pk=item_id)
    print("USER", item.created_by, request.user)
    if item.created_by != request.user:
        return redirect(f"../../items/{item_id}", pk=item.pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
    else:
        form = ItemForm(instance=item)
    return render(request, "items/item_form.html", {"item_form": form})