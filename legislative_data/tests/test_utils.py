from django.test import TestCase
from legislative_data.utils import read_csv, calc_votes, get_legislator_data, get_bill_data

class TestUtils(TestCase):

    def test_read_csv_list(self):
        """Should return a list"""
        legislators = read_csv('legislative_data/csvs/legislators.csv')
        self.assertIsInstance(legislators, list)

    def test_read_csv_format(self):
        """Should return a list of dicts with the keys shown below"""
        legislators = read_csv('legislative_data/csvs/legislators.csv')
        self.assertListEqual(['id', 'name'], list(legislators[0].keys()))
    
    def test_calc_vote_dict(self):
        """Should return a dict"""
        vote_results = read_csv('legislative_data/csvs/vote_results.csv')
        calculated_votes = calc_votes(vote_results, 'legislator_id')
        self.assertIsInstance(calculated_votes, dict)

    def test_calc_votes_format(self):
        """Should return a dict where every key value is a dict with the keys shown below"""
        vote_results = read_csv('legislative_data/csvs/vote_results.csv')
        calculated_votes = calc_votes(vote_results, 'legislator_id')
        self.assertListEqual(['1', '2'], list(calculated_votes.get('400440').keys()))
    
    def test_get_legislator_data_list(self):
        """Should return a list"""
        legislator_data = get_legislator_data()
        self.assertIsInstance(legislator_data, list)

    def test_get_legislator_data_format(self):
        """Should return a list of dicts with the keys shown below"""
        legislator_data = get_legislator_data()
        self.assertListEqual(['legislator_id', 'legislator_name', 'yea_votes', 'nay_votes'],
                             list(legislator_data[0].keys()))

    def test_get_bill_data_list(self):
        """Should return a list"""
        bill_data = get_bill_data()
        self.assertIsInstance(bill_data, list)

    def test_get_bill_data(self):
        """Should return a list of dicts with the format shown below"""
        bill_data = get_bill_data()
        self.assertListEqual(['id', 'title', 'yea_votes', 'nay_votes', 'primary_sponsor'],
                             list(bill_data[0].keys()))
    
