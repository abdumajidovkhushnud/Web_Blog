from django.contrib.auth.forms import UserCreationForm  #form u-n django model
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') #after signup automatically goes to login
    template_name = 'registration/signup.html'  # bu esa papkani ichidagi ösha fayl