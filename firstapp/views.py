from django.shortcuts import render

# Create your views here.
from firstapp.models import Alex


# функция заносит данные из формы в бозу данных
def form_set(request):
    a = request.GET.get('content_value', '')
    a_2 = request.GET.get('title_value', '')
    a_3 = request.GET.get('slug_value', '')
    if str(a) != '' or str(a_2) != '' or str(a_3) != '':
        i = Alex.objects.create(content=a, title=a_2, slug=a_3)
        i.save()
    return render(request, 'admin1.html')


# вывод информации из базы данных на главную страницу
def main_page(request):
    y = Alex.objects.values_list().values()
    content = {
        'content_value': y,
    }
    return render(request, 'main_page.html', content)


# выводит на экран инфу из поля контент
def cnt(request, x):
    y = Alex.objects.filter(slug=x).values_list()
    template = "template.html"
    content = {
        'content': y[0][1],
        'title': y[0][2]
    }
    return render(request, template, content)


# функция для вывода админки
def admin(request):
    return render(request, 'admin/admin.html')


# вывод инфы из базы данных на articles.html
def articles(request):
    y = Alex.objects.values_list().values()
    content = {
        'content_value': y,
    }
    return render(request, 'admin/articles.html', content)


# добавляет данные в базу на странице add.html
def add(request):
    a = request.GET.get('content_value', '')
    a_2 = request.GET.get('title_value', '')
    a_3 = request.GET.get('slug_value', '')
    if str(a) != '' or str(a_2) != '' or str(a_3) != '':
        i = Alex.objects.create(content=a, title=a_2, slug=a_3)
        i.save()
    return render(request, 'admin/add.html')
