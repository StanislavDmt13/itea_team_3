from django.shortcuts import render
import calendar
from calendar import HTMLCalendar


def event_calendar(request, year, month):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)

    return render(request, 'calendar.html',{
        'month': month,
        'year':  year,
        'cal':  cal,
    })
