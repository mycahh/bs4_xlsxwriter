from bs4 import BeautifulSoup
import requests

URL = 'https://comparemovingprices.com/residential-move/'

def getInfo():

    request = requests.get(URL)
    htmldoc = BeautifulSoup(request.text, "html.parser")
    
    companyNames = htmldoc.select('.bck-content-toggle-front .wdc-content-slide-title')
    WrapperLinks = htmldoc.select('.bck-content-toggle-front .wdc-mce-content a')

    ListLinks = []

    for l in WrapperLinks:
        ListLinks.append(l['href'])
    
    ListLinks.insert(44, 'No tiene')
    ListLinks.insert(80, 'No tiene')
    ListLinks.insert(180, 'No tiene')
    
    FormattedInfo = []
    
    for i in range(len(companyNames)):
        FormattedInfo.append({
            'name': companyNames[i].text,
            'google_url': ListLinks[0],
            'yelp_url': ListLinks[1],
            'book_url': ListLinks[2],
            'telf': ListLinks[3]
            })
        
        del ListLinks[0:4]

    return FormattedInfo