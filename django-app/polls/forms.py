from django import forms

from .models import Vendor

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('vendor_name', 'vendor_eans',)

class RawVendorForm(forms.Form):
	vendor_name = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
	vendor_eans = forms.CharField(required=False,
								  widget=forms.Textarea(
								  attrs={
								  		"placeholder":"Your ean codes",
								  		"class": "new-class-name two",
								  		"id": "my-is-for-textarea",
								  		"rows" : 20,
								  		"cols" :120

								  }
							)
						)