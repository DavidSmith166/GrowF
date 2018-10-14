import requests
import json


class GoldmanAPI:
    client_id = r'7df56d72cc914bba925b8792e261b0b3'
    client_secret = r'e0ced1370eccb3c329f89cb1a27fc64280b7e239c9a8b330911afdbde41864f8'

    auth_data = {
        'grant_type'    : 'client_credentials',
        'client_id'     : client_id,
        'client_secret' : client_secret,
        'scope'         : 'read_content read_financial_data read_product_data read_user_profile'
    }

    def __enter__(self):
        # create session instance
        self.session = requests.Session()

        # make a POST to retrieve access_token
        auth_request = self.session.post('https://idfs.gs.com/as/token.oauth2', data=self.auth_data)
        access_token_dict = json.loads(auth_request.text)
        access_token = access_token_dict['access_token']

        # update session headers
        self.session.headers.update({'Authorization':'Bearer '+ access_token})

    def test_connectivity(self):
        # test API connectivity
        request_url = 'https://api.marquee.gs.com/simple-api-test/v1/test'
        request = self.session.get(url=request_url)
        print(request.text)

    def __exit__(self, *args, **kwargs):
        self.session.close()

    def __init__(self):
        self.test_connectivity()


def get_ranking_info():
    pass
