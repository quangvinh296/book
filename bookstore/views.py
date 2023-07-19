from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import TacGia, Sach
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# Create your views here.


def danh_sach(request):
    all_book = Sach.objects.select_related()
    paginator = Paginator(all_book, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "bookstore/index.html", {"page_obj": page_obj})


def search(request):
    if request.method == 'POST':
        tenSachRq = request.POST.get('ten')
        status = Sach.objects.filter(tenSach__icontains=tenSachRq)
        paginator = Paginator(status, 3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "bookstore/index.html", {"page_obj": page_obj})
    else:
        return render(request, "bookstore/index.html", {})
