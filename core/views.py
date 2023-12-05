from django.shortcuts import render
from core.models import Part, Contact
from django.views.generic import  TemplateView , ListView ,FormView
from accounts.models import User
# 
from django.urls import reverse_lazy
from core.forms import ContactForm
from django.views.generic.edit import FormMixin

class MainView(TemplateView,FormMixin):
    template_name = "main-index.html"
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy('core:main')
    
    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)

    def form_valid(self, form):
        form.instance.account = self.request.user
        post = Post.objects.get(pk=int(self.request.POST['post']))
        form.instance.account_post = post
        form.save()
        return super().form_valid(form)
 
 

class WinView(ListView):
    model = Part
    template_name = 'main2-index.html'
    context_object_name = 'parts'

class ShopListView(ListView):
    model = Part
    template_name = 'autopart-magazine-list.html'
    context_object_name = 'parts'



class ContactView(FormView,FormMixin):
    model = Contact
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:main')

 

    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)


class AboutView(ListView):
    model = Part
    template_name = 'aboutus.html'
    context_object_name = 'parts'

