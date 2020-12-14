Judul:NoSQL dan NewSQL 
Oleh:Muhammad Aziz Shobari
Tanggal : 16-03-2020
Ringkasan materi:
NoSQL bukan merupakan bahasa. NoSQL adalah sebuah mekanisme untuk menyimpan data dan mengambil data yang dilakukan oleh database kita. NoQSL tidak membutuhkan data model relational dan bahasa SQL untuk melakukan hal tersebut. NoSQL menggunakan metadata pada database kita dan memanfaatkan index dari data tersebut.
DBMS NoSQL Sebuah NoSQL awalnya mengacu pada non SQL atau non relasional adalah database yang menyediakan mekanisme untuk penyimpanan dan pengambilan data. Data ini dimodelkan dalam cara selain hubungan tabular yang digunakan dalam database relasional.
MongoDB adalah salah satu jenis database NoSQL yang berbasis dokumen dengan fomat JSON.Pada database SQL, data disimpan dalam bentuk tabel. Sedangkan pada MongoDB data disimpan dalam bentuk dokumen dengan format JSON.

Penjelasan tentang isi repo:
Hari ini kita menginstall MongoDB
Menginstal dan Menjalankan MongoDB pada Mesin Windows
Unduh file pemasang MongoDB dari bagian unduhan situs web MongoDB.

Temukan file .msi dowloaded di Windows Explorer. Klik dua kali file tersebut dan ikuti petunjuk untuk menginstal Mongo. Catatan: kecuali Anda menentukan direktori khusus, Mongo kemungkinan besar akan dipasang di C:\mongodbdirektori **. Namun, berdasarkan pengaturan pada mesin Anda, Mongo dapat diinstal di tempat lain. Sebagai contoh C:\Program Files\MongoDB\Server\3.2,. Selain itu, Anda dapat menemukan MongoDB di menu tambah / hapus program.

Buat direktori tempat MongoDB akan menyimpan file-file itu. Dari command prompt, jalankan md \data\db. Ini adalah lokasi default. Namun, lokasi lain dapat ditentukan menggunakan --dbpathparameter. Lihat dokumen Mongo untuk informasi lebih lanjut.

Mulai daemon mongodb dengan menjalankan C:\mongodb\bin\mongod.exedi Command Prompt. Atau dengan berlari,C:\path\to\mongodb\bin\mongod.exe

Terhubung ke MongoDB menggunakan shell Mongo Sementara daemon MongoDB sedang berjalan, dari jendela Command prompt yang berbeda jalankanC:\mongodb\bin\mongo.exe

Install CockroachDB 
Biner CockroachDB untuk Linux membutuhkan glibc,, libncursesdan tzdata, yang ditemukan secara default di hampir semua distribusi Linux, dengan Alpine sebagai pengecualian.

Unduh arsip CockroachDB untuk Linux, dan ekstrak binernya:

SALINAN 
wget -qO- https://binaries.cockroachdb.com/cockroach-v19.2.4.linux-amd64.tgz | tar  xvz
Salin biner ke Anda PATHsehingga mudah untuk mengeksekusi perintah kecoa dari shell apa pun:

SALINAN 
cp -i cockroach-v19.2.4.linux-amd64/cockroach /usr/local/bin/
Jika Anda mendapatkan kesalahan izin, awali perintah dengan sudo.

terdapatg problem dalam mongo shell manual yaitu perintah nya saya menjalankan di windows itu tidak bisa