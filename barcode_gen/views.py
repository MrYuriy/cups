from django.shortcuts import render
from django.views import View
from .utils import gen_labels
from django.shortcuts import render, redirect
from django.urls import reverse

class HomeView(View):
    template_name = "barcode_gen/gen_labels.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        index = 0
        labels_code = ""
        while request.POST.get(f"qty_{index}"):
            sku = request.POST.get(f"sku_{index}", "")
            ean = request.POST.get(f"ean_{index}", "")
            qty = request.POST.get(f"qty_{index}")
            labels_code += gen_labels(barcod=ean, sku=sku, qty=int(qty))
            index += 1
        context = {"labels_code": labels_code}
        return render(request, self.template_name, context=context)

