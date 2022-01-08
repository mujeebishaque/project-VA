from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class IndexView(View):
    def get(self, request):
        template = 'analytics'
        return render(request, template, context={})
    
    def post(self, request):
        tempalte = 'analytics'
        return render(request, template, context={})