from django.contrib import admin
from .models import TacGia, Sach
# Register your models here.


@admin.register(TacGia)
class TacGiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenTacGia')

# Register your models here.


@admin.register(Sach)
class SachAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenSach', 'gia', 'tacGia')
