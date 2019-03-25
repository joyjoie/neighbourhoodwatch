from django.test import TestCase
import datetime as dt
# Create your tests here.
from .models import Neighbourhood,Profile,Business,Comments
import datetime as dt

class NeighbourhoodTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.type= Neighbourhood(name='south')

    def test_instance(self):
        self.assertTrue(isinstance(self.type,Neighbourhood))

    def test_init(self):
       
        self.assertTrue(self.type.name == 'south')

  
    def tearDown(self):
       Neighbourhood.objects.all().delete()
       

class ProfileTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.type= Profile(bio ="me")

    def test_instance(self):
        self.assertTrue(isinstance(self.type,Profile))

    def test_init(self):
       
        self.assertTrue(self.type.bio == "me")

  
    def tearDown(self):
       Profile.objects.all().delete()
    

class BusinessTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.type= Business(name ="joy")

    def test_instance(self):
        self.assertTrue(isinstance(self.type,Business))

    def test_init(self):
       
        self.assertTrue(self.type.name == "joy")

  
    def tearDown(self):
       Business.objects.all().delete()


class CommentsTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.type= Comments(comment="hi")

    def test_instance(self):
        self.assertTrue(isinstance(self.type,Comments))

    def test_init(self):
       
        self.assertTrue(self.type.comment == "hi")

  
    def tearDown(self):
       Comments.objects.all().delete()
