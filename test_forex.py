from forex import is_valid_currency,convert_currency
from unittest import TestCase

class ForexTestCase(TestCase):
    """testing is valid currency"""
    def test0_is_valid_currency(self):
        self.assertEqual(is_valid_currency("eur"),True)

    def test1_is_valid_currency(self):
        self.assertEqual(is_valid_currency("usd"),True)

    def test2_is_valid_currency(self):
        self.assertEqual(is_valid_currency("bacon"),False)

    """testing currency converter"""
    def test0_convert_currency(self):
        self.assertEqual(convert_currency("usd","usd",1),1)

    def test1_convert_currency(self):
        self.assertEqual(convert_currency("eur","eur",1),1)
    