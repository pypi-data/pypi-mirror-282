import requests

class NekosiaAPI():
    def __init__(self):
        self.eko = 23


def cepo():
    url = 'https://example.com'
    response = requests.get(url)
    content = response.text
    return(content)