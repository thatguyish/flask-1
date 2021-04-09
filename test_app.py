from unittest import TestCase
from app import app

class ForexViewsTestCase(TestCase):

    def test0_home_view(self):
        with app.test_client() as client:
            res = client.get('/')
            self.assertEqual(res.status_code,200)


    def test0_convert_view(self):
        with app.test_client() as client:
            res = client.post('/convert',data = dict(convert_from="usd",convert_to="usd",convert_amount=1,follow_redirects=True))
            html = res.get_data(as_text =True)
            self.assertIn("1",html)