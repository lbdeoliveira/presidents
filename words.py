import requests
from bs4 import BeautifulSoup

def get_speech(url):
    '''
    Returns a tuple of president name and speech text for a given url for UVA Miller Center collection of presidential speeches.
    https://millercenter.org/the-presidency/presidential-speeches
    '''
    # get html
    r = requests.get(url)
    html_text = r.text
    
    # extract president name and speech text
    soup = BeautifulSoup(html_text, 'lxml')
    speech = soup.find('div', class_='view-transcript').get_text()
    president = soup.find('p', class_='president-name').get_text()
    
    # remove leading 'Transcript' and replace newlines with spaces in speech:
    if speech[:10] == 'Transcript':
        speech = speech[10:]
    speech = speech.replace('\n', ' ').strip()
    
    return president, speech
