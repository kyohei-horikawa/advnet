import requests
from bs4 import BeautifulSoup
import random


def synonym(words):
    results = []
    if len(words) > 2:
        words = [words[0], words[1]]
    print(words)

    for word in words:
        print(word[0])
        res = requests.get(f'https://renso-ruigo.com/word/{word[0]}')
        soup = BeautifulSoup(res.text, 'html.parser')

        ans = []
        for div in soup.findAll('div'):
            if 'id' in div.attrs:
                if 'ruigogun_paragraph' in div.attrs['id']:
                    for a in div.findAll('a'):
                        ans.append(a.string)

            if 'class' in div.attrs:
                for class_ in div.attrs['class']:
                    if 'word_t_field' in class_:
                        for a in div.findAll('a'):
                            ans.append(a.string)

        if len(ans) == 0:
            results.append(word[0])
        else:
            results.append(random.choice(ans))

    return results
