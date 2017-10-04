from django.test import TestCase

# Create your tests here.
class CollectionTest(TestCase):
    def test_index(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)

    def test_no_logic_page(self):
        r = self.client.get('/fruit/')
        self.assertEqual(r.status_code, 200)
