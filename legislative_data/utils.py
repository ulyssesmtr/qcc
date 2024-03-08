import csv


def read_csv(file_name):
    """
    Opens and reads a csv file.
    Formats the file content into a list of dictionaries.
    """
    with open(file_name, newline='') as csvfile:
        content = csv.reader(csvfile)
        header = next(content)
        data_list = [{header[col]: data for col, data in enumerate(row)} for row in content]
    return data_list


def calc_votes(vote_result_array, key):
    """
    Counts the votes in favor and in opposition for the 'key'
    parameter. This parameter can be either 'legislator_id' 
    or 'vote_id'. 
    In the case it is 'legislator_id', it will
    return a dictionary where the key:value pair will be 
    'legislator_id': {"1": votes_in_favor_count, "2": votes_in_opposition_count}
    """
    vote_results_dict = {}
    for vr in vote_result_array:
        # If the key does not exist in the dictionary, set it with the default value of {"1": 0, "2": 0} and returns it
        # if it does, returns the current key value
        vote_count = vote_results_dict.setdefault(vr.get(key), {"1": 0, "2": 0})
        vote_count[vr.get('vote_type')] += 1
    return vote_results_dict


def get_legislator_data():
    """
    Returns a list of dictionaries containing information on
    how many votes in favor and in opposition each legislator voted for.
    """
    legislators = read_csv('legislative_data/csvs/legislators.csv')
    vote_results = read_csv('legislative_data/csvs/vote_results.csv')
    # Retrieves a dict containing the amount of votes in favor and in opposition casted by each legislator
    vote_results_dict = calc_votes(vote_results, 'legislator_id')
    legislator_bill_votes = [
        {
            "legislator_id": legislator.get('id'),
            "legislator_name": legislator.get('name'),
            "yea_votes": vote_results_dict.get(legislator.get('id'), {}).get('1', 0),
            "nay_votes": vote_results_dict.get(legislator.get('id'), {}).get('2', 0),
        } for legislator in legislators]
    
    return legislator_bill_votes


def get_bill_data():
    bills = read_csv('legislative_data/csvs/bills.csv')
    vote_results = read_csv('legislative_data/csvs/vote_results.csv')
    votes = read_csv('legislative_data/csvs/votes.csv')
    legislators = read_csv('legislative_data/csvs/legislators.csv')
    # Retrieves a dict containing the amount of votes in favor and in opposition for each bill's vote
    vote_results_dict = calc_votes(vote_results, 'vote_id')
    # Formats the legislator list of dicts, allowing the legislator name to be retrievable by id
    legislator_dicts = {legislator.get('id'): legislator.get('name') for legislator in legislators}
    # Formats the votes array in to a dict that relates each bill to all its possible votes
    # In this example each bill has only one vote, but converting it in this way
    # allows it to be expanded in the future, in the case there are more votes
    # for each bill and there is the need to display this data for every vote, instead of every bill.
    votes_dict = {}
    for vote in votes:
        votes_dict.setdefault(vote.get('bill_id'), []).append(vote.get('id'))
    bill_data = [
        {
            'id': bill.get('id'),
            'title': bill.get('title'),
            'yea_votes': vote_results_dict.get(votes_dict.get(bill.get('id'))[0]).get('1', 0),
            'nay_votes': vote_results_dict.get(votes_dict.get(bill.get('id'))[0]).get('2', 0),
            'primary_sponsor': legislator_dicts.get(bill.get('sponsor_id'), 'Not Found')  
        } for bill in bills]

    return bill_data



