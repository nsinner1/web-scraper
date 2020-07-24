import requests
from bs4 import BeautifulSoup 

URL = 'https://en.wikipedia.org/wiki/Washington_(state)'


def get_soup(URL):
    response = requests.get(URL)
    # print(dir(response))
    content = response.content
    # print(content)
    soup = BeautifulSoup(content, 'html.parser')
    # print(soup.prettify())

    return soup


def citation_list(soup):
    citation_content = soup.find_all(class_="noprint Inline-Template Template-Fact")
    citation_text = [c.parent.parent.parent.text.replace('[citation needed]', '') for c in citation_content]
    # print(citation_text)

    return citation_text


def get_citations_needed_count(URL):
    soup = get_soup(URL)
    citations = citation_list(soup)

    return len(citations)

# print(get_citations_needed_count(URL))


def get_citations_needed_report(URL):
    soup = get_soup(URL)
    citations = citation_list(soup)
    output = ''
    for c in citations:
        output += f'Citation needed {c} \n'

    return output

# print(get_citations_needed_report(URL))


if __name__ == "__main__":
    length = get_citations_needed_count(URL)
    string = get_citations_needed_report(URL)

    print(f'Number of citations needed {length}')
    print(string)
