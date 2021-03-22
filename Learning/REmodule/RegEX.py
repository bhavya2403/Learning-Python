import re

mystr = '''Nakamura started 2020 as the top-ranked blitz chess player in the world. Due to the COVID-19 pandemic, chess moved online, with Nakamura playing an important role in popularizing it.[110]
Since April 2020, Nakamura participated in the Magnus Carlsen Chess Tour with a prize pool of $1 million.[111] He won the group stage of Magnus Carlsen Invitational and finished second behind Magnus Carlsen. He beat Carlsen in the semi-finals of Lindores Abbey Rapid Challenge and also finished second. Nakamura made it to the Magnus Carlsen Chess Tour Finals against Carlsen where he took his opponent to seven matches before drawing an armageddon tie breaker game as white, losing the match. Nakamura mentioned that he had decided earlier that he wouldn't make an attempt to "flag" in order to secure a win if he ended up in a drawing scenario in the armageddon match. The world champion praised Nakamura after the match, saying "he played a great match, he made it extremely difficult for me".[112]
In September, Nakamura tied for 1st with Carlsen in Champions Showdown(81539-76915): Chess 9LX[113] and finished 3rd in St. Louis Rapid & Blitz.[114]
After a number of victories in shorter tournaments on Chess.com, including Titled Tuesday[115] and Super Swiss,[116] Nakamura failed to defend his U.S. Chess Champion title, finishing 7th. The tournament, which took place online in a rapid format, was won by Wesley So.[117]
In October, Nakamura held a 77 board charity simultaneous exhibition online, raising around $ 9,500 for Doctors Without Borders.[118] Before the 2020 United States presidential election, he challenged President Barack Obama to a game of chess to raise funds for the presidential nominee Joe Biden’s victory fund and ActBlue.[119] He also streamed on Twitch in support of the I Will Vote campaign.[120]
Nakamura won the Chess.com Speed Chess Championship in December. It was his third victory in the format. The site had promoted the knockout tournament by emphasizing a possible rematch of Nakamura and world champion Magnus Carlsen in the final. However, French grandmaster Maxime Vachier-Lagrave defeated Carlsen in their semi-final match. Nakamura then defeated Vachier-Lagrave by a score of 18.5-12.5 in the final. His skill at bullet chess proved to be the deciding factor, as he beat Vachier-Lagrave 8-3 in the bullet section of the match. Previous to the final Nakamura had defeated grandmasters Haik Martirosyan 21-5, Vladimir Fedoseev 21.5-5.5, and Wesley So'''

# pattern = re.compile(r'Naka') # r'' means raw string(doen't escape escape characters)
# pattern = re.compile(r'.') # here . means any character
# pattern = re.compile(r'.mura')
# pattern = re.compile(r'^Naka') # return if string starts with Naka
# pattern = re.compile(r'So$') # return if string ends with So
# pattern = re.compile(r'er*') # any number of word 'r' after e
# pattern = re.compile(r'er+') # any(1 or more) number of word 'r' after e
# pattern = re.compile(r'er{2}') # two 'r' after e means word 'err'
# pattern = re.compile(r'er|Naka') # either 'er' or 'Naka'
# pattern = re.compile(r'\Ashow') # same as ^
# pattern = re.compile(r'\bShow') # returns if word starts with given chars
# pattern = re.compile(r'down\b') # returns if word ends with given chas
# pattern = re.compile(r'\d{5}-\d{5}') # returns if 5digits-5digits

matches = pattern.finditer(mystr)
for match in matches:
    print(match)