from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives,send_mail
from django.conf import settings

#get template sirve para enviar un email con formato html


def send_email(texto,direc_email,telefono,asunto):
    context={'texto':texto ,'direc_email':direc_email,'telefono':telefono,'asunto':asunto}
    template=get_template('correo.html')
    #se redeneriza el template definido
    content=template.render(context)

    email=EmailMultiAlternatives(
        'Nuevo mensaje de {}'.format(direc_email),
        asunto,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER,],    
    )
    email.attach_alternative(content , 'text/html')
    email.send()

def index(request):
    if request.method=='POST':
        texto=request.POST.get('mensaje')
        direc_email=request.POST.get('email')
        asunto=request.POST.get('asunto')
        telefono=request.POST.get('numero')

        send_email(texto,direc_email,telefono,asunto)
        
    
    return render(request,'index.html',{})

'''
def contact(request):
    if request.method=='POST':

        subject=request.POST['asunto']
        print(subject)
        mensaje=request.POST['mensaje']+''+request.POST['email']
        email_from=settings.EMAIL_HOST_USER
        recipient_list=['direc.construcciones.escolares@gmail.com']
        send_mail(subject,mensaje,email_from,recipient_list)

        return render(request,'gracias.html')
    else:
        print('hubo un error')
    return render(request , 'index.html')'''