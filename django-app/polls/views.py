from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import VendorForm #, RawVendorForm
from django.shortcuts import redirect
from .models import Vendor
import requests
from subprocess import run, PIPE
import sys



def vendor_detail(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    return render(request, 'polls/vendor_detail.html', {'vendor': vendor})

def vendor_list(request):
    vendors =Vendor.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'polls/vendor_list.html', {'vendors': vendors})

def vendor_new(request):
    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.author = request.user
            vendor.published_date = timezone.now()
            vendor.save()
            return redirect('vendor_detail', pk=vendor.pk)
    else:
        form = VendorForm()
    return render(request, 'polls/vendor_edit.html', {'form': form})


def vendor_edit(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == "POST":
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.published_date = timezone.now()
            vendor.save()
            return redirect('vendor_detail', pk=vendor.pk)
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'polls/vendor_edit.html', {'form': form})


def vendor_button(request):
    data=requests.get("https://www.google.es")
    print(data.text)
    data=data.text
    return render(request, 'polls/button.html', {'data': data})

def button(request): 
    return render(request, 'polls/button.html')


def external(request):
    inp=request.POST.get("param")
    out= run([sys.executable,'//Users//Abacuc//Project_IH_Abacuc//Scraping.py',inp], shell=False, stdout=PIPE)
    print(out)

    return render(request, 'polls/button.html', {'data1': out.stdout})

