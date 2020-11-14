from django.shortcuts import render

# Create your views here.


def index(request):
    items = Item.objects.order_by("-publish_date")
    now = datetime.datetime.now()
    return render(request, 'portfolio/index.html', {"items": items, "year": now.year})
