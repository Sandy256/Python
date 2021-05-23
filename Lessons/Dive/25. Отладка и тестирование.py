import requests
import re

def main(site_url, substring):
    import pdb
    pdb.set_trace()
    site_code = get_site_code(site_url)
    matching_substring = get_matching_substring(site_code, substring)
    print('"{}" found {} times in {}'.format(
        substring, len(matching_substring), site_url
    ))
def get_site_code(site_url):
    if not site_url.startswith('http'):
        site_url = 'http://' + site_url

    return  requests.get(site_url).text

def get_matching_substring(source, substring):
    return re.findall(source, substring)

main('mail.ru', 'script')

# Тестирование
# test_python.py

import unittest


class TestPython(unittest.TestCase):
    def test_float_to_int_coercion(self):
        self.assertEqual(1, int(1.0))

    def test_get_empty_dict(self):
        self.assertIsNone({}.get('key'))

    def test_trueness(self):
        self.assertTrue(bool(10))
# project/tests $> python3 -m unittest test_python.py

# test_division.py

import unittest


class TestDivision(unittest.TestCase):
    def test_integer_division(self):
        self.assertIs(10 / 5, 2)
# project/tests $> python3 -m unittest test_division.py