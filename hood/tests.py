from  django . test  import  TestCase
from .models import neighbourhood,healthservices
from django.contrib.auth.models import User
import  datetime  as  dt
# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self . Byimana  =  neighbourhood ( neighbourhood = 'Byimana' )

    def test_instance(self):
        self.assertTrue(isinstance(self.Byimana,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Byimana.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self . Byimana . delete_neighbourhood ( 'Byimana' )
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

class healthservicesTestClass(TestCase):
    def setUp(self):
        self.Sauna = healthservices(healthservices='Sauna')

    def test_instance(self):
        self.assertTrue(isinstance(self.Sauna,healthservices))

    def tearDown(self):
        healthservices.objects.all().delete()

    def test_save_method(self):
        self.Sauna.save_healthservices()
        health = healthservices.objects.all()
        self.assertTrue(len(health)>0)

    def test_delete_method(self):
        self.Sauna.delete_healthservices('Sauna')
        health = healthservices.objects.all()
        self.assertTrue(len(health)==0)