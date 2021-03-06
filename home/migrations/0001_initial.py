# Generated by Django 3.0.7 on 2020-07-14 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonViTinh',
            fields=[
                ('madonvitinh', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('tendonvitinh', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HoSoDL',
            fields=[
                ('tendaily', models.CharField(max_length=100)),
                ('mahosodaily', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('dienthoai', models.CharField(max_length=100)),
                ('diachi', models.CharField(max_length=100)),
                ('ngaytiepnhan', models.DateTimeField(auto_now_add=True)),
                ('tienno', models.PositiveIntegerField(default=0, max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoaiDL',
            fields=[
                ('maloaidaily', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('tenloaidaily', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PhieuXuatHang',
            fields=[
                ('maphieuxuathang', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ngaylapphieu', models.DateTimeField(auto_now_add=True)),
                ('tongtien', models.CharField(max_length=1000000)),
                ('sotientra', models.CharField(max_length=1000000)),
                ('active1', models.BooleanField(default=True)),
                ('madaily', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.HoSoDL')),
            ],
        ),
        migrations.CreateModel(
            name='Quan',
            fields=[
                ('maquan', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('tenquan', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('maphieuthutien', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ngaythutien', models.DateTimeField(auto_now_add=True)),
                ('sotienthu', models.CharField(max_length=1000000)),
                ('active3', models.BooleanField(default=True)),
                ('maphieuxuathang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.PhieuXuatHang')),
            ],
        ),
        migrations.CreateModel(
            name='MatHang',
            fields=[
                ('mamathang', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('tenmathang', models.CharField(max_length=100)),
                ('gia', models.CharField(max_length=1000000)),
                ('soluong', models.CharField(max_length=100)),
                ('active2', models.BooleanField(default=True)),
                ('madonvi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.DonViTinh')),
            ],
        ),
        migrations.AddField(
            model_name='hosodl',
            name='loaidaily',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.LoaiDL'),
        ),
        migrations.AddField(
            model_name='hosodl',
            name='quan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Quan'),
        ),
        migrations.CreateModel(
            name='CTPhieuXuatHang',
            fields=[
                ('machitietphieuxuathang', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('soluong', models.CharField(max_length=1000)),
                ('dongia', models.CharField(max_length=1000000)),
                ('thanhtien', models.CharField(max_length=1000000)),
                ('active3', models.BooleanField(default=True)),
                ('madonvitinh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.DonViTinh')),
                ('mamathang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.MatHang')),
                ('maphieuxuathang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.PhieuXuatHang')),
            ],
        ),
    ]
