from django.db import models

# Create your models here.

class TacGia(models.Model):
    id = models.AutoField(primary_key=True)
    tenTacGia = models.CharField(max_length=250, db_index=True)
    def __str__(self) -> str:
        return self.tenTacGia

class Sach(models.Model):
    id = models.AutoField(primary_key=True)
    tenSach = models.CharField(max_length=250, db_index=True)
    gia = models.IntegerField()
    tacGia = models.ForeignKey(TacGia, related_name='book', on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return self.tenSach



