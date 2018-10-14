import requests
import json
from api.yahoo import get_past_date
from api.models import Stock

class GoldmanAPI:

    def __init__(self):
        self.client_id = r'7df56d72cc914bba925b8792e261b0b3'
        self.client_secret = r'e0ced1370eccb3c329f89cb1a27fc64280b7e239c9a8b330911afdbde41864f8'

        self.auth_data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': 'read_content read_financial_data read_product_data read_user_profile'
        }

        #self.url = 'https://api.marquee.gs.com/v1/data/USCANFPP_MINI/query'
        self.url = 'https://api.marquee.gs.com/v1/assets/data/query'
        #self.bulk_url = "https://api.marquee.gs.com/v1/data/last/query/bulk"

    def __enter__(self):
        # create session instance
        self.session = requests.Session()

        # make a POST to retrieve access_token
        auth_request = self.session.post('https://idfs.gs.com/as/token.oauth2', data=self.auth_data)
        access_token_dict = json.loads(auth_request.text)
        access_token = access_token_dict['access_token']

        # update session headers
        self.session.headers.update({'Authorization':'Bearer '+ access_token})
        print(self.test_connectivity())
        return self

    def test_connectivity(self):
        # test API connectivity
        request_url = 'https://api.marquee.gs.com/simple-api-test/v1/test'
        request = self.session.get(url=request_url)
        return(request.text)

    def __exit__(self, *args, **kwargs):
        self.session.close()

    def get_ranking_info(self):
        past_date = get_past_date(365)
        end_date = get_past_date(0)
        tickers = [stock.ticker for stock in Stock.objects.all()]
        """
        request = {
            'startDate': past_date,
            'endDate': end_date,
            'where': {
                'ticker': tickers,
            },
        }
        """
        request = {
            "where": {
                "gsid": ["10516", "10696", "11308", "11896", "13901"]
            },
            "fields": ["gsid", "ticker", "name"],
        }
        from pprint import pprint
        #print(json.dumps(request))
        response = self.session.post(url=self.url, json=request)
        #not working url = 'https://api.marquee.gs.com/v1/data'
        #response = self.session.get(url=self.url)
        return response.text
