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


Python_stab = {python_s.find_all('span',class_="release-number")[2].text.split('Python')[1].strip()}
PHP_stab = {php_s.find_all('a',class_="download-link")[1].text.strip()}
CS_stab = {cs_s.find_all('h2',class_="margin-none font-size-h6")[2].text.split('C#')[1]}
CPP_stab = {cpp_s.find_all('span',class_='wikidata-snak wikidata-main-snak')[21].text.strip()}
Lua_stab = {lua_s.find_all('a')[9].text.split('Lua')[1].strip()}
Java_stab  = {java_s.findAll('span',class_="wikidata-snak wikidata-main-snak")[13].text.split("SE")[1].strip()}
JS_stab = {js_s.find_all('span',class_='no-wikidata')[5].text.split('[Спецификация 1]')[0].strip()}
Swift_stab = {swift_s.find_all('span',class_='no-wikidata')[3].text.split('[')[0].strip()}
Kotlin_stab = {kt_s.find_all('span',class_='wikidata-snak wikidata-main-snak')[4].text}
Go_stab = {go_s.find_all('span',class_='wikidata-snak wikidata-main-snak')[8].text}
Ruby_stab = {ruby_s.find_all('span',class_='wikidata-snak wikidata-main-snak')[6].text}
Node_js_stab = {nodejs_s.find_all('a', class_="home-downloadbutton")[0].text.split('LTS')[0].strip()}
Unreal_Engine_stab = {ue_s.find_all('li')[4].text.split('Notes')[1].strip()}
Unity_stab = {unity_s.find_all('h4')[25].text.split("Unity")[1].strip()}

s_version = ( Python_stab, PHP_stab, CS_stab, CPP_stab, Lua_stab, Java_stab, JS_stab, Swift_stab, Kotlin_stab, Go_stab, Ruby_stab, Node_js_stab, Unreal_Engine_stab, Unity_stab)

stab_version = str(s_version).split("'")

stability_version = (stab_version[1], stab_version[3], stab_version[5].strip(), stab_version[7], stab_version[9], stab_version[11], stab_version[13], stab_version[15], stab_version[17], stab_version[19], stab_version[21], stab_version[23], stab_version[25], stab_version[27])