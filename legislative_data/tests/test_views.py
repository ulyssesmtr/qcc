from django.test import TestCase
from django.shortcuts import resolve_url as r

class IndexTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('index'))

    def test_get(self):
        """Should return status 200"""
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        """Should use the specified template"""
        self.assertTemplateUsed(self.resp, 'index.html')
    
    def test_html(self):
        """Should contain the following strings in the html"""
        contents = ('Information on Bills', 'Information on Legislators')
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)
    

class LegislatorData(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('legislator_data'))

    def test_get(self):
        """Should return status 200"""
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        """Should use the specified template"""
        self.assertTemplateUsed(self.resp, 'legislator_data.html')
    
    def test_html(self):
        """Should contain the following strings in the html"""
        contents = (
            'Legislators Bill Votes Report', 
            'ID',
            'Legislator',
            'Supported bills',
            'Opposed bills',
            'Return')
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class BillData(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('bill_data'))

    def test_get(self):
        """Should return status 200"""
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        """Should use the specified template"""
        self.assertTemplateUsed(self.resp, 'bill_data.html')
    
    def test_html(self):
        """Should contain the following strings in the html"""
        contents = (
            'Bills Report', 
            'ID',
            'Bill',
            'Supporters',
            'Opposers',
            'Primary Sponsor')
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)
