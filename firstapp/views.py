from django.shortcuts import render

# Create your views here.
from firstapp.models import Alex


# функция заносит данные из формы в бозу данных
def form_set(request):
    a = request.GET.get('context_value', '')
    # a_2 = request.GET.get('title_value', '')
    # a_3 = request.GET.get('slug_value', '')
    if str(a) != '':  # or str(a_2) != '' or str(a_3) != '':
        i = Alex.objects.create(context=a)#, title=a_2, slug=a_3)
        i.save()
    return render(request, 'admin1.html')


# вывод информации из базы данных на главную страницу
def main_page(request):
    y = Alex.objects.values_list().values()
    context = {
        'context_value': y,
    }
    return render(request, 'main_page.html', context)
