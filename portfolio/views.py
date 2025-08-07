from django.shortcuts import render
from django.views.generic import ListView
from django.core.mail import send_mail
from portfolio.models import Info, Category
from django.conf import settings



class InfoList(ListView):
    model = Info
    context_object_name = 'categories'
    template_name = 'portfolio/index.html'
    extra_context = {
        "title":"My Portfolio"
    }

    def get_queryset(self):
        categories = Category.objects.all()
        data = []
        for category in categories:
            infos = category.infos.all()

            data.append({
                "title":category.title,
                "infos":infos
            })
        return data

class InfoListByCategory(ListView):
    model = Info
    context_object_name = "infos"
    template_name = 'portfolio/index.html'
    extra_context = {
        "title":"Portfolio Page"
    }



def send_email_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f"New message: from {name}"

        full_message = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        return redirect("index")

    return render(request, "base.html")