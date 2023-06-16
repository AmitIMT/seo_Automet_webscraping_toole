import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Enter the URL of your webpage here:
url = 'https://theappsolutions.com/'

# Make a GET request to fetch the webpage content:
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Extract meta tags from the page content:
meta_tags = soup.find_all('meta')
meta_dict = {}
for tag in meta_tags:
    if tag.has_attr('name'):
        name = tag.attrs['name']
        value = tag.attrs['content']
        meta_dict[name] = value

# Print all meta tags found on the page:
print(meta_dict)

# Use regular expressions to find specific keywords on the page:
keywords_regex1 = r'<\s*title[^>]*>(.*?)<\s*/\s*title\s*>'
keywords_regex2= r'name="description" content="(.*?)"'
keywords_regex3= r'name="keywords" content="(.*?)"'

title_matcher=re.compile(keywords_regex1,re.IGNORECASE|re.DOTALL)
desc_matcher=re.compile(keywords_regex2,re.IGNORECASE|re.DOTALL)
kw_matcher=re.compile(keywords_regex3,re.IGNORECASE|re.DOTALL)

title_match = title_matcher.search(str(soup))
title = title_match.group(1).strip() if title_match else ""
desc_match = desc_matcher.search(str(soup))
desc = desc_match.group(1).strip() if desc_match else ""
kw_match = kw_matcher.search(str(soup))
keywords = kw_match.group(1).strip() if kw_match else ""

# Print the keywords found on the page:
print('Title:', title)
print('Description:', desc)
print('Keywords:', keywords)

# Create a CSV file to store all meta tags and keywords:
data = {'Meta Tag': list(meta_dict.keys()), 'Content': list(meta_dict.values())}
df = pd.DataFrame(data)
df.to_csv('seo_data.csv', index=False)

