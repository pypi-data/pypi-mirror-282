import unittest
from auraflow_client.api import get_data


class TestAPI(unittest.TestCase):
    def test_get_data(self):
        dummy_api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmRlcl9pZCI6IkdVR1Y2WjVLV0ciLCJhcGlfc2VjcmV0IjoiNmMxM2M3MWYtNDdhYi00OThlLTg1YjktYzcxYjk5NGJmNGM4In0.51FNSG02kwVT1-Uw60nEL7oHu4X9JNoprN4sRrEriRQ'
        body = {
            'ticker_list': ['^GSPC'],
            "start": '2020-01-01',
            "end": '2023-01-01',
            "source": 'yahoo',
            "data_format": 'json'
        }

        response = get_data(dummy_api_key, body)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
