from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.db.models import Q


from .forms import RegisterForm

from .models import Register
from devices.models import Device

def home(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')


def register_success_view(request):
    return render(request, 'register_success.html')


@login_required
def register_list_view(request):
    registers = Register.objects.all().order_by('date')

    return render(request, 'admin/submission_list.html', {'registers': registers})


def register_create_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # Commented until define email configs
            # email sender section
            # data = form.cleaned_data
            # recipient_email = data['member_email'] if data['register_type'] == 'member' else data['aggregator_email']
            # subject = 'You’ve started registration for the TER!'
            # template_email = 'mail_template_confirmation.html'
            # redirect_page = "register_success"
            # send_email(request, subject, recipient_email, template_email, redirect_page)
            form.save()

            return render(request, "register_success.html")

    context = {
        'form': form
    }
    return render(request, "register_create.html", context)


@login_required
def submission_detail_view(request, pk):
    obj = Register.objects.get(id=pk)
    if request.method == 'POST':
        if 'mark_registered' in request.POST:
            print("EMAIL SENDING")
            # email sender section
            # recipient_email = obj.member_email if obj.register_type == 'member' else obj.aggregator_email
            # subject = "Configure your VEN for the TER."
            # template_email = 'mail_template_registered.html'
            # redirect_page = "submissions"
            # send_email(request, subject, recipient_email, template_email, redirect_page)

        obj.delete()

        return redirect('submissions')

    return render(request, "admin/submission_detail.html", {'object': obj})


@login_required
def settings_view(request):
    return render(request, 'admin/settings.html')


def send_email(request, subject, recipient_email, template_email, redirect_page):
    subject = subject
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [recipient_email]
    message = get_template(template_email).render()

    msg = EmailMessage(subject, message, email_from, recipient_list)
    msg.content_subtype = 'html'
    msg.send()

    return render(request, redirect_page)


class SearchDeviceView(ListView):
    model = Device
    template_name = 'lookup_device.html'
    context_object_name = 'results'
    show_result = False

    def get_queryset(self):
       result = super(SearchDeviceView, self).get_queryset()
       query = self.request.GET.get('search')

       if query:
          postresult = Device.objects.filter(Q(device_id=query) | Q(ven_id=query))
          result = postresult
       else:
           result = None
       return result
