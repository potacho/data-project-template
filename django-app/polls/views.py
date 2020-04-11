from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import VendorForm
from django.shortcuts import redirect
from .models import Vendor




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


