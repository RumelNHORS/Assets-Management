from django.shortcuts import render, HttpResponseRedirect
from . models import AssetsModel, CheckIn, CheckOut
from . forms import CustomerRegistrationForm, ProductCheckInForm, ProductCheckOutForm
from django.views.generic.base import TemplateView, RedirectView
from django.views import View

class CustomerAddView(TemplateView):
    template_name = 'myapp/add_show.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = CustomerRegistrationForm()
        cmr = AssetsModel.objects.all()
        context = {'cmr':cmr, 'form':fm}
        return context

    def post(self, request):
        if request.method == 'POST':
            fm = CustomerRegistrationForm(request.POST)
            if fm.is_valid():
                fm.save()
            return HttpResponseRedirect('/')

class CustomerUpdate(View):
    def get(self, request, id):
        up = AssetsModel.objects.get(pk=id)
        fm = CustomerRegistrationForm(instance=up)
        return render(request, 'myapp/update.html', {'form':fm})
    def post(self, request, id):
        up = AssetsModel.objects.get(pk=id)
        fm = CustomerRegistrationForm(request.POST, instance=up)
        if fm.is_valid():
            fm.save()
        return render(request, 'myapp/update.html', {'form':fm})


class CustomerDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        AssetsModel.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


class CheckInAddView(TemplateView):
    template_name = 'myapp/checkin.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = ProductCheckInForm()
        cmr = CheckIn.objects.all()
        context = {'cmr':cmr, 'form':fm}
        return context

    def post(self, request):
        if request.method == 'POST':
            fm = ProductCheckInForm(request.POST)
            if fm.is_valid():
                fm.save()
            return render(request, 'myapp/checkin.html')