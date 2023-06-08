import requests

class JumpPediaAPI:
    def __init__(self, base_url='http://localhost:5000'):
        self.base_url = base_url

    def retrieve_all_jump_levels(self):
        url = f'{self.base_url}/api/jumps'
        response = requests.get(url)
        return response.json()

    def filter_jump_levels(self, filter_criteria):
        url = f'{self.base_url}/api/jumps'
        response = requests.post(url, json=filter_criteria)
        return response.json()
