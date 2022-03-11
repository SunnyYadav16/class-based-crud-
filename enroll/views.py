from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, FormView, CreateView, UpdateView, \
    DeleteView

from .forms import StudentRegistration
from .models import UserData


class UserAddShowView(TemplateView):
    template_name = 'enroll/addandshow.html'

    def get(self, request, *args, **kwargs):
        # context = self.get_context_data(**kwargs)
        forms = StudentRegistration()
        data = UserData.objects.all()
        context = {
            "stu": data,
            "form": forms,
        }
        return self.render_to_response(context)

    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            mail = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            UserData(name=name, email=mail, password=pwd).save()
            return HttpResponseRedirect('/')


class UserDeleteView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        userdata = UserData.objects.get(id=kwargs['id'])
        userdata.delete()
        return super().get_redirect_url(*args, **kwargs)


class update_data(TemplateView):
    template_name = 'enroll/updatestudent.html'

    def get(self, request, id):
        pi = UserData.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        context = {
            'form': fm,
        }
        return self.render_to_response(context)

    def post(self, request, id):
        pi = UserData.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('addandshow')


class UserUpdateView(View):
    def get(self, request, id):
        pi = UserData.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'enroll/updatestudent.html', {'form': fm})

    def post(self, request, id):
        pi = UserData.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('addandshow')
        return HttpResponseRedirect('/')


class showList(ListView):
    model = UserData
    template_name = 'enroll/addandshow.html'
    context_object_name = 'student_key'

    # def get_queryset(self):
    #     return UserData.objects.filter(name="Sunny")


class detailList(DetailView):
    model = UserData
    template_name = 'enroll/detail.html'
    context_object_name = 'student_key'


class ShowForm(FormView):
    template_name = 'enroll/addandshow.html'
    form_class = StudentRegistration
    success_url = '/'

    def form_valid(self, form):
        # cleaned_name = form.cleaned_data['name']
        # cleaned_email = form.cleaned_data['email']
        # cleaned_pwd = form.cleaned_data['password']
        # UserData(name=cleaned_name, email=cleaned_email, password=cleaned_pwd).save()
        form.save()
        return HttpResponse(self.success_url)


class showListandForm(FormView, ListView):
    model = UserData
    template_name = 'enroll/addandshow.html'
    context_object_name = 'student_key'
    form_class = StudentRegistration
    success_url = '/'


""" Using CreateView for creating new users. """
class CreateUser(CreateView):
    model = UserData
    # fields = ['name', 'email', 'password']
    fields = '__all__'
    template_name = 'enroll/addandshow.html'
    success_url = "/thanks/"


class thankyou(TemplateView):
    template_name = 'enroll/thanks.html'


class updatestudent(UpdateView, ListView):
    model = UserData
    # fields = ['name', 'email', 'password']
    form_class = StudentRegistration
    # context_object_name = 'student_key'
    template_name = 'enroll/addandshow.html'
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_key'] = UserData.objects.all()
        return context


class deletestudent(DeleteView):
    model = UserData
    # template_name = 'enroll/delete_form.html'
    success_url = '/'
