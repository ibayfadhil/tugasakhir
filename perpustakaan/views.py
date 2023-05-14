from django.shortcuts import render, redirect, HttpResponse
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BukuResource
from django.contrib.auth.models import User
from .AES import *
from django.http import FileResponse
from django.template import loader
from .forms import *
from django.shortcuts import redirect

def home(request):
    context = {
        'banner':'static/images/banner_about.png',
    }
    template = 'home.html'
    return render(request, template, context)

@login_required(login_url=settings.LOGIN_URL)
def users(request):
    users = User.objects.all()
    template = 'users.html'
    context = {
        'users':users,
    }
    return render(request, template, context)

@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="laporan buku.xls"'
    return response

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat!")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form,
        }
    return render(request, 'signup.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    messages.success(request, "Data Berhasil dihapus!")
    return redirect('buku')

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku,
        }
    return render(request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    books = Buku.objects.all()

    konteks = {
        'books': books,
    }
    return render(request, 'buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    return render(request, 'penerbit.html')

#cp
@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            ins = form.save()
            DB = Buku.objects
            data = DB.get(id=ins.pk)
            fp = data.dokumen.path
            kp = data.key_enkripsi.path
            ext = os.path.splitext(fp)[1].upper().replace(".","")
            if ext in pdf : encpath = EncryptPdf(fp,kp)
            elif ext in doc : encpath = EncryptDoc(fp,kp)
            elif ext in png : encpath = EncryptImage(fp,kp)
            elif ext in xlsx : encpath = EncryptExcel(fp,kp)
            elif ext == "TXT" : encpath = EncryptTXT(fp,kp)
            if encpath : 
                data.encpath = encpath.replace('\\', '/').replace("+","_")
                data.save()
            form = FormBuku()
            pesan = "Data berhasil disimpan"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-buku.html', konteks)
    else:
        form = FormBuku()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-buku.html', konteks)

def dekripsi(request):
    context = {"form":FileUploadForm()}
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file1 = form.cleaned_data['file1']
            file2 = form.cleaned_data['file2']
            os.makedirs(f"./media/dec/{file1.name}", exist_ok=True)
            with open(f'./media/dec/{file1.name}/' + file1.name, 'wb+') as destination:
                for chunk in file1.chunks():
                    destination.write(chunk)
            with open(f'./media/dec/{file1.name}/' + file2.name, 'wb+') as destination:
                for chunk in file2.chunks():
                    destination.write(chunk)
            ext = os.path.splitext(file1.name)[1].upper().replace(".","")
            fp = f'./media/dec/{file1.name}/'+ file1.name
            kp = f'./media/dec/{file1.name}/'+ file2.name
            if ext in pdf : encpath = DecryptPdf(fp,kp)
            elif ext in doc : encpath = DecryptDoc(fp,kp)
            elif ext in png : encpath = DecryptImage(fp,kp)
            elif ext in xlsx : encpath = DecryptExcel(fp,kp)
            elif ext == "TXT" : encpath = DecryptTXT(fp,kp) 
            if encpath : 
                url = "/download/" + encpath.replace('\\', '/')
                return redirect(url)
    else:
        form = FileUploadForm()
    response = HttpResponse(loader.get_template("dekripsi.html").render(context, request))
    return response

def download_file(request, fp):
    response = FileResponse(open(fp, 'rb'))
    fn = os.path.basename(fp)
    if "_encrypted_decrypted" in fn: 
        fn = fn.replace("_encrypted","")
    response['Content-Disposition'] = f'attachment; filename="{fn}"'
    return response

def keygen(request):
    filename = 'key.key' # replace with your actual filename
    content_type = 'application/octet-stream'
    response = HttpResponse(GenKey(), content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
