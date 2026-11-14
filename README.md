# 25-564933-BI-11824_Luqman-Yanuarta_MagangGMRT
Tugas Day 2 Pembekalan Programmer GMRT

1.Profil

Nama : Luqman Yanuarta
NIM : 25/564933/BI/11824

2. Dekskripsi
   
  Program ini merupakan hasil forward kinematics yang dijadikan bahasa python, pada program ini yang dihitung adalah posisi koordinat akhir pada ujung kaki robot berdasarkan sudut putaran 2 servo robot. Program ini bekerja dengan menerima input panjang femur berdasarkan 2 angka terakhir dari NIU, panjang tibia yang berdasarkan 2 angka terakhir NIF, serta sudut dalam derajat yang di konversi satuan radian nya menggunakan numpy, setelah diubah maka dihitung posisi bagian bagian kaki menggunakan persamaan trigonometri sehingga didapatkan koordinat akhirnya.

4. Daftar Fitur

a. Program Python interaktif (menggunakan input()) untuk mencari koordinat titik akhir (end-effector) ✅

b. Uji dengan memasukkan input rotasi Servo 1 = 40° dan Servo 2 = 30° dan lampirin output hasil test case ✅

c. Mathematical Proof: Menyertakan foto/scan coretan tangan perhitungan matematis rumus FK/IK ✅

d. N-DoF: Menambahkan Degree of Freedom pada sistem (>2 DoF, misalnya panjang Coxa tidak lagi 0). ❌

e. Spatial Kinematics: Membuat sistem dalam tiga dimensi (X, Y, Z). ❌

f. Homogeneous Transformation: Mengaplikasikan library matriks (misal: NumPy) untuk perhitungan Homogeneous Transform Matrix.❌

g. Visualisasi GUI/Plot: Menampilkan postur robot menggunakan matplotlib (dalam bentuk window pop-up atau menyimpan gambar png/jpg).❌

h. Inverse Kinematics (IK): Menambahkan opsi kalkulasi IK (mencari sudut jika diketahui target X, Y).❌

4. Cara Penggunaan
   
   1. Install Library NumPy
- buka terminal
- ketik "pip install numpy"
  
   2. Jalankan Program
- Tugas_Day_2.py di run
  
   3. Masukan Angka yang diinginkan
- Masukkan panjang femur sesuai 2 angka terakhir NIU mu
- Masukkan panjang tibia sesuai 2 angka terakhir NIF mu
- Masukkan sudut servo 1 sesuai yang diinginkan
- Masukkan sudut servo 2 sesuai yang diinginkan
  
   4. Lihat Hasil
- Koordinat X dan Y akan muncul


   
      
