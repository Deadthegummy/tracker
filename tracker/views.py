from django.shortcuts import render_to_response
from django.http import HttpResponse
from tracker.models import Event


# Create your views here.


def index(request):
    event_list = Event.objects.all()
    event_data = []
    for event in event_list:
        event_data.append(event.format_data())

    context = {'exercises': event_data}
    return render_to_response('exercise_list.html', context)


def detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    context = {'event': {'exercise_type': event.exercise_type.type,
                         'date': event.date}}
    return render_to_response('exercise_detail.html', context)


