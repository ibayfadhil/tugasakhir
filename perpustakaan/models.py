from django.db import models
# Create your models here.

class Kelompok(models.Model):
  nama       = models.CharField(max_length=9)
  keterangan = models.TextField()

  def __str__(self):
    return self.nama

class Buku(models.Model):
  judul       = models.CharField(max_length=50)
  penulis     = models.CharField(max_length=40)
  penerbit    = models.CharField(max_length=40)
  #jumlah      = models.IntegerField(null=True)
  dokumen     = models.FileField(upload_to='docs/')
  key_enkripsi = models.FileField(upload_to='key/')
  tanggal     = models.DateTimeField(auto_now_add=True, null=True)
  encpath = models.CharField(max_length=100,null=True)

  def __str__(self):
    return self.judul