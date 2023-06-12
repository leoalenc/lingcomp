Python 3.8.10 (default, May 26 2023, 14:05:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> s='''Aramé panhẽ maã, usãi uikú waá kaá rupí, uyeréu suú arama, wirá arama. (p. 168, adapt.) - Então tudo o que estava espalhado pela mata virou animal, ave. - Aramé opaĩ mahã, oçâin oikộ uahá cahá rupí, ocërêo çöô arãma, uyrá arãma.'''
>>> f=open('data/magalhaes.txt','r')
>>> text=f.read()
>>> import os
>>> os.getcwd()
'/home/leonel/lingcomp'
>>> type(f)
<class '_io.TextIOWrapper'>
>>> text
'Aramé panhẽ maã, usãi uikú waá kaá rupí, uyeréu suú arama, wirá arama. (p. 168, adapt.) - Então tudo o que estava espalhado pela mata virou animal, ave. - Aramé opaĩ mahã, oçâin oikộ uahá cahá rupí, ocërêo çöô arãma, uyrá arãma.\n'
>>> parts=re.split(r"[-)(]",text)
>>> len(parts)
5
>>> for part in parts:
	print(part)

	
Aramé panhẽ maã, usãi uikú waá kaá rupí, uyeréu suú arama, wirá arama. 
p. 168, adapt.
 
 Então tudo o que estava espalhado pela mata virou animal, ave. 
 Aramé opaĩ mahã, oçâin oikộ uahá cahá rupí, ocërêo çöô arãma, uyrá arãma.

>>> parts
['Aramé panhẽ maã, usãi uikú waá kaá rupí, uyeréu suú arama, wirá arama. ', 'p. 168, adapt.', ' ', ' Então tudo o que estava espalhado pela mata virou animal, ave. ', ' Aramé opaĩ mahã, oçâin oikộ uahá cahá rupí, ocërêo çöô arãma, uyrá arãma.\n']
>>> parts=re.split(r"\s+-\s+|[)(]",text)
>>> len(parts)
5
>>> for part in parts:
	print(part)

	
Aramé panhẽ maã, usãi uikú waá kaá rupí, uyeréu suú arama, wirá arama. 
p. 168, adapt.

Então tudo o que estava espalhado pela mata virou animal, ave.
Aramé opaĩ mahã, oçâin oikộ uahá cahá rupí, ocërêo çöô arãma, uyrá arãma.

>>> example={}
>>> example['yrl']=parts[0]
>>> example['source']=parts[1]
>>> example['por']=parts[3]
>>> example['orig']=parts[4]
>>> for k,v in example.items():
	print(k,v)

	
yrl Aramé panhẽ maã, usãi uikú waá kaá rupí, uyeréu suú arama, wirá arama. 
source p. 168, adapt.
por Então tudo o que estava espalhado pela mata virou animal, ave.
orig Aramé opaĩ mahã, oçâin oikộ uahá cahá rupí, ocërêo çöô arãma, uyrá arãma.

>>> for k,v in example.items():
	print(f"{k}:\t'{v}'")

	
yrl:	'Aramé panhẽ maã, usãi uikú waá kaá rupí, uyeréu suú arama, wirá arama. '
source:	'p. 168, adapt.'
por:	'Então tudo o que estava espalhado pela mata virou animal, ave.'
orig:	'Aramé opaĩ mahã, oçâin oikộ uahá cahá rupí, ocërêo çöô arãma, uyrá arãma.
'
>>> regex=r"\w*[áéíú]\w*"
>>> re.findall(regex,example['yrl'])
['Aramé', 'uikú', 'waá', 'kaá', 'rupí', 'uyeréu', 'suú', 'wirá']
>>> regex=r"\w+"
>>> re.findall(regex,example['yrl'])
['Aramé', 'panhẽ', 'maã', 'usãi', 'uikú', 'waá', 'kaá', 'rupí', 'uyeréu', 'suú', 'arama', 'wirá', 'arama']
>>> regex=r"\w*"
>>> re.findall(regex,example['yrl'])
['Aramé', '', 'panhẽ', '', 'maã', '', '', 'usãi', '', 'uikú', '', 'waá', '', 'kaá', '', 'rupí', '', '', 'uyeréu', '', 'suú', '', 'arama', '', '', 'wirá', '', 'arama', '', '', '']
>>> regex=r"\w+|[,.?]"
>>> re.findall(regex,example['yrl'])
['Aramé', 'panhẽ', 'maã', ',', 'usãi', 'uikú', 'waá', 'kaá', 'rupí', ',', 'uyeréu', 'suú', 'arama', ',', 'wirá', 'arama', '.']
>>> a='Pois pois...'
>>> regex=r"\w+|[,.?]+"
>>> re.findall(regex,a)
['Pois', 'pois', '...']
>>> re.sub(r"ë",r"ẹ",example['orig'])
'Aramé opaĩ mahã, oçâin oikộ uahá cahá rupí, ocẹrêo çöô arãma, uyrá arãma.\n'
>>> vowel=r"[aeiou]"
>>> re.sub(vowel,r"x",example['yrl'])
'Arxmé pxnhẽ mxã, xsãx xxkú wxá kxá rxpí, xyxréx sxú xrxmx, wxrá xrxmx. '
>>> ditongo=r"[aeiou]{2,}"
>>> re.sub(ditongo,r"xy","o cachorro fez au au auuu")
'o cachorro fez xy xy xy'
>>> ditongo=r"[aeiou]{2,4}"
>>> re.sub(ditongo,r"xy","o cachorro fez au au auuu aaauuuu")
'o cachorro fez xy xy xy xyxy'
>>> re.sub(ditongo,r"xy","o cachorro fez au au auuu aaauuuuu")
'o cachorro fez xy xy xy xyxy'
>>> re.sub(ditongo,r"xy","o cachorro fez au au auuu aaauuuuui")
'o cachorro fez xy xy xy xyxyi'
>>> ditongo=r"[aeiou]{,4}"
>>> re.sub(ditongo,r"xy","o cachorro fez au au auuu aaauuuuui")
'xyxy xycxyxycxyhxyxyrxyrxyxy xyfxyxyzxy xyxy xyxy xyxy xyxyxyxy'
>>> 