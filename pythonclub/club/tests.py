from django.test import TestCase
from .models import Meeting, MeetingMinutes
from django .urls import reverse #what does this one do

# Create your tests here.

class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='Django Jamboree')
        self.assertEqual(str(meeting), meeting.meetingtitle)

        def test_tablename(self):
            self.assertEqual(str(Meeting._meta.db_table), 'meeting')

#testing a view

