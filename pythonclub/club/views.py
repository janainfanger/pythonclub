from django.shortcuts import render, get_object_or_404
from.models import Resource, Meeting
from .forms import MeetingForm

# Create your views here.

def index(request):
    return render(request, 'club/index.html')

def resources(request):
    resources=Resource.objects.all()
    return render(request, 'club/resources.html', {'resources': resources})

def getmeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list': meeting_list})

def meetingdetail(request, id):
    detail=get_object_or_404(Meeting, pk=id)
    context = { 'detail': detail}
    return render (request, 'club/details.html', context=context)

#forms view
def addMeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True) #if form is filles, commit and save to database
            post.save()
            form=MeetingForm #reloads empty form after saving input data
    else:
        form=MeetingForm()
    return render (request, 'club/addmeeting.html', {'form': form})


