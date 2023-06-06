#!/usr/bin/env python
# coding: utf-8

# In[13]:


import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pandas as pd

from tqdm import tqdm #


# In[14]:


options = Options()
options.add_argument('--headless') 
service = Service()
driver = webdriver.Chrome(service=service, options=options)


# In[15]:


def get_country_by_code(country_code):
    country = ''

    if(country_code == '2'): country = 'United States'
    elif(country_code == '3'): country = 'Canada'
    elif(country_code == '4'): country = 'Argentina'
    elif(country_code == '5'): country = 'Belgium'
    elif(country_code == '9'): country = 'Afghanistan'
    elif(country_code == '10'): country = 'Albania'
    elif(country_code == '11'): country = 'Andorra'
    elif(country_code == '12'): country = 'Anguilla'
    elif(country_code == '13'): country = 'Antigua/Barbuda'
    elif(country_code == '14'): country = 'Armenia'
    elif(country_code == '15'): country = 'Aruba'
    elif(country_code == '17'): country = 'Australia'
    elif(country_code == '18'): country = 'Austria'
    elif(country_code == '19'): country = 'Bahamas'
    elif(country_code == '20'): country = 'Bahrain'
    elif(country_code == '21'): country = 'Barbados'
    elif(country_code == '23'): country = 'Belize'
    elif(country_code == '24'): country = 'Bermuda'
    elif(country_code == '25'): country = 'Bolivia'
    elif(country_code == '26'): country = 'Bosnia-Herzehovina'
    elif(country_code == '27'): country = 'Brazil'
    elif(country_code == '28'): country = 'Bulgaria'
    elif(country_code == '29'): country = 'Canary Islands'
    elif(country_code == '30'): country = 'Cayman Islands'
    elif(country_code == '32'): country = 'Chile'
    elif(country_code == '33'): country = 'China'
    elif(country_code == '34'): country = 'Colombia'
    elif(country_code == '35'): country = 'Costa Rica'
    elif(country_code == '36'): country = 'Croatia'
    elif(country_code == '37'): country = 'Cuba'
    elif(country_code == '38'): country = 'Curacao'
    elif(country_code == '39'): country = 'Cyprus'
    elif(country_code == '40'): country = 'Czech Republic'
    elif(country_code == '41'): country = 'Denmark'
    elif(country_code == '42'): country = 'Dominica'
    elif(country_code == '43'): country = 'Dominican Republic'
    elif(country_code == '44'): country = 'Ecuador'
    elif(country_code == '45'): country = 'Egypt'
    elif(country_code == '46'): country = 'El Salvador'
    elif(country_code == '47'): country = 'Estonia'
    elif(country_code == '48'): country = 'Falkland Islands'
    elif(country_code == '49'): country = 'Faroe Islands'
    elif(country_code == '50'): country = 'Fiji'
    elif(country_code == '51'): country = 'Finland'
    elif(country_code == '52'): country = 'France'
    elif(country_code == '53'): country = 'Georgia'
    elif(country_code == '54'): country = 'Germany'
    elif(country_code == '55'): country = 'Gibraltar'
    elif(country_code == '56'): country = 'Greece'
    elif(country_code == '57'): country = 'Greenland'
    elif(country_code == '58'): country = 'Grenada'
    elif(country_code == '59'): country = 'Guadeloupe'
    elif(country_code == '60'): country = 'Guam'
    elif(country_code == '61'): country = 'Guatemala'
    elif(country_code == '62'): country = 'Guernsey'
    elif(country_code == '63'): country = 'Guyana'
    elif(country_code == '64'): country = 'Haiti'
    elif(country_code == '65'): country = 'Honduras'
    elif(country_code == '66'): country = 'Hong Kong'
    elif(country_code == '67'): country = 'Hungary'
    elif(country_code == '68'): country = 'Iceland'
    elif(country_code == '69'): country = 'India'
    elif(country_code == '70'): country = 'Indonesia'
    elif(country_code == '71'): country = 'Iran'
    elif(country_code == '72'): country = 'Iraq'
    elif(country_code == '73'): country = 'Ireland'
    elif(country_code == '74'): country = 'Isle of Man'
    elif(country_code == '75'): country = 'Israel'
    elif(country_code == '76'): country = 'Italy'
    elif(country_code == '77'): country = 'Jamaica'
    elif(country_code == '78'): country = 'Japan'
    elif(country_code == '79'): country = 'Jersey'
    elif(country_code == '80'): country = 'Jordan'
    elif(country_code == '81'): country = 'Kazakhstan'
    elif(country_code == '82'): country = 'Kiribati'
    elif(country_code == '84'): country = 'Kuwait'
    elif(country_code == '85'): country = 'Latvia'
    elif(country_code == '86'): country = 'Lebanon'
    elif(country_code == '87'): country = 'Liechtenstein'
    elif(country_code == '88'): country = 'Lithuenia'
    elif(country_code == '89'): country = 'Luxembourg'
    elif(country_code == '90'): country = 'Macao'
    elif(country_code == '91'): country = 'North Macedonia'
    elif(country_code == '92'): country = 'Malaysia'
    elif(country_code == '93'): country = 'Malta'
    elif(country_code == '94'): country = 'Martinique'
    elif(country_code == '95'): country = 'Mexico'
    elif(country_code == '96'): country = 'Moldova'
    elif(country_code == '97'): country = 'Monaco'
    elif(country_code == '98'): country = 'Montserrat'
    elif(country_code == '99'): country = 'Nauru'
    elif(country_code == '100'): country = 'Nepal'
    elif(country_code == '101'): country = 'Netherlands'
    elif(country_code == '102'): country = 'New Zealand'
    elif(country_code == '103'): country = 'Nicaragua'
    elif(country_code == '104'): country = 'Norway'
    elif(country_code == '105'): country = 'Oman'
    elif(country_code == '106'): country = 'Pakistan'
    elif(country_code == '107'): country = 'Panama'
    elif(country_code == '108'): country = 'Papua New Guinea'
    elif(country_code == '109'): country = 'Paraguay'
    elif(country_code == '110'): country = 'Peru'
    elif(country_code == '111'): country = 'Philippines'
    elif(country_code == '112'): country = 'Poland'
    elif(country_code == '113'): country = 'Portugal'
    elif(country_code == '114'): country = 'Puerto Rico'
    elif(country_code == '115'): country = 'Romania'
    elif(country_code == '118'): country = 'St.Kitts/Nevis'
    elif(country_code == '119'): country = 'Saint Lucia'
    elif(country_code == '120'): country = 'Saint Pierre/Miquelon'
    elif(country_code == '122'): country = 'San Marino'
    elif(country_code == '123'): country = 'Saudi Arabia'
    elif(country_code == '125'): country = 'Singapore'
    elif(country_code == '126'): country = 'Slovakia'
    elif(country_code == '127'): country = 'Slovenia'
    elif(country_code == '128'): country = 'Solomon Islands'
    elif(country_code == '129'): country = 'South Africa'
    elif(country_code == '130'): country = 'South Georgia'
    elif(country_code == '131'): country = 'Suriname'
    elif(country_code == '132'): country = 'Sweden'
    elif(country_code == '133'): country = 'Switzerland'
    elif(country_code == '134'): country = 'Taiwan'
    elif(country_code == '135'): country = 'Thailand'
    elif(country_code == '136'): country = 'Tonga'
    elif(country_code == '137'): country = 'Trinidad/Tobago'
    elif(country_code == '138'): country = 'Turkey'
    elif(country_code == '139'): country = 'Turkmenistan'
    elif(country_code == '140'): country = 'Tuvalu'
    elif(country_code == '141'): country = 'Ukraine'
    elif(country_code == '142'): country = 'United Arab Emirates'
    elif(country_code == '143'): country = 'Uruguay'
    elif(country_code == '145'): country = 'Uzbekistan'
    elif(country_code == '146'): country = 'Vanuatu'
    elif(country_code == '147'): country = 'Vatican City'
    elif(country_code == '148'): country = 'Venezuela'
    elif(country_code == '149'): country = 'Vietnam'
    elif(country_code == '151'): country = 'Yemen'
    elif(country_code == '153'): country = 'American Samoa'
    elif(country_code == '154'): country = 'St.Vincent/Grenadines'
    elif(country_code == '156'): country = 'Azerbaijan'
    elif(country_code == '157'): country = 'Mongolia'
    elif(country_code == '158'): country = 'Syria'
    elif(country_code == '159'): country = 'England'
    elif(country_code == '160'): country = 'Marshall Islands'
    elif(country_code == '162'): country = 'Scotland'
    elif(country_code == '163'): country = 'Spain'
    elif(country_code == '164'): country = 'United Kingdom'
    elif(country_code == '165'): country = 'US Virgin Islands'
    elif(country_code == '166'): country = 'Wales'
    elif(country_code == '175'): country = 'South Korea'
    elif(country_code == '176'): country = 'Kyrgyzstan'
    elif(country_code == '177'): country = 'Bangladesh'
    elif(country_code == '178'): country = 'Sudan'
    elif(country_code == '179'): country = 'Benin'
    elif(country_code == '180'): country = 'Bhutan'
    elif(country_code == '181'): country = 'Botswana'
    elif(country_code == '182'): country = 'Brunei'
    elif(country_code == '183'): country = 'Burundi'
    elif(country_code == '184'): country = 'Cambodia'
    elif(country_code == '185'): country = 'Cameroon'
    elif(country_code == '186'): country = 'Cape Verde'
    elif(country_code == '187'): country = 'Central Africa'
    elif(country_code == '188'): country = 'Chad'
    elif(country_code == '189'): country = 'Congo-Brazzaville'
    elif(country_code == '190'): country = 'Ivory Coast'
    elif(country_code == '191'): country = 'Djibouti'
    elif(country_code == '192'): country = 'Equatorial Guinea'
    elif(country_code == '193'): country = 'Gabon'
    elif(country_code == '194'): country = 'Ghata'
    elif(country_code == '195'): country = 'Kenya'
    elif(country_code == '196'): country = 'Laos'
    elif(country_code == '197'): country = 'Liberia'
    elif(country_code == '198'): country = 'Madagascar'
    elif(country_code == '199'): country = 'Morocco'
    elif(country_code == '200'): country = 'Mozambique'
    elif(country_code == '201'): country = 'Myanmar(Burma)'
    elif(country_code == '202'): country = 'Namibia'
    elif(country_code == '203'): country = 'Niger'
    elif(country_code == '204'): country = 'Nigeria'
    elif(country_code == '206'): country = 'Qatar'
    elif(country_code == '207'): country = 'Rwanda'
    elif(country_code == '208'): country = 'Samoa'
    elif(country_code == '209'): country = 'Sao Tome/Principe'
    elif(country_code == '210'): country = 'Senegal'
    elif(country_code == '211'): country = 'Sierra Leone'
    elif(country_code == '212'): country = 'Somalia'
    elif(country_code == '213'): country = 'Sri Lanka'
    elif(country_code == '214'): country = 'Swaziland'
    elif(country_code == '215'): country = 'Tajikistan'
    elif(country_code == '216'): country = 'Tanzania'
    elif(country_code == '217'): country = 'Timor-Leste'
    elif(country_code == '218'): country = 'Togo'
    elif(country_code == '219'): country = 'Tunisia'
    elif(country_code == '220'): country = 'Uganda'
    elif(country_code == '221'): country = 'Zambia'
    elif(country_code == '222'): country = 'Zimbabwe'
    elif(country_code == '223'): country = 'Algeria'
    elif(country_code == '224'): country = 'Mauritania'
    elif(country_code == '225'): country = 'International'
    elif(country_code == '231'): country = 'Serbia'
    elif(country_code == '241'): country = 'Montenegro'
    elif(country_code == '261'): country = 'Libya'
    elif(country_code == '271'): country = 'The Gambia'
    elif(country_code == '281'): country = 'Malawi'
    elif(country_code == '291'): country = 'Palestine'
    elif(country_code == '301'): country = 'Ethiopia'
    elif(country_code == '311'): country = 'Mauritius'
    elif(country_code == '312'): country = 'Lesotho'
    elif(country_code == '313'): country = 'Mali'
    elif(country_code == '314'): country = 'Maldives'
    elif(country_code == '315'): country = 'Catalonia'
    elif(country_code == '316'): country = 'Galicia'
    elif(country_code == '317'): country = 'Kosovo'
    elif(country_code == '318'): country = 'DR Congo'
    elif(country_code == '319'): country = 'Angola'
    elif(country_code == '320'): country = 'Comoros'
    elif(country_code == '321'): country = 'Eritrea'
    elif(country_code == '322'): country = 'Guinea'
    elif(country_code == '323'): country = 'Guinea-Bissau'
    elif(country_code == '324'): country = 'Micronesia'
    elif(country_code == '325'): country = 'North Korea'
    elif(country_code == '326'): country = 'Palau'
    elif(country_code == '327'): country = 'Seychelles'
    elif(country_code == '328'): country = 'Western Sahara'
    elif(country_code == '329'): country = 'British Virgin Islands'
    elif(country_code == '330'): country = 'South Sudan'
    elif(country_code == '332'): country = 'Basque Country'
    elif(country_code == '333'): country = 'New Caledonia'
    elif(country_code == '334'): country = 'Burkina Faso'
    elif(country_code == '335'): country = 'Reunion'
    elif(country_code == '336'): country = 'Aland Islands'
    elif(country_code == '337'): country = 'French Guiana'
    elif(country_code == '338'): country = 'Mayotte'
    elif(country_code == '339'): country = 'Sint Maarten'
    elif(country_code == '340'): country = 'Turks and Caicos Islands'
    elif(country_code == '350'): country = 'French Polynesia'
    elif(country_code == '351'): country = 'European Union'
    elif(country_code == '352'): country = 'Niue'
    elif(country_code == '353'): country = 'Chinese Taipei'
    elif(country_code == 'sanctioned" href="/blog/CHESScom/on-the-invasion-of-ukraine" target="_blank'): country = 'Russia'
    else: country = ''
        
    return country


# In[18]:


category = input('category(blitz,rapid,etc.):')
players_number = int(input('players_number(min-100,max-500k):'))
page = 1
pbar = tqdm(total=(players_number)) #
while True:
    titles = []
    usernames = []
    names = []
    rates = []
    countries = []
    wons = []
    draws = []
    losts = []
    won_percents = []
    draw_percents = []
    lost_percents = []
    
    if category == 'blitz':
        if page == 1: url = 'https://www.chess.com/leaderboard/live?'
        else: url = f'https://www.chess.com/leaderboard/live?page={page}'
    else:
        if page == 1: url = f'https://www.chess.com/leaderboard/live/{category}'
        else: url = f'https://www.chess.com/leaderboard/live/{category}?page={page}'
    
    driver.get(url)

    driver.implicitly_wait(60)

    html_content = driver.page_source

    data = BeautifulSoup(html_content, 'html.parser').decode("utf-8")

    l = data.split('<div class="user-tagline-component"')

    for i in range(1,len(l)):
        title = l[i].partition('user-chess-title-component">\n                  ')[2].partition('\n')[0]

        name_username = l[i].partition('user-tagline-username" href="/member/')[2].partition('<!-- -->')[0]

        username = name_username.partition('">\n')[0]
        name = name_username.partition('">\n                  ')[2].partition('\n')[0]
        
        rate = l[i].partition(f'/stats/live/{category}/')[2].partition('<!-- -->\n                ')[2].partition('\n')[0]
        
        country_code = l[i].partition('flags-component country-')[2].partition('">\n')[0]
        country = get_country_by_code(country_code)
        
        stats = l[i].partition('leaderboard-row-stats">\n                 ')[2]
        
        won = stats.partition(' /')[0]
        draw = stats.partition(' / ')[2].partition(' / ')[0]
        lost = stats.partition(' / ')[2].partition(' / ')[2].partition('\n')[0]

        won_percent = stats.partition('class="won">\n                  ')[2].partition('%\n')[0]
        draw_percent = stats.partition('class="draw">\n                  ')[2].partition('%\n')[0]
        lost_percent = stats.partition('class="lost">\n                  ')[2].partition('%\n')[0]

        titles.append(title)
        usernames.append(username)
        names.append(name)
        rates.append(rate)
        countries.append(country)
        wons.append(won)
        draws.append(draw)
        losts.append(lost)
        won_percents.append(won_percent)
        draw_percents.append(draw_percent)
        lost_percents.append(lost_percent)
        
    df_add = pd.DataFrame({
        'title': titles,
        'username': usernames,
        'name': names,
        'rate': rates,
        'country': countries,
        'won': wons,
        'draw': draws,
        'lost': losts,
        'won_percent': won_percents,
        'draw_percent': draw_percents,
        'lost_percent': lost_percents
    })
    
    if len(df_add) == 50:
        if page != 1:
            df_all = pd.read_csv(f'players_{category}.csv', low_memory=False)
            df = pd.concat([df_all,df_add])
            df = df.reset_index(drop=True)
            df.to_csv(f'players_{category}.csv', index=False)
            
            players = df.drop_duplicates(subset='username').reset_index(drop=True)
            if players_number <= len(players):
                players = players.iloc[0:players_number]
                games = players.won.astype(int)+players.draw.astype(int)+players.lost.astype(int)
                players = pd.DataFrame({
                    'title': players.title,
                    'username': players.username,
                    'name': players.name,
                    'rate': players.rate,
                    'country': players.country,
                    'games': games,
                    'won': players.won,
                    'draw': players.draw,
                    'lost': players.lost,
                    'won_percent': players.won_percent,
                    'draw_percent': players.draw_percent,
                    'lost_percent': players.lost_percent
                })
                players.to_csv(f'players_{category}.csv', index=False)
                break
        else:
            df_add.to_csv(f'players_{category}.csv', index=False)
        page += 1
        pbar.update(50) #
    else:
        continue
pbar.update(50) #
pbar.close() #
print(f'players_{category}.csv file with {players_number} players was created!') #
#pd.read_csv(f'players_{category}.csv', low_memory=False)


# In[ ]:




