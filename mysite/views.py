from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from mysite.models import Contact


class HomeView(TemplateView):
    template_name = "Main.html"

class NewsView(TemplateView):
    template_name = "news.html"

    def get_context_data(self, **kwargs):

        keyword = self.request.GET.get("keyword")
        contacts = Contact.objects.all()
        if keyword:
            contacts = Contact.objects.filter(name__contains=keyword)
        context = {
            'contacts': contacts
        }
        return context

class LifeView(TemplateView):
    template_name = "life.html"

class AboutView(TemplateView):
    template_name = "about.html"

class KonkursView(TemplateView):
    template_name = "kurs.html"
class SignView(TemplateView):
    template_name = "sign.html"
class ProfilePage(TemplateView):
    template_name = "registration/profile.html"
class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))
        return render(request, self.template_name)