# liquipediapy
> api for liquipedia.net 

## Contents
- [Installation](#install)
- [Examples](#examples)
- [API](#api)
- [Contributing](#cb)
- [Author](#author)
- [License](#ls)
- [Notes](#notes)

<a name="install"></a>
## Install 

```pip install liquipediapy```

Please refer to [liquipedia's terms of use](https://liquipedia.net/api-terms-of-use) for rate-limiting information. 

<a name="examples"></a>
## Examples
The [examples](https://github.com/c00kie17/liquipediapy/tree/master/examples) directory contains an example files on how to interact with the each class.

<a name="api"></a>
## API
- [liquipediapy](#liquipediapy_obj)
  - [parse](#liquipediapy_parse)
  - [dota2webapi](#liquipediapy_dota2webapi)
  - [search](#liquipediapy_search)
- [dota](#dota)
  - [get_players](#dota_get_players)
  - [get_player_info](#dota_get_player_info)
  - [get_teams](#dota_get_teams)
  - [get_team_info](#dota_get_team_info)
  - [get_transfers](#get_transfers)
  - [get_upcoming_and_ongoing_games](#dota_get_upcoming_and_ongoing_games)
  - [get_heros](#dota_get_heros)
  - [get_items](#dota_get_items)
  - [get_patches](#dota_get_patches)
  - [get_tournaments](#dota_get_tournaments)
  - [get_tournament_baner](#dota_get_tournament_baner)
  - [get_pro_circuit_details](#dota_get_pro_circuit_details)
- [counterstrike](#counterstrike) 
  - [get_players](#counterstrike_get_players)
  - [get_teams](#counterstrike_get_teams)
  - [get_player_info](#counterstrike_get_player_info)
  - [get_team_info](#counterstrike_get_team_info) 
  - [get_transfers](#counterstrike_get_transfers) 
  - [get_upcoming_and_ongoing_games](#counterstrike_get_upcoming_and_ongoing_games) 
  - [get_tournaments](#counterstrike_get_tournaments) 
  - [get_weapons](#counterstrike_get_weapons) 
  - [get_weapon_info](#counterstrike_get_weapon_info) 
  - [get_statistics](#counterstrike_get_statistics) 
  - [get_patches](#counterstrike_get_patches) 
- [smash](#smash) 
  - [get_players](#smash_get_players) 
  - [get_player_info](#smash_get_player_info) 
  - [get_teams](#smash_get_teams) 
  - [get_team_info](#smash_get_team_info)
  - [get_transfers](#smash_get_transfers) 
  - [get_tournaments](#smash_get_tournaments)
  
<a name="liquipediapy_obj"></a>  
#### liquipediapy(appname,game)
create a liquipediapy object

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| appname | <code>string</code> | The name for your app, you can refer to the [liquipedia's terms of use](https://liquipedia.net/api-terms-of-use) for more information |
| game | <code>string</code> | name of the game you want to create the object for |
| debug_folder | <code>string</code> | (Optionnal) Path of the debug folder where you want to store html pages (and read back from it)|

##### example
```python
from liquipediapy import liquipediapy

liquipy_object = liquipediapy('appname')
liquipy_object = liquipediapy('appname', 'dota2')
liquipy_object = liquipediapy('appname', 'smash', "F:\\Path\\To\\Debug\\Folder\\")
```
***
<a name="liquipediapy_parse"></a>  
#### parse(page)
parses a given page
[example](https://liquipedia.net/dota2/api.php?action=parse&page=arteezy)
##### parameters
| Param | Type | Description |
| --- | --- | --- |
| page | <code>string</code> | name of the page you want to parse |


##### response
| Return | Type | Description |
| --- | --- | --- |
| soup | <code>bs4 Object</code> | a [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) object  |
| redirect_value | <code>string</code> | if the page has been redirected then returns page value it was redirected to, orderwise returns ```None``` |

##### example
```python
soup,url = liquipediapy_object.parse('arteezy')
```
***

<a name="liquipediapy_dota2webapi"></a>  
#### dota2webapi(matchId)
returns match details for a given dota2 match, only works if ```game``` value in contructor is set to ```dota2```

[example](https://liquipedia.net/dota2/api.php?action=dota2webapi&matchid=4225454337&data=picks_bans%7Cplayers%7Ckills_deaths|duration|radiant_win|teams|start_time&format=json)

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| matchId | <code>string</code> | ID of the match you want details for  |


##### response
| Return | Type | Description |
| --- | --- | --- |
| match_details | <code>json</code> | match_details if valid matchID otherwise an error in json  |


##### example
```python
match_details = liquipediapy_object.dota2webapi('4225454337')
```
***


<a name="liquipediapy_search"></a>  
#### search(serach_value)
searchs liquipedia.net for a given term
[example](https://liquipedia.net/dota2/api.php?action=opensearch&format=json&search=mid)

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| serach_value | <code>string</code> | search term |


##### response
| Return | Type | Description |
| --- | --- | --- |
| search_result | <code>json</code> | response |

##### example
```python
search_result = liquipediapy_object.search('mar')
```
***
<a name="dota"></a>  
#### dota(appname)
create a dota object

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| appname | <code>string</code> | The name for your app, you can refer to the [liquipedia's terms of use](https://liquipedia.net/api-terms-of-use) for more information |

##### example
```python
from liquipediapy import dota

dota_obj = dota("appname")
```
***


<a name="dota_get_players"></a>  
#### get_players()
returns all dota players from [Portal:Players](https://liquipedia.net/dota2/Portal:Players)

##### response
````python
[{'country': 'Russia', 'ID': '.Ark', 'Name': 'Egor Zhabotinskii', 'Team': '', 'Links': {'twitter': 'https://twitter.com/just_Ark', 'vk': 'http://vk.com/wtfkaelownage'}},...,{'country': 'China', 'ID': '小郭嘉', 'Name': 'Zhan Yaoyang', 'Team': '', 'Links': {}}, {'country': 'China', 'ID': '闷油瓶', 'Name': 'Wang Liang', 'Team': '', 'Links': {}}]
````
##### example
```python
players = dota_obj.get_players()
```
***


<a name="dota_get_player_info"></a>  
#### get_player_info(playerName,results)
gets information for a specified player

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| playerName | <code>string</code> | name of player |
| results | <code>bool</code> | if you want to parse the results page for the player, defauls to ```False``` |


##### response
````python
{'info': {'image': 'https://liquipedia.net/commons/images/thumb/f/f2/Miracle_SL_i-League.jpg/600px-Miracle_SL_i-League.jpg', 'name': 'عامر البرقاوي', 'romanized_name': 'Amer Al-Barkawi', 'birth_details': 'June 20, 1997 (1997-06-20) (age21)', 'country': ['Jordan', 'Poland'], 'status': 'Active', 'team': 'Team Liquid', 'roles': ['Solo Middle', 'Carry'], 'signature_heros': ['Invoker', 'Anti Mage', 'Shadow Fiend'], 'earnings': 3668824, 'ranking': {'rank': '10', 'points': 3120}}, 'links': {'dotabuff': 'https://www.dotabuff.com/esports/players/105248644',...,'steamcommunity': 'https://steamcommunity.com/profiles/76561198065514372'}, 'history': [{'duration': '2015-01-01 — 2015-04-02', 'name': 'Balkan Bears'},...{'duration': '2016-09-16 — Present', 'name': 'Team Liquid'}], 'achivements': [{'Date': '2018-08-24', 'Placement': '44', 'LP Tier': 'Premier', 'Tournament': 'The International 2018', 'Team': 'Team Liquid', 'Results': '0:2', 'opponent': 'Evil Geniuses', 'Prize': '$1,787,252'},...{'Date': '2015-11-21', 'Placement': '11', 'LP Tier': 'Premier', 'Tournament': 'The Frankfurt Major 2015', 'Team': 'OG', 'Results': '3:1', 'opponent': 'Team Secret', 'Prize': '$1,110,000'}], 'results': [{'Date': '2018-11-30', 'Placement': '22', 'LP Tier': 'Qualifier', 'Tournament': 'The Chongqing Major Europe Qualifier', 'Team': 'Team Liquid', 'Results': '2:1', 'opponent': 'Alliance', 'Prize': '$0'},...{'Date': '2015-01-21', 'Placement': '55 - 8', 'LP Tier': 'Minor', 'Tournament': 'Esportal Dota 2 League Open Tournament 2', 'Team': 'Balkan Bears', 'Results': '1:2', 'opponent': 'MYinsanity', 'Prize': '$0'}]}
````
##### example
```python
player_details = dota_obj.get_player_info('Miracle-',True)
```
***


<a name="dota_get_teams"></a>
#### get_teams()
return all active and inactive teams from Portal:Teams

##### response
````python
['Cyber Legacy', 'Effect',....,'FlyToMoon', 'ForZe']
````

##### example
````python
teams = dota_obj.get_teams()
````
***

<a name="dota_get_team_info"></a>  
#### get_team_info(teamName,results)
gets information for a specified team

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| teamName | <code>string</code> | name of the team |
| results | <code>bool</code> | if you want to parse the results page for the team, defauls to ```False``` |


##### response
```python
{'info': {'image': 'https://liquipedia.net/commons/images/thumb/7/7e/Team_Liquid_2020.png/600px-Team_Liquid_2020.png', 'location': ['Netherlands', 'Europe'], 'region': 'Europe', 'coach': 'Blitz', 'director': 'Steve Arhancet Nazgul', 'manager': 'Elya', 'team captain': 'iNSaNiA', 'sponsor': ['Marvel', 'Monster Energy', 'Alienware', 'SAP', 'Honda', 'HyperX', 'Secretlab', 'Twitch', "Jersey Mike's", 'Huya 虎牙直播'], 'earnings': 22991558, 'created': '2000-??-?? 2012-12-06'}, 'links': {'teamliquid': 'https://www.teamliquid.com/', 'liquiddota': 'https://www.liquiddota.com/forum/players-and-teams/495594-team-liquid-discussion', 'facebook': 'https://facebook.com/teamliquid', 'vk': 'https://vk.com/teamliquidpro', 'twitch': 'https://www.twitch.tv/team/teamliquid', 'twitter': 'https://twitter.com/teamliquid', 'weibo': 'https://weibo.com/teamliquid', 'youtube': 'https://www.youtube.com/Team_Liquid', 'instagram': 'https://www.instagram.com/teamliquid', 'dotabuff': 'https://www.dotabuff.com/esports/teams/2163', 'datdota': 'https://www.datdota.com/teams/2163'}, 'cups': ['RaidCall Dota 2 League Season 2', 'EPICENTER 2016', 'StarLadder i-League StarSeries Season 3', 'StarLadder i-League Invitational Season 2', 'EPICENTER 2017', 'The International 2017', 'China Dota2 Supermajor', 'ESL One Germany 2020'], 'team_roster': [{'ID': 'miCKe', 'Name': 'Michael Vu', 'Position': '1', 'Join Date': '2019-10-02'}, {'ID': 'qojqva', 'Name': 'Maximilian Bröcker', 'Position': '2', 'Join Date': '2019-10-02'}, {'ID': 'Boxi', 'Name': 'Samuel Svahn', 'Position': '3', 'Join Date': '2019-10-02'}, {'ID': 'Taiga', 'Name': 'Tommy Le', 'Position': '4', 'Join Date': '2019-10-02'}, {'ID': 'iNSaNiA', 'Name': 'Aydin Sarkohi', 'Position': '5', 'Join Date': '2019-10-02'}]} ````
```
##### example
```python
team_details = dota_obj.get_team_info('Team Liquid',True)
```
***


<a name="get_transfers"></a>  
#### get_transfers()
gets all transfers from [Portal:Transfers](https://liquipedia.net/dota2/Portal:Transfers)



##### response
````python
[{'Date': '2018-12-03', 'Player': ['Moogy', 'Inflame'], 'Previous': 'Newbee', 'Current': 'Newbee'},...{'Date': '2018-09-10', 'Player': ['Fenrir'], 'Previous': 'Vici Gaming', 'Current': 'Team Aster'}]
````
##### example
```python
transfers = dota_obj.get_transfers()
```
***

<a name="dota_get_upcoming_and_ongoing_games"></a>  
#### get_upcoming_and_ongoing_games()
gets all matches from [Liquipedia:Upcoming_and_ongoing_matches](https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches)



##### response
````python
[{'team1': 'B8', 'format': 'Bo3', 'team2': 'EXTREMUM', 'start_time': 'January 11, 2021 - 10:00 UTC', 'tournament': 'ESL One CIS Online Season 1: Decider Tournament', 'tournament_short_name': 'ESL One CIS S1: Decider', 'twitch_channel': None},...,{'team1': 'NoPangolier', 'format': 'Bo3', 'team2': 'Winstrike Team', 'start_time': 'January 11, 2021 - 13:00 UTC', 'tournament': 'ESL One CIS Online Season 1: Decider Tournament', 'tournament_short_name': 'ESL One CIS S1: Decider', 'twitch_channel': None}]
````
##### example
```python
games = dota_obj.get_upcoming_and_ongoing_games()
```
***

<a name="dota_get_heros"></a>  
#### get_heros()
gets all heros from [Portal:Heroes](https://liquipedia.net/dota2/Portal:Heroes)



##### response
````python
[{'image': 'https://liquipedia.net/commons/images/thumb/f/fa/Abaddon_Large.png/125px-Abaddon_Large.png', 'name': 'Abaddon'},...,{'image': 'https://liquipedia.net/commons/images/thumb/9/91/Zeus_Large.png/125px-Zeus_Large.png', 'name': 'Zeus'}]
````
##### example
```python
heros = dota_obj.get_heros()
```
***

<a name="dota_get_items"></a>  
#### get_items()
gets all items from [Portal:Items](https://liquipedia.net/dota2/Portal:Items)



##### response
````python
[{'image': 'https://liquipedia.net/commons/images/thumb/c/cd/Animal_Courier.png/60px-Animal_Courier.png', 'name': 'Animal Courier', 'price': '50'},...,{'image': 'https://liquipedia.net/commons/images/thumb/e/  e8/Ring_of_Aquila.png/60px-Ring_of_Aquila.png', 'name': 'Ring of Aquila', 'price': '985'}]
````
##### example
```python
items = dota_obj.get_items()
```
***

<a name="dota_get_patches"></a>  
#### get_patches()
gets all patches from [Portal:Patches](https://liquipedia.net/dota2/Portal:Patches)



##### response
````python
[{'Version': '7.20c', 'Release Date': '2018-11-24', 'Highlights': ['Balance Changes']},...,{'Version': '0.60', 'Highlights': ['Ported the following heroes:', ' Chen', ' Crystal Maiden', ' Death Prophet', ' Doom', ' Drow Ranger', ' Faceless Void', ' Lich', ' Lina', ' Lion', ' Magnus', " Nature's Prophet", ' Nyx Assassin', ' Pugna', ' Queen of Pain', ' Razor', ' Riki', ' Shadow Shaman', ' Silencer', ' Slardar', ' Sven', ' Vengeful Spirit', ' Venomancer', ' Viper', ' Visage', ' Wraith King']}]
````
##### example
```python
patches = dota_obj.get_patches()
```
***


<a name="dota_get_tournaments"></a>  
#### get_tournaments(type)
gets all tournaments from [Portal:Tournaments](https://liquipedia.net/dota2/Portal:Tournaments)

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| type | <code>string</code> | type of tournaments , defaults to ```None``` , accepted values are ```Tier 1``` ,```Tier 2```, ```Tier 3```, ```Tier 4```, ```Qualifier```, ```Monthly```, ```Weekly```, ```Show Matches```|

##### response
````python
[{'tier': 'Qualifier', 'name': 'DreamLeague Season 14 DPC EU Decider Tournament', 'icon': 'https://liquipedia.net/commons/images/9/96/Dreamleague_logo_small.png', 'page': 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/1/Europe/Decider_Tournament', 'dates': 'Jan 07 - 10, 2021', 'prize_pool': 0, 'teams': '8', 'host_location': 'Europe', 'winner': 'TBD', 'runner_up': 'TBD'},...,{'tier': 'Tier 4', 'name': 'Moscow Esports 2020 S2 Superfinal', 'icon': 'https://liquipedia.net/commons/images/b/b6/Moscowesport.png', 'page': 'https://liquipedia.net/dota2/Moscow_Esports/7', 'dates': 'Dec 19 - 20, 2020', 'prize_pool': 2039, 'teams': '16', 'host_location': 'Russia', 'winner': 'Blstrbl', 'runner_up': 'NP'}]
````
##### example
```python
tournaments = dota_obj.get_tournaments()
```
***


<a name="dota_get_tournament_baner"></a>  
#### get_tournament_baner(url)
gets baner url from tournament page

##### parameters
| Param | Type |
| --- | --- |
| url | <code>string</code> | 

##### response
````python
'https://liquipedia.net/commons/images/thumb/0/0b/IeSF_2020.png/600px-IeSF_2020.png'
````
##### example
```python
tournaments = dota_obj.get_tournament_baner('https://liquipedia.net/dota2/IeSF_World_Championship/2020')
```
***


<a name="dota_get_pro_circuit_details"></a>  
#### get_pro_circuit_details()
returns pro circuit [rankings](https://liquipedia.net/dota2/Dota_Pro_Circuit/2018-19/Rankings) and [schedule](https://liquipedia.net/dota2/Dota_Pro_Circuit/2018-19/Schedule)



##### response
````python
{'rankings': [{'#': '1.', 'ID': ' Virtus.pro', 'Points': ' 4950', 'DreamLeague Season 10': 0, 'The Kuala Lumpur Major': ' 4950', 'The Bucharest Minor': 0, 'The Chongqing Major': 0, 'TBD': 0, 'DreamLeague Season 11': 0, 'AMD SAPPHIRE Dota PIT Minor': 0},...{'#': '23.', 'ID': ' ROOONS', 'Points': ' 8.192 5', 'DreamLeague Season 10': ' 20', 'The Kuala Lumpur Major': 0, 'The Bucharest Minor': 0, 'The Chongqing Major': 0, 'TBD': 0, 'DreamLeague Season 11': 0, 'AMD SAPPHIRE Dota PIT Minor': 0}], 'schedule': [{'Date': 'Sep 16-21, 2018', 'Title': ' The Kuala Lumpur Major Qualifier', 'DPC Points': '0'},...,{'Date': 'June 20-30, 2019', 'Title': 'Major Main Event', 'DPC Points': '15000'}]}
````
##### example
```python
pro_circuit_details = dota_obj.get_pro_circuit_details()
```
***

<a name="counterstrike"></a>  
#### counterstrike(appname)
create a counterstike object

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| appname | <code>string</code> | The name for your app, you can refer to the [liquipedia's terms of use](https://liquipedia.net/api-terms-of-use) for more information |

##### example
```python
from liquipediapy import counterstrike

counterstrike_obj = counterstrike("appname")
```
***

<a name="counterstrike_get_players"></a>  
#### get_players()
returns all counter-strike players from all regions from [Portal:Players](https://liquipedia.net/counterstrike/Portal:Players)

##### response
````python
[{'id': 'MITSARAS', 'name': 'DimitrisFiloxenidis', 'country': 'Austria', 'team': 'Private Esports'},..., {'id': 'takbok', 'name': 'JanTheron', 'country': 'South Africa', 'team': ''}]
````
##### example
```python
players = counterstrike_obj.get_players()
```
***

<a name="counterstrike_get_teams"></a>  
#### get_teams(region)
returns all counter-strike teams from specified region

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| region | <code>string</code> | region from which you want the teams you can find the regions on [this](https://liquipedia.net/counterstrike/Portal:Teams) page tabs|

##### response
````python
[{'name': 'Astralis', 'logo': 'https://liquipedia.net/commons/images/3/37/Astralislogo_std.png', 'playes': [{'country': 'Denmark', 'id': 'dev1ce', 'name': ' Nicolai Reedtz '}, {'country': 'Denmark', 'id': 'dupreeh', 'name': ' Peter Rasmussen '}, {'country': 'Denmark', 'id': 'Xyp9x', 'name': ' Andreas Højsleth '}, {'country': 'Denmark', 'id': 'gla1ve', 'name': ' Lukas Rossander '}, {'country': 'Denmark', 'id': 'Magisk', 'name': ' Emil Reif '}, {'country': 'Denmark', 'id': 'zonic', 'name': ' Danny Sørensen '}]},...,{'name': 'x6tence', 'logo': 'https://liquipedia.net/commons/images/b/b4/X6tencelogo_std.png', 'playes': [{'country': 'Spain', 'id': 'FlipiN', 'name': ' Antonio Rivas del Rey '}, {'country': 'Argentina', 'id': 'JonY BoY', 'name': ' Jonathan Muñoz '}, {'country': 'Spain', 'id': 'TheClaran', 'name': ' Carlos Gonzálvez '}, {'country': 'Spain', 'id': 'Meco', 'name': ' Sebastián Meco '}, {'country': 'Spain', 'id': 'Vares', 'name': ' Luis Olivares '}, {'country': 'Spain', 'id': 'FeldmaN', 'name': ' Rafael  Rodríguez '}, {'country': 'Spain', 'id': 'Hepa', 'name': ' Juan Borges '}, {'country': 'Spain', 'id': 'TiburoN', 'name': ' Miguel Agudo Sánchez '}, {'country': 'Spain', 'id': 'Alexsen', 'name': ' Alejandro Alberto Gesteira '}, {'country': 'Spain', 'id': 'Xeon', 'name': ' Carles García '}]}]
````
##### example
```python
teams = counterstrike_obj.get_teams()
```
***

<a name="counterstrike_get_player_info"></a>  
#### get_player_info(playerName,results)
gets information for a specified player

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| playerName | <code>string</code> | name of player |
| results | <code>bool</code> | if you want to parse the results page for the player, defauls to ```False``` |

##### response
````python
{'info': {'image': 'https://liquipedia.net/commons/images/thumb/5/51/Nitr0_at_StarLadder_i-League_StarSeries_S4.jpg/600px-Nitr0_at_StarLadder_i-League_StarSeries_S4.jpg', 'name': 'Nicholas Cannella', 'birth_details': 'August 16, 1995 (1995-08-16) (age 23)', 'countries': ['United States'], 'status': 'Active', 'team': 'Team Liquid', 'roles': ['In-game leader', 'AWPer'], 'earnings': 403482, 'games': ['Global Offensive']}, 'links': {'twitter': 'https://twitter.com/nitr0',...'steamcommunity': 'https://steamcommunity.com/profiles/76561197995889730'},'history': [{'duration': '2014-04-08 – 2014-10-16', 'name': 'Area 51 Gaming'},...{'duration': '2015-01-13 – Present', 'name': 'Team Liquid'}],'achivements': [{'Date': '2018-12-09', 'Placement': '22', 'Tier': 'Premier', 'game': 'Counter-Strike: Global Offensive', 'Tournament': 'ESL Pro League Season 8 - Finals', 'Team': 'Team Liquid', 'Result': '1 : 3', 'opponent': 'Astralis', 'Prize': '$110,000'},...{'Date': '2016-07-10', 'Placement': '22', 'Tier': 'Premier', 'game': 'Counter-Strike: Global Offensive', 'Tournament': 'ESL One: Cologne 2016', 'Team': 'Team Liquid', 'Result': '0 : 2', 'opponent': 'SK Gaming', 'Prize': '$150,000'}],'gear_settings': {'hardware': {'Mouse': 'ZOWIE by BenQ EC2-B', 'Mousepad': 'Zowie G-SR (Dark Grey Edition)', 'Monitor': 'ZOWIE by BenQ XL2546', 'Refresh rate': '240 Hz', 'In-game resolution': '1024×768', 'Scaling': 'Black Bars', 'Keyboard': 'MK Disco (TKL)', 'Headset': 'HyperX Cloud II (Silver)'}, 'Mouse': {'Mouse': 'ZOWIE by BenQ EC2-B', 'Effective DPI': '700', 'cm/360': '59.4', 'in/360': '23.4', 'DPI': '400', 'In-game sens.': '1.75', 'Windows sens.': '6/11', 'Accel.': '1.05', 'Raw input?': 'On', 'Polling rate': '500 Hz'}, 'Crosshair': {'Style': '4', 'Size': '3', 'Thickness': '0.5', 'Sniper': '1', 'Gap': '-1', 'Outline': 'Yes (thickness 0)', 'Dot': 'No (0)', 'Color': 'Green (1)', 'Alpha': '255'}},'results': [{'Date': '2018-12-09', 'Placement': '22', 'Tier': 'Premier', 'game': 'Counter-Strike: Global Offensive', 'Tournament': 'ESL Pro League Season 8 - Finals', 'Team': 'Team Liquid', 'Result': '1 : 3', 'opponent': 'Astralis', 'Prize': '$110,000'},...,{'Date': '2014-06-22', 'Placement': '33', 'Tier': 'Minor', 'game': 'Counter-Strike: Global Offensive', 'Tournament': 'ESEA Season 16: Main Division - North America', 'Team': 'Area 51 Gaming', 'Result': '6 - 16', 'opponent': 'Mythic', 'Prize': '$800'}]}
````
##### example
```python
player_details = counterstrike_obj.get_player_info('nitr0',True)
```
***

<a name="counterstrike_get_team_info"></a>  
#### get_team_info(teamName,results)
gets information for a specified team

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| teamName | <code>string</code> | name of the team |
| results | <code>bool</code> | if you want to parse the results page for the team, defauls to ```False``` |


##### response
````python
{'info': {'image': 'https://liquipedia.net/commons/images/thumb/0/07/Team_liquid_logo_2017.png/600px-Team_liquid_logo_2017.png', 'location': ['Netherlands', 'North America'], 'region': ' North America', 'ceo': '  Victor "Nazgul" Goossens Steve "LiQuiD112" Arhancet', 'manager': ' Steve "jokasteve" Perino', 'team captain': ' Nicholas "nitr0" Cannella', 'coaches': ' Wilton "zews" Prado', 'sponsor': ['Alienware', 'Monster Energy', 'SAP', 'Twitch', 'HyperX', 'Ballistix', 'NEEDforSEAT'], 'earnings': 1971562, 'games': ['Global Offensive'], 'created': 'Organization: 2000-??-??: 2015-01-13'}, 'links': {'teamliquidpro': 'https://www.teamliquidpro.com/',...'steamcommunity': 'https://steamcommunity.com/groups/teamliquid-pro'},'team_roster': [{'Country': 'USA', 'ID': 'nitr0', 'Name': 'Nicholas Cannella', 'Join Date': '2015-01-13'},... {'Country': 'Brazil', 'ID': 'zews (Coach)', 'Name': 'Wilton Prado', 'Join Date': '2016-11-10'}],'achivements': [{'Date': '2018-12-09', 'Placement': '22', 'Tier': 'Premier', 'Type': 'Offline', 'game': 'Counter-Strike: Global Offensive', 'Tournament': 'ESL Pro League Season 8 - Finals', 'Results': '1:3', 'opponent': 'Astralis', 'Prize': '$110,000'},...,{'Date': '2016-07-10', 'Placement': '22', 'Tier': 'Premier', 'Type': 'Offline' 'game': 'Counter-Strike: Global Offensive', 'Tournament': 'ESL One: Cologne 2016', 'Results': '0:2', 'opponent': 'SK Gaming', 'Prize': '$150,000'}],'results': [{'Date': '2010-04-04', 'Placement': '1', 'Tier': 'B-Tier', 'Type': 'Offline', 'game': 'Counter-Strike', 'Tournament': 'Arbalet Ukraine 2010', 'Results': '2:0', 'opponent': 'PiNG', 'Prize': '$3,000'},...,{'Date': '2010-03-06', 'Placement': '1', 'Tier': 'S-Tier', 'Type': 'Offline', 'game': 'Counter-Strike', 'Tournament': 'Intel Extreme Masters IV', 'Results': '2:0', 'opponent': 'Fnatic', 'Prize': '$50,000'}]}
````
##### example
```python
team_details = counterstrike_obj.get_team_info('Team Liquid',True)
```
***

<a name="counterstrike_get_transfers"></a>  
#### get_transfers()
gets all transfers from [Portal:Transfers](https://liquipedia.net/counterstrike/Portal:Transfers)


##### response
````python
[{'Date': '2018-12-16', 'Player': ['bnwGiggs'], 'Old': 'ALPHA Red', 'New': 'None'},...,{'Date': '2018-10-14', 'Player': ['fAst'], 'Old': 'Nemiga Gaming', 'New': 'None'}]
````
##### example
```python
transfers = counterstrike_obj.get_transfers()
```
***

<a name="counterstrike_get_upcoming_and_ongoing_games"></a>  
#### get_upcoming_and_ongoing_games()
gets all matches from [Liquipedia:Upcoming_and_ongoing_matches](https://liquipedia.net/counterstrike/Liquipedia:Upcoming_and_ongoing_matches)



##### response
````python
[{'team1': 'Dragons Esports Club', 'team2': 'Giants Gaming', 'start_time': 'December 16, 2018 - 16:00 UTC', 'tournament': 'ESL Masters España S4', 'twitch_channel': 'esl csgo es'},...,{'team1': 'Team Endpoint', 'team2': 'Orgles5', 'start_time': 'January 5, 2019 - 16:00 UTC', 'tournament': 'Premiership Winter 2018', 'twitch_channel': None}]
````
##### example
```python
games = counterstrike_obj.get_upcoming_and_ongoing_games()
```
***

<a name="counterstrike_get_tournaments"></a>  
#### get_tournaments(type)
gets all tournaments from [Portal:Tournaments](https://liquipedia.net/counterstrike/Portal:Leagues)

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| type | <code>string</code> | type of tournaments , defaults to ```None``` , accepted values are ```Premier``` ,```Major```, ```Minor``` , ```Monthly```, ```Weekly```|


##### response
````python
[{'tier': 'Minor', 'tournament': 'WESG 2018 Female - Southeast Asia', 'date': 'Dec 13 - 16, 2018', 'prize': '$15,000', 'teams_no': '10', 'host_locaion': ' Malaysia', 'event_locaion': ' Kuala Lumpur', 'first_place': 'ArkAngel.fe', 'second_place': 'Asterisk'},...,{'tier': 'Qualifier', 'tournament': 'ESWC Africa 2018 - Nigerian Qualifier', 'date': 'Nov 17 - 18, 2018', 'prize': '', 'teams_no': '16', 'host_locaion': ' Nigeria', 'event_locaion': ' Online', 'qualified': []}]
````
##### example
```python
tournaments = counterstrike_obj.get_tournaments()
```
***

<a name="counterstrike_get_weapons"></a>  
#### get_weapons()
gets all weapons from [Portal:Weapons](https://liquipedia.net/counterstrike/Portal:Weapons)


##### response
````python
[{'image': 'https://liquipedia.net/commons/images/4/4b/Weapon_hkp2000.png', 'name': 'P2000'},...,{'image': 'https://liquipedia.net/commons/images/a/ab/Weapon_knife_bowie.png', 'name': 'Bowie Knife'}]
````
##### example
```python
weapons = counterstrike_obj.get_weapons()
```
***

<a name="counterstrike_get_weapon_info"></a>  
#### get_weapon_info(weaponName)
gets information for a specified weapon

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| weaponName | <code>string</code> | Name of the weapon you want information for|


##### response
````python
{'image': 'https://liquipedia.net/commons/images/1/14/Weapon_CZ75-Auto.png', 'class': 'pistol', 'price': '$500', 'kill_award': '$50', 'ammunition/capacity': '12/12', 'reload_time': '2.7ss', 'movement_speed': '240 units/s', 'firing_mode': 'Automatic', 'side': ['Counter-Terrorists', ' Terrorists']}
````
##### example
```python
weapon_details = counterstrike_obj.get_weapon_info('CZ75-Auto')
```
***

<a name="counterstrike_get_statistics"></a>  
#### get_statistics()
gets information from conter-strike [statistics](https://liquipedia.net/counterstrike/Statistics/Total) page


##### response
````python
[{'name': ' Astralis', 'earnings': '$ 5,909,134', 'golds': '20', 'silver': '10', 'bronze': '2'},..., {'name': ' USSR Team', 'earnings': '$ 4,128', 'golds': '2', 'silver': '2', 'bronze': '2'}]
````
##### example
```python
statistics = counterstrike_obj.get_statistics()
```
***

<a name="counterstrike_get_patches"></a>  
#### get_patches()
gets all patches from [Patches](https://liquipedia.net/counterstrike/Patches)


##### response
````python
[{'Version': '1.36.6.9', 'Release Date': '14 December 2018', 'Release Highlights': ['Danger Zone Changes']},...{'Version': 'Beta 1.0', 'Release Date': '19 June 1999', 'Release Highlights': ['Initial Beta Release']}]
````
##### example
```python
patches = counterstrike_obj.get_patches()
```
***

<a name="smash"></a>  
#### smash(appname)
create a smash object

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| appname | <code>string</code> | The name for your app, you can refer to the [liquipedia's terms of use](https://liquipedia.net/api-terms-of-use) for more information |

##### example
```python
from liquipediapy import counterstrike

smash_obj = smash("appname")
smash_obj = smash('appname', "F:\\Path\\To\\Debug\\Folder\\")
```
***


<a name="smash_get_players"></a>  
#### get_players()
returns all smash players from all regions from 
- [Players_(Americas)/64](https://liquipedia.net/smash/Players_(Americas)/64) 
- [Players_(Americas)/Melee](https://liquipedia.net/smash/Players_(Americas)/Melee) 
- [Players_(Americas)/Project_M](https://liquipedia.net/smash/Players_(Americas)/Project_M) 
- [Players_(Americas)/Brawl_WiiU_Ultimate](https://liquipedia.net/smash/Players_(Americas)/Brawl_WiiU_Ultimate) 
- [Players_(Europe)/64](https://liquipedia.net/smash/Players_(Europe)/64) 
- [Players_(Europe)/Melee](https://liquipedia.net/smash/Players_(Europe)/Melee) 
- [Players_(Europe)/Project_M](https://liquipedia.net/smash/Players_(Europe)/Project_M) 
- [Players_(Europe)/Brawl_WiiU_Ultimate](https://liquipedia.net/smash/Players_(Europe)/Brawl_WiiU_Ultimate) 
- [Players_(Asia/Oceania)](https://liquipedia.net/smash/Players_(Asia/Oceania)) 
  _Asia/Oceania page use dynamic tab instead of static tabs_

##### response
````python
[{'Country': 'Canada', 'ID': 'Fck Vwls', 'Real Name': 'Neil Mahadeo', 'Main': ['Captain Falcon'], 'Team': '', 'Links': {}, 'Game': '64'}, {'Country': 'Canada', 'ID': 'HandsomeTom', 'Real Name': 'Etienne Gagnon', 'Main': ['Kirby'], 'Team': '', 'Links': {'twitter': 'https://twitter.com/HandsomeTomSSB'}, 'Game': '64'},...,{'Country': 'Australia', 'ID': 'Waveguider', 'Real Name': 'Alex Grant', 'Main': ['Greninja', 'Wii Fit Trainer'], 'Team': '', 'Links': {'twitch': 'https://www.twitch.tv/waveguider', 'twitter': 'https://twitter.com/WaveguiderAU'}, 'Game': 'Brawl WiiU Ultimate'}]
````
##### example
```python
players = smash_obj.get_players()
```
***


<a name="smash_get_player_info"></a>  
#### get_player_info(playerName,results)
gets information for a specified player

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| playerName | <code>string</code> | name of player |
| results | <code>bool</code> | if you want to parse the results page for the player, defauls to ```False``` |


##### response
````python
{'info': {'image': 'https://liquipedia.net/commons/images/thumb/5/5b/Armada_TBH8.jpg/600px-Armada_TBH8.jpg', 'name': 'Adam Lindgren', 'born': ' (1993-03-28) March 28, 1993 (age 29)', 'countries': ['Sweden'], 'years_active': '2007 - 2019', 'team': 'Alliance', 'earnings': 298358, 'nicknames': 'The Swedish Sniper, The Beast from Sweden, The One True God', 'current_mains': ' Inkling', 'secondaries': ' Corrin Mewtwo'}, 'links': {'www': 'https://www.reddit.com/user/Armada_', 'twitter': 'https://twitter.com/ArmadaUGS', 'facebook': 'https://facebook.com/armadassbm'},..., {'Game': 'Melee', 'Date': '2007-04-03', 'Place': ('D1', '4th'), 'Event': "Smashers' Reunion 2", 'Result': {'Characters': [], 'Scores': ['L'], 'Opp_characters': [], 'Opponent': 'Helios'}, 'Prize': {'amount': 49.0, 'currency': '$'}}]}
````
##### example
```python
player_details = smash_obj.get_player_info('Armada',True)
```
***

<a name="smash_get_teams"></a>  
#### get_teams()
returns all smash teams

##### response
````python
['16-Bit Esports', '26 RISING', 'AllChat Esports', 'Alliance', 'Balance Gaming', 'Bandits Gaming', 'beastcoast', 'Bermuda', 'Black Sun E-Sports', 'BMS ESPORTS', 'BOX', 'Cologne Gaming Network', 'Chilly Mountain', 'CJ eSports', 'Clash Tournaments', 'Cloud9', 'Coalition Gaming', 'Conduit Gaming', 'Counter Logic Gaming', 'Crazy Raccoon', 'Dignitas', 'Divinity Esports', 'EndGameTV', 'Esport BERG', 'Even Matchup Gaming', 'Evil Geniuses', 'FaZe Clan', 'Fly Society', 'FlyQuest', 'FURIA Esports', 'Geeky Goon Squad', 'Golden Guardians', 'Granit Gaming', 'Ground Zero Gaming', 'Hexagon', 'Hound Esports', 'IlluZion Gaming', 'InControl Nation', 'Kanga Esports', 'Karnage eSports', 'Lavender esports', 'Level1', 'LOSC eSports', 'Luminosity Gaming', 'Mazer Gaming', 'Melee It On Me', 'Mindfreak', 'Moist Esports', 'Most Valuable Gaming', 'mYinsanity', 'Nevermore International', 'NidhoGG esport', 'orKs Grand Poitiers', 'Panda', 'Patchwork', 'Phenoms Pro', 'Phoenix Blue', 'Pittsburgh Knights', 'plan-B esports', 'Polar Ace', 'Pulse', 'Rectify Esports', 'Red Bull eSports', 'RELAPSE', 'Renegades', 'Revo', 'RoyalBlue eSports', 'Salty Arena', 'Shogunate Gaming', 'Sissi State Punks', 'SmartFox Gaming', 'Smash Studios', 'Solary', 'Spacestation Gaming', 'SSBMontreal', 'T1', 'Taipan Esports', 'The Dutch Brawlers', 'Team Envy', 'Heir', 'Team Liquid', 'Team Oplon', 'TSM', 'Team Vegacy', 'Tempo Storm', 'Thunder Gaming', 'UYU', 'VGBootCamp', 'Warthox', 'Wolves eSports', '24 Islands', '2GGaming', 'Amino', 'AntiBeat', 'Armada', 'Asterion', 'Beefy Smash Doods', 'Boreal eSports', 'COGnitive Gaming', 'Control Gaming', 'Dark Sided', 'Demise', 'Denial eSports', 'Dream Team', 'eSports Ecosystem', 'Earthroot Gaming', 'Echo Fox', 'eLevate', 'Empire Arcadia', 'FolloweSports.com', 'Forward Smash', 'Frequency Gaming', 'G2 Esports', 'Glacial Gaming', 'Halocline Gaming', 'Immortals', 'justice esports', 'Kingsmen', 'Kyoto eSports', 'LeStream Esport', 'LowLandLions', 'Meliora Esports', 'Mentality Esports', 'Misfits', 'Mortality', 'NRG Esports', 'OG', 'Obey Alliance', 'Phoenix1', 'Poilon Software', 'Prometheus', 'ROOT Gaming', 'Rogue', 'Selfless Gaming', 'ShieldBreakFast', 'Sinai Village', 'Sloth', 'Splyce', 'TKA E-Sports', 'Curse', 'Team Secret', 'Team YP', 'TeamViral', 'Tuxedo Esports', 'Versus Gaming Center', 'VwS Gaming', 'Winterfox', 'World Best Gaming', 'Yatta Gaming', 'eUnited']
````
##### example
```python
teams = smash_obj.get_teams()
```
***


<a name="smash_get_team_info"></a>  
#### get_team_info(teamName)
gets information for a specified team

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| teamName | <code>string</code> | name of the team |

##### response
```python
{'info': {'image': 'https://liquipedia.net/commons/images/thumb/4/4e/T1_allmode.png/600px-T1_allmode.png', 'location': ['South Korea', 'United States'], 'region': ' North America', 'created': '2019-03-13'}, 'links': {'t1': 'https://t1.gg', 'facebook': 'https://facebook.com/SKsports.T1', 'twitter': 'https://twitter.com/T1', 'www': 'https://www.youtube.com/channel/UCJprx3bX49vNl6Bcw01Cwfg'}, 'team_roster': [{'Country': 'South Korea', 'ID': 'Sejun', 'Name': 'Sejun Park', 'Main': ['King Dedede'], 'Join Date': '2019-11-14'}, {'Country': 'Mexico', 'ID': 'MKLeo', 'Name': 'Leonardo Lopez Perez', 'Main': ['Pyra and Mythra', 'Byleth'], 'Join Date': '2020-02-26'}, {'Country': 'United States', 'ID': 'ANTi', 'Name': 'Jason Bates', 'Main': ['Mario', 'Snake'], 'Join Date': '2019-04-17', 'Leave Date': '2020-07-02'}, {'Country': 'United States', 'ID': 'Larry Lurr', 'Name': 'Larry Holland', 'Main': ['Wolf', 'Falco'], 'Join Date': '2019-04-17', 'Leave Date': '2020-01-10'}], 'org_roster': []}
```
##### example
```python
team_details = smash_obj.get_team_info('T1')
```
***

<a name="smash_get_transfers"></a>  
#### get_transfers()
gets all transfers from [Player_Transfers](https://liquipedia.net/smash/Player_Transfers)
from **Portal_Transfers/2014** to **Portal_Transfers/2022**


##### response
```python
[{'Date': '2014-11-09', 'Player': [{'Country': 'Japan', 'Main': 'Sheik', 'Name': 'Nietono'}], 'Old': 'None', 'New': 'DetonatioN Gaming', 'Link': 'http://team-detonation.net/news/3709'},...,{'Date': '2022-01-01', 'Player': [{'Country': 'Japan', 'Main': 'Corrin', 'Name': 'Ly'}, {'Country': 'Japan', 'Main': 'Link', 'Name': 'Rido'}, {'Country': 'Japan', 'Main': 'Falco', 'Name': 'MASA'}], 'Old': 'None', 'New': 'UNI Gaming', 'Link': 'https://twitter.com/uni_gaming_info/status/1477071164174389251'}]
```
##### example
```python
transfers = smash_obj.get_transfers()
```
***

<a name="smash_get_tournaments"></a>  
#### get_tournaments(games, extended_infos)
gets all tournaments from [Portal:Tournaments](https://liquipedia.net/smash/Portal:Tournaments)

##### parameters
| Param | Type | Description |
| --- | --- | --- |
| games | <code>list[string]</code> | games we want to retrieve, defaults is ```['64']```, accepted values are ```64```, ```Melee```, ```Brawl```, ```Project_M```, ```Wii_U```, ```Ultimate```|
| extended_infos | <code>bool</code> | get type of tournaments (Major, Invitationnal, Double, ...), Winner & RunnerUp characters (for Majors only)

##### response
```python
[{'Game': '64', 'Tournament': 'Apex 2022', 'Date': 'Nov 18 - 20, 2022', 'Prize': {'amount': ' ', 'currency': ' '}, 'Players': '', 'Location': {'Country': 'United States', 'City': 'Secaucus'}, 'Winner': {'Country': '', 'Name': ''}, 'Runner-up': {'Country': '', 'Name': ''}},..., {'Game': '64', 'Tournament': '1st Kansai', 'Date': 'Mar 14, 2008', 'Prize': {'amount': ' ', 'currency': ' '}, 'Players': '46', 'Location': {'Country': 'Japan', 'City': 'Osaka'}, 'Winner': {'Country': 'Japan', 'Name': 'Ron'}, 'Runner-up': {'Country': 'Japan', 'Name': 'Tsukuru BOY'}}]
```
```python
[{'Game': '64', 'Tournament': 'Apex 2022', 'Date': 'Nov 18 - 20, 2022', 'Prize': {'amount': ' ', 'currency': ' '}, 'Players': '', 'Location': {'Country': 'United States', 'City': 'Secaucus'}, 'Winner': {'Country': '', 'Name': ''}, 'Runner-up': {'Country': '', 'Name': ''}},..., {'Game': '64', 'Tournament': '1st Kansai', 'Date': 'Mar 14, 2008', 'Prize': {'amount': ' ', 'currency': ' '}, 'Players': '46', 'Location': {'Country': 'Japan', 'City': 'Osaka'}, 'Winner': {'Country': 'Japan', 'Name': 'Ron', 'Characters': ['Jigglypuff']}, 'Runner-up': {'Country': 'Japan', 'Name': 'Tsukuru BOY', 'Characters': ['Captain Falcon']}, 'Type': 'Major'}]
```
##### example
```python
tournaments = smash_obj.get_tournaments()
tournaments = smash_obj.get_tournaments(extended_infos=True)
tournaments = smash_obj.get_tournaments(games=['64', 'Melee', 'Brawl', 'Project_M', 'Wii_U', 'Ultimate'], extended_infos=True)
```
***


<a name="cb"></a> 
## Contributing

Contributions are welcome. Please submit all pull requests the against master branch. Please check the [Contributing Guidelines](https://github.com/c00kie17/liquipediapy/blob/master/CONTRIBUTING.md) for more details. If you want to contribute but have no idea what to work towards please check the [TODO](https://github.com/c00kie17/liquipediapy/blob/master/TODO.md) file or [Issues](https://github.com/c00kie17/liquipediapy/issues) there should always be something there you can work towards. Thanks! 

***
<a name="author"></a> 
## Author
[c00kie17](https://github.com/c00kie17)

***
<a name="ls"></a> 
## License
This project conforms to the [CC-BY-SA 3.0 license](https://creativecommons.org/licenses/by-sa/3.0/us/) as that is the License that all the text data on Liquipedia adhears to, for more information you can check out the [Liquipedia Copyrights Page](https://liquipedia.net/commons/Liquipedia:Copyrights). 

A lot of images you can download with this API have been provided to Liquipedia under separate licensing terms that may be incompatible with [CC-BY-SA 3.0 license](https://creativecommons.org/licenses/by-sa/3.0/us/).

***
<a name="notes"></a> 
## Notes
Liquipedia has a [API Terms of Use page](https://liquipedia.net/api-terms-of-use). The rate limits mentioned there have to be strictly followed, or bans will be issued by Liquipedias server administration.
