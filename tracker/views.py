from django.shortcuts import render_to_response
from django.http import HttpResponse
from tracker.models import Event
from django.views import View
import json


# Create your views here.

class RESTDispatch(View):
    @staticmethod
    def json_response(content='', status=200):
        return HttpResponse(json.dumps(content, sort_keys=True),
                            status=status,
                            content_type='application/json')

    @staticmethod
    def error_response(status, message='', content={}):
        content['error'] = str(message)
        return HttpResponse(json.dumps(content),
                            status=status,
                            content_type='application/json')


class EventView(RESTDispatch):
    def get(self, request):
        event_list = Event.objects.all()
        event_data = []
        for event in event_list:
            event_data.append(event.format_data())
        return self.json_response(content=event_data)


class EventDetailView(RESTDispatch):
    def get(self, request, event_id):
        # gets single event and all attributes, needs to be done
        return self.json_response()


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


