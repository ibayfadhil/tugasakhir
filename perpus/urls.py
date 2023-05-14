from django.contrib import admin
from django.urls import path
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('dekripsi/', dekripsi, name='dekripsi'),
    path('penerbit/', penerbit, name='penerbit'),
    path('keygen/', keygen, name='keygen'),
    path('buku/', buku, name='buku'),
    path('buku/tambah/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name="hapus_buku"),
    path('buku/export/xls/', export_xls, name='export_xls'),
    path('auth/masuk/', LoginView.as_view(), name='masuk'),
    path('auth/keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('user/', users, name='users'),
    path('user/add/', signup, name='signup'),
    path('download/<path:fp>/', download_file, name='download_file'),
]

urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)