from django.shortcuts import render
from django.template.defaulttags import register
from django.http import HttpResponse
from datetime import date

def main(request):
    year, month, day = str(date.today()).split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 
              'Октябрь', 'Ноябрь', 'Декабрь']

    data = {
        'year': year,
        'month': months[month - 1],
        'day': day
    }
    return render(request, 'main/main.html', data)
