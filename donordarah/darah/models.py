from django.db import models

class Pasien(models.Model):
    no_pasien = models.CharField(max_length =10, null=True,blank=False)
    nama_pasien = models.CharField(max_length=240, null=True,blank=False)
    golongan_darah = models.CharField(max_length=2, null=True,blank=False)
    jenis_kelamin = models.CharField(max_length=6, null=True,blank=False)
    tanggal_lahir = models.DateField(null=True,blank=False)
    alamat_pasien = models.CharField(max_length=100, null=True,blank=False)
    no_hp = models.IntegerField(null=True,blank=False)

    def __str__(self):
        return self.nama_pasien