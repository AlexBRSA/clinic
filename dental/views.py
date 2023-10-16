from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

from .forms import UploadImageForm

#почта
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from clinic.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL

# menu = [{'title': "О клинике", 'url_name': 'about'},
#         {'title': "Цены", 'price': 'price'},
#         {'title': "Врачи", 'url_name': 'contact'},        
#         {'title': "Услуги", 'url_name': 'contact'},
#         {'title': "Фотогалерея", 'url_name': 'contact'},
#         {'title': "Контакты", 'url_name': 'contact'},
#         {'title': "Акции", 'url_name': 'contact'},
#         {'title': "Войти", 'url_name': 'login'}
# ]

contact = [{'title': "instagram", 'url_name': 'about'},
        {'title': "vk", 'url_name': 'add_page'},
        {'title': "whatsapp", 'url_name': 'contact'},        
        {'title': "fone", 'url_name': 'contact'}        
]

def index(request):
    posts = Dental.objects.all()

    context = {
        'contact' :contact, 
        'posts': posts,
        # 'menu': menu,
        'title': '«Шикарная улыбка»',
        'cat_selected': 0,
    }

    return render(request, 'dental/index.html', context=context)

def price(request):
    
    context = {
        'contact' :contact,         
        # 'menu': menu,
        'title': '«Цены на услуги»',
        'cat_selected': 0,
    }
    return render(request, 'dental/price.html', context=context)

def personal(request):
    posts = Dental.objects.all()
    context = {
        'contact' :contact,         
        'posts': posts,
        'title': '«Наши врачи»',
        'cat_selected': 0,
    }
    return render(request, 'dental/personal.html', context=context)

def services(request):
    
    context = {
        'contact' :contact,         
        # 'menu': menu,
        'title': '«Весь спектр услуг»',
        'cat_selected': 0,
    }
    return render(request, 'dental/services.html', context=context)


def foto(request):
   
    context = {
        'contact' :contact,         
        # 'menu': menu,
        'title': '«foto»',
        'cat_selected': 0,
    }
    return render(request, 'dental/foto.html', context=context)

def contacts(request):
   
    context = {
        'contact' :contact,         
        # 'menu': menu,
        'title': '«contacts»',
        'cat_selected': 0,
    }
    return render(request, 'dental/contacts.html', context=context)

def actions(request):
   
    context = {
        'contact' :contact,         
        # 'menu': menu,
        'title': '«actions»',
        'cat_selected': 0,
    }
    return render(request, 'dental/actions.html', context=context)

def enter(request):
   
    context = {
        'contact' :contact,         
        # 'menu': menu,
        'title': '«enter»',
        'cat_selected': 0,
    }
    return render(request, 'dental/enter.html', context=context)

def email(request):
   
    context = {
        'contact' :contact,         
        # 'menu': menu,
        'title': '«enter2»',
        'cat_selected': 0,
    }
    return render(request, 'dental/email.html', context=context)
# foto

def foto_gallery(request):

    gallery = GalleryImage.objects.all()

    

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)

        if form.is_valid():
            for image in request.FILES.getlist('images'):
                GalleryImage.objects.create(image=image)
    else:
        form = UploadImageForm()

    
    return render(request, 'dental/foto.html', {'form': form, 'gallery': gallery})

#почта

def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "dental/email.html", {'form': form})

def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')



# Отображение статьи с id
def show_post(request, post_slug):
    post = get_object_or_404(Dental, slug=post_slug)

    context = {
        'post': post,        
        'title': post.title,
        'cat_selected': post,
    }

    return render(request, 'dental/post.html', context=context)