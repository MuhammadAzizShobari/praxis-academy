from django.db import models
class profil(models.Model):

    nama = models.CharField(max_length=30)
    alamat = models.CharField(max_length=100)
    nomor_kamar = models.IntegerField()
    tgl_bayar = models.CharField(max_length=20)

    def __str__(self):
        return self.nama