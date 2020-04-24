from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import VendorForm, RawVendorForm
from django.shortcuts import redirect
from .models import Vendor
import requests
from subprocess import run, PIPE
import sys
import pandas as pd




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


# def vendor_edit(request, pk):
#     vendor = get_object_or_404(Vendor, pk=pk)
#     if request.method == "POST":
#         form = VendorForm(request.POST, instance=vendor)
#         if form.is_valid():
#             vendor = form.save(commit=False)
#             vendor.published_date = timezone.now()
#             vendor.save()
#             return redirect('vendor_detail', pk=vendor.pk)
#     else:
#         form = VendorForm(instance=vendor)
#     return render(request, 'polls/vendor_edit.html', {'form': form})


def data_view(request):

    inp=request.POST.get("param")
    out= run([sys.executable,'//Users//Abacuc//Project_IH_Abacuc//django-app//Scraping.py',inp], shell=False, stdout=PIPE)
    
    carrefour_info= pd.read_csv('//Users//Abacuc//Project_IH_Abacuc//csv//carrefour_info.csv')
    carrefour_info = carrefour_info.to_html()
    ebay_info= pd.read_csv('//Users//Abacuc//Project_IH_Abacuc//csv//ebay_info.csv')
    ebay_info= ebay_info.to_html()
    amazon_info = pd.read_csv('//Users//Abacuc//Project_IH_Abacuc//csv//amazon_info.csv')
    amazon_info= amazon_info.to_html()
    eci_info = pd.read_csv('//Users//Abacuc//Project_IH_Abacuc//csv//eci_info.csv')
    eci_info= eci_info.to_html()
    mm_info = pd.read_csv('//Users//Abacuc//Project_IH_Abacuc//csv//mm_info.csv')
    mm_info= mm_info.to_html()


    return render(request, 'polls/data.html', {'carrefour_info': carrefour_info, 'ebay_info': ebay_info, 'amazon_info': amazon_info , 'eci_info': eci_info, 'mm_info': mm_info  })

def results_view(request):

    inp=request.POST.get("param")
    inp1=request.POST.get("categoria de productos")
    inp2=request.POST.get("Edad Media cliente")
    inp3=request.POST.get("Tamaño Familia")
    inp4=request.POST.get("Tipo de comunidad")
    result= run([sys.executable,'//Users//Abacuc//Project_IH_Abacuc//django-app//Selection.py',inp,inp1,inp2,inp3,inp4], shell=False, stdout=PIPE)
    print(result)
    return render(request, 'polls/results.html', {'result': result.stdout})




