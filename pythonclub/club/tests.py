from django.test import TestCase
from .models import Meeting, MeetingMinutes
from django .urls import reverse #what does this one do

# Create your tests here.

class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='Django Jamboree')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

class MinutesTest(TestCase):
    def test_stringOutput(self):
        minutes=MeetingMinutes(minutes='meetingid')
        self.assertEqual(str(minutes), MeetingMinutes.minutes)

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')


class Resource(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='userid')
        self.assertEqual(str(resource), resource.resourcename)

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class Event(TestCase):
    def test_stringOutput(Self):
        event=Event(event='eventtitle')
        self.assertEqual(str(event), event.eventtitle)

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db.table), 'event')
        