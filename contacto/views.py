from pdb import post_mortem
from django.shortcuts import redirect, render
from django.core.mail import send_mail, EmailMessage
from .forms import Contacto

# Create your views here.

def contacto(request):

    formulario = Contacto()

    if request.method == "POST":
        formulario = Contacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            correo = EmailMessage("Correo de contacto desde Portafolio", "Usuario: {}, Email: {}.\n\nMensaje:\n{}".format(nombre, email, contenido), 
            "", ['juanpcandal@gmail.com'], ['juanpcandal@gmail.com'], reply_to=[email])

            try:
                correo.send()
                return redirect("/contacto/?Valido")
            except:
                return redirect("/contacto/?Invalido")

    return render(request, 'contacto.html', {'formulario' : formulario})