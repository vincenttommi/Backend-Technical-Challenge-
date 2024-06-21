import africastalking
from django.test import TestCase
from decouple  import config
#Decouple helps one to organize settigs so  no can  change parameters
#without need to redeploy the app

from ..serializers import sendsms
USERNAME = config('AT_USERNAME')
API_KEY = config('AT_API_KEY')

africastalking.initialize(USERNAME,API_KEY)
token_service  = africastalking.Token
service  = africastalking.SMS


class TestSmsService(TestCase):
    def test_send(self):
        """
        Test Sending SMS
        """
        res  = service.send('Test message',['0759209325'])
        recipients = res['SMSMessageData']['Recipients']
        assert recipients[0]['status'] == 'Success'
        


