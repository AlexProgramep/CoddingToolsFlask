import requests
from bs4 import BeautifulSoup as bs

python_v = requests.get('https://www.python.org/downloads/').text
php_v = requests.get('https://www.php.net').text
cpp_v = requests.get('https://ru.wikipedia.org/wiki/C%2B%2B').text
cs_v = requests.get('https://docs.microsoft.com/en-us/dotnet/csharp/').text
lua_v = requests.get('https://www.lua.org').text
java_v = requests.get('https://ru.wikipedia.org/wiki/Java').text
js_v = requests.get('https://ru.wikipedia.org/wiki/JavaScript').text
swift_v = requests.get('https://ru.wikipedia.org/wiki/Swift_(язык_программирования)').text
kt_v = requests.get('https://ru.wikipedia.org/wiki/Kotlin').text
go_v = requests.get('https://ru.wikipedia.org/wiki/Go').text
ruby_v = requests.get('https://ru.wikipedia.org/wiki/Ruby').text
nodejs_v = requests.get('https://nodejs.org/en/').text
ue_v = requests.get('https://www.unrealengine.com/en-US/release-notes').text
unity_v = requests.get('https://unity3d.com/ru/get-unity/download/archive').text

python_s = bs(python_v, 'html.parser')
php_s = bs(php_v, 'html.parser')
cpp_s = bs(cpp_v, 'html.parser')
cs_s = bs(cs_v, 'html.parser')
lua_s = bs(lua_v, 'html.parser')
java_s = bs(java_v, 'html.parser')
js_s = bs(js_v, 'html.parser')
swift_s = bs(swift_v, 'html.parser')
kt_s = bs(kt_v, 'html.parser')
go_s = bs(go_v, 'html.parser')
ruby_s = bs(ruby_v, 'html.parser')
nodejs_s = bs(nodejs_v, 'html.parser')
ue_s = bs(ue_v, 'html.parser')
unity_s = bs(unity_v, 'html.parser')


Python_v = {python_s.find_all('span',class_="release-number")[1].text.split('Python')[1]}
PHP_v = {php_s.find_all('a',class_="download-link")[0].text}
CS_v = {cs_s.find_all('h2',class_="margin-none font-size-h6")[2].text.split('C#')[1]}
CPP_v = {cpp_s.find_all('span',class_='wikidata-snak wikidata-main-snak')[21].text}
Lua_v ={lua_s.find_all('a')[8].text.split('Lua')[1]}
Java_v  = {java_s.findAll('span',class_="wikidata-snak wikidata-main-snak")[13].text.split("SE")[1].strip()}
JS_v = {js_s.find_all('span',class_='no-wikidata')[5].text.split('[Спецификация 1]')[0]}
Swift_v = {swift_s.find_all('span',class_='no-wikidata')[3].text.split('[')[0]}
Kotlin_v = {kt_s.find_all('span',class_='wikidata-snak wikidata-main-snak')[4].text}
Go_v = {go_s.find_all('span',class_='wikidata-snak wikidata-main-snak')[8].text}
Ruby_v = {ruby_s.find_all('span',class_='wikidata-snak wikidata-main-snak')[6].text}
Node_js_v = {nodejs_s.find_all('a', class_="home-downloadbutton")[1].text.split('Current')[0].strip()}
Unreal_Engine_v = {ue_s.find_all('li')[3].text.split('Notes')[1].strip()}
Unity_v = {unity_s.find_all('h4')[1].text.split("Unity")[1].strip()}

l_version = ( Python_v, PHP_v, CS_v, CPP_v, Lua_v, Java_v, JS_v, Swift_v, Kotlin_v, Go_v, Ruby_v, Node_js_v, Unreal_Engine_v, Unity_v)

last_ver = str(l_version).split("'")

last_version = (last_ver[1], last_ver[3], last_ver[5].strip(), last_ver[7], last_ver[9], last_ver[11], last_ver[13], last_ver[15], last_ver[17], last_ver[19], last_ver[21], last_ver[23], last_ver[25], last_ver[27])