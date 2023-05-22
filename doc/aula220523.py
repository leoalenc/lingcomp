>>> lista=[2,7]
>>> x, y = lista
>>> x
2
>>> y
7
>>> u,v= 'ab'
>>> u
'a'
>>> v
'b'
>>> u,v,z='abc'
>>> z
'c'
>>> u,v,z='ab'
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#101>", line 1, in <module>
ValueError: not enough values to unpack (expected 3, got 2)
>>> u,v='abc'
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#102>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
>>> def maxnum1(x,y):
	if x > y:
		return x
	else:
		return y

	
>>> def maxnum1(x,y):
	if x > y:
		return x
	else:
		return y

	
>>> maxnum1(3,9)
9
>>> maxnum1(11,9)
11
>>> def maxnum1(x,y):
	if x > y:
		return x
	return y

>>> def maxnum1(x,y):
	maxnum=x
	if y > x:
		maxnum=y
	return maxnum

>>> maxnum1(3,9)
9
>>> maxnum1(11,9)
11
>>> def maxnum2(x,y,z):
	maxnum=x
	if y > x and y > z:
		maxnum=y
	elif z > y and z > x:
		maxnum=z
	return maxnum

>>> maxnum1(3,9,7)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#121>", line 1, in <module>
TypeError: maxnum1() takes 2 positional arguments but 3 were given
>>> maxnum2(3,9,7)
9
>>> maxnum2(3,9,70)
70
>>> maxnum2(300,9,70)
300
>>> "scalability"
'scalability'
>>> def maxnum3(nums):
	maxnum=1
	for num in nums:
		if num > maxnum:
			maxnum=num
	return maxnum

>>> nums=[2]
>>> maxnum3(nums)
2
>>> nums=[]
>>> maxnum3(nums)
1
>>> nums=[-2,-5, 2, 9, 8, 700]
>>> maxnum3(nums)
700
>>> def maxnum3(nums):
	maxnum=0
	for num in nums:
		if num > maxnum:
			maxnum=num
	return maxnum

>>> def maxnum3(nums):
	maxnum=nums[0]
	for num in nums:
		if num > maxnum:
			maxnum=num
	return maxnum

>>> nums=[-2,-5, 2, 9, 8, 700, -11,0]
>>> maxnum3(nums)
700
>>> nums=[]
>>> maxnum3(nums)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#146>", line 1, in <module>
  File "<pyshell#142>", line 2, in maxnum3
IndexError: list index out of range
>>> def maxnum3(nums):
	if maxnum:
		maxnum=nums[0]
	for num in nums:
		if num > maxnum:
			maxnum=num
	return maxnum

>>> maxnum3(nums)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#149>", line 1, in <module>
  File "<pyshell#148>", line 2, in maxnum3
UnboundLocalError: local variable 'maxnum' referenced before assignment
>>> def maxnum3(nums):
	if nums:
		maxnum=nums[0]
		for num in nums:
			if num > maxnum:
				maxnum=numreturn maxnum
				
SyntaxError: invalid syntax
>>> def maxnum3(nums):
	if nums:
		maxnum=nums[0]
		for num in nums:
			if num > maxnum:
				maxnum=num
		return maxnum

	
>>> maxnum3(nums)
>>> retorno=maxnum3(nums)
>>> type(retorno)
<class 'NoneType'>
>>> max(1,80,5,-2, -10, 0)
80
>>> def maxnum3(*nums):
	if nums:
		maxnum=nums[0]
		for num in nums:
			if num > maxnum:
				maxnum=num
		return maxnum

	
>>> maxnum3(1,80,5,-2, -10, 0)
80
>>> max()
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#161>", line 1, in <module>
TypeError: max expected 1 argument, got 0
>>> maxnum3()
>>> maxnum3(1,80,5)
80
>>> maxnum3(1,5)
5
>>> maxnum3(1)
1
>>> maxnum3()
>>> type(maxnum3())
<class 'NoneType'>
>>> import conllu
>>> from io import open
>>> from conllu import parse_incr
>>> data_file = open("/home/leonel/complin/nheengatu/data/corpus/universal-dependencies/yrl_complin-ud-test.conllu", "r", encoding="utf-8")
>>> sample=[]
>>> i=0
>>> data=data_file.read()
>>> data[:10]
'# sent_id '
>>> data[:100]
'# sent_id = MooreFP1994:0:0:1\n# text = Yamunhã timbiú, yapinaitika, yamunhã kaxirí.\n# text_eng = We '
>>> print(data[:100])
# sent_id = MooreFP1994:0:0:1
# text = Yamunhã timbiú, yapinaitika, yamunhã kaxirí.
# text_eng = We 
>>> sentences = parse(data)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#179>", line 1, in <module>
TypeError: parse() missing 4 required positional arguments: 'pref', 'textid', 'index', and 'sentid'
>>> sentences = conllu.parse(data)
>>> len(sentences)
920
>>> sent1=sentences[0]
>>> sent1
TokenList<Yamunhã, timbiú, ,, yapinaitika, ,, yamunhã, kaxirí, .>
>>> type(sent1)
<class 'conllu.models.TokenList'>
>>> sent1[0]
{'id': 1, 'form': 'Yamunhã', 'lemma': 'munhã', 'upos': 'VERB', 'xpos': 'V', 'feats': {'Number': 'Plur', 'Person': '1', 'VerbForm': 'Fin'}, 'head': 0, 'deprel': 'root', 'deps': None, 'misc': {'TokenRange': '0:7'}}
>>> type(sent1[0])
<class 'conllu.models.Token'>
>>> sent1[0]['upos']
'VERB'
>>> sent1[0]['lemma']
'munhã'
>>> sent1[0]['head']
0
>>> sent1[0]['deprel']
'root'
>>> sent1[1]['head']
1
>>> sent1.metadata['text']
'Yamunhã timbiú, yapinaitika, yamunhã kaxirí.'
>>> sent1.metadata['text_eng']
'We make food, we fish, we make chicha.'
>>> sent1.metadata['text_por']
'Fazemos comida, pescamos, fazemos caxiri.'
>>> freqdist={}
>>> token=sent1[0]
>>> token.keys()
dict_keys(['id', 'form', 'lemma', 'upos', 'xpos', 'feats', 'head', 'deprel', 'deps', 'misc'])
>>> sample=[]
>>> for sent in sentences[:20]:
	text=sent.metadata['text']
	sample.append(text)

	
>>> sample[0]
'Yamunhã timbiú, yapinaitika, yamunhã kaxirí.'
>>> f=open('sample.txt','w')
>>> for sent in sample:
	f.write(sent)
	f.write('\n")
		
SyntaxError: EOL while scanning string literal
>>> f=open('sample.txt','w')
>>> for sent in sample:
	f.write(sent)
	f.write('\n')

	
44
1
43
1
29
1
34
1
21
1
30
1
15
1
38
1
26
1
24
1
29
1
41
1
26
1
15
1
45
1
76
1
49
1
49
1
50
1
30
1
>>> f.close()
>>> import os
>>> os.getcwd()
'/home/leonel/complin/nheengatu/data'
>>> texto='''Yamunhã timbiú, yapinaitika, yamunhã kaxirí.
Yamburi maniaka paranã upé i membeka arama.
Ayuíri-putari se retama kití.
Yandé yapurungitá yaikú nheengatú.
Ixé se ruka upé aikú.
Rembeú aintá supé puranga ixé.
Aikwé kaxuwera.
Presizu aintá uistudari português upé.
Ti apitá, ayuíri kwá kití.
Ti tapira apigawa uyuká.
Nhaã yawara, aé usuú apigawa.
Indé remurari apekatú kwá suí tetama suí?
Maã taá rewasemu puxuwera?
Taína umaã maã?
Kuxiíma aikwé yepé feiticeiro akunheseri waá.
Ayururé se manha upitá arama yané rendawa upé se ratiwa uxari waá yandé arã.
Aintá ukuntari uakonteseri waá garapé apira kití.
Aintá upisika paá yandé yaú ramé timbiú irusanga.
Yaú timbiú sakú ti arama kurupira-itá urasú yandé.
Yamaã timbiú apigawa uú arama.'''
>>> sents=[sent.strip() for sent in texto.split('\n')]
>>> len(sents)
20
>>> sents[0]
'Yamunhã timbiú, yapinaitika, yamunhã kaxirí.'
>>> freqdist={}
>>> words=[]
>>> for sent in sents:
	words.extend(sent.split(" "))

	
>>> len(words)
113
>>> for word in words:
	if freqdist.get(word):
		freqdist[word]+=1
	else:
		freqdist[word]=1

		
>>> freq['timbiú']
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#231>", line 1, in <module>
NameError: name 'freq' is not defined
>>> freqdist['timbiú']
3
>>> maxfreq=1
>>> for word,freq in freqdist.items():
	if freq>1:
		maxfreq=freq

		
>>> maxfreq
3
>>> maxfreq
3
>>> freqdist
{'Yamunhã': 1, 'timbiú,': 1, 'yapinaitika,': 1, 'yamunhã': 1, 'kaxirí.': 1, 'Yamburi': 1, 'maniaka': 1, 'paranã': 1, 'upé': 3, 'i': 1, 'membeka': 1, 'arama.': 2, 'Ayuíri-putari': 1, 'se': 4, 'retama': 1, 'kití.': 3, 'Yandé': 1, 'yapurungitá': 1, 'yaikú': 1, 'nheengatú.': 1, 'Ixé': 1, 'ruka': 1, 'aikú.': 1, 'Rembeú': 1, 'aintá': 2, 'supé': 1, 'puranga': 1, 'ixé.': 1, 'Aikwé': 1, 'kaxuwera.': 1, 'Presizu': 1, 'uistudari': 1, 'português': 1, 'upé.': 1, 'Ti': 2, 'apitá,': 1, 'ayuíri': 1, 'kwá': 2, 'tapira': 1, 'apigawa': 2, 'uyuká.': 1, 'Nhaã': 1, 'yawara,': 1, 'aé': 1, 'usuú': 1, 'apigawa.': 1, 'Indé': 1, 'remurari': 1, 'apekatú': 1, 'suí': 1, 'tetama': 1, 'suí?': 1, 'Maã': 1, 'taá': 1, 'rewasemu': 1, 'puxuwera?': 1, 'Taína': 1, 'umaã': 1, 'maã?': 1, 'Kuxiíma': 1, 'aikwé': 1, 'yepé': 1, 'feiticeiro': 1, 'akunheseri': 1, 'waá.': 1, 'Ayururé': 1, 'manha': 1, 'upitá': 1, 'arama': 2, 'yané': 1, 'rendawa': 1, 'ratiwa': 1, 'uxari': 1, 'waá': 2, 'yandé': 2, 'arã.': 1, 'Aintá': 2, 'ukuntari': 1, 'uakonteseri': 1, 'garapé': 1, 'apira': 1, 'upisika': 1, 'paá': 1, 'yaú': 1, 'ramé': 1, 'timbiú': 3, 'irusanga.': 1, 'Yaú': 1, 'sakú': 1, 'ti': 1, 'kurupira-itá': 1, 'urasú': 1, 'yandé.': 1, 'Yamaã': 1, 'uú': 1}
>>> maxfreq=1
>>> for word,freq in freqdist.items():
	if freq>maxfreq:
		maxfreq=freq

		
>>> maxfreq
4
>>> for word,freq in freqdist.items():
	print(word,freq)

	
Yamunhã 1
timbiú, 1
yapinaitika, 1
yamunhã 1
kaxirí. 1
Yamburi 1
maniaka 1
paranã 1
upé 3
i 1
membeka 1
arama. 2
Ayuíri-putari 1
se 4
retama 1
kití. 3
Yandé 1
yapurungitá 1
yaikú 1
nheengatú. 1
Ixé 1
ruka 1
aikú. 1
Rembeú 1
aintá 2
supé 1
puranga 1
ixé. 1
Aikwé 1
kaxuwera. 1
Presizu 1
uistudari 1
português 1
upé. 1
Ti 2
apitá, 1
ayuíri 1
kwá 2
tapira 1
apigawa 2
uyuká. 1
Nhaã 1
yawara, 1
aé 1
usuú 1
apigawa. 1
Indé 1
remurari 1
apekatú 1
suí 1
tetama 1
suí? 1
Maã 1
taá 1
rewasemu 1
puxuwera? 1
Taína 1
umaã 1
maã? 1
Kuxiíma 1
aikwé 1
yepé 1
feiticeiro 1
akunheseri 1
waá. 1
Ayururé 1
manha 1
upitá 1
arama 2
yané 1
rendawa 1
ratiwa 1
uxari 1
waá 2
yandé 2
arã. 1
Aintá 2
ukuntari 1
uakonteseri 1
garapé 1
apira 1
upisika 1
paá 1
yaú 1
ramé 1
timbiú 3
irusanga. 1
Yaú 1
sakú 1
ti 1
kurupira-itá 1
urasú 1
yandé. 1
Yamaã 1
uú 1
>>> words=[]
>>> for sent in sents:
	for token in sent.split(" "):
		if token[-1] in ".,!?:;":
			words.append(token[:-1])
			#words.append(token[-1])
		else:
			words.append(token)

			
>>> len(words)
113
>>> words=[]
>>> for sent in sents:
	for token in sent.split(" "):
		if token[-1] in ".,!?:;":
			words.append(token[:-1].lower())
			#words.append(token[-1])
		else:
			words.append(token.lower())

			
>>> len(words)
113
>>> print(words,sep='\n')
['yamunhã', 'timbiú', 'yapinaitika', 'yamunhã', 'kaxirí', 'yamburi', 'maniaka', 'paranã', 'upé', 'i', 'membeka', 'arama', 'ayuíri-putari', 'se', 'retama', 'kití', 'yandé', 'yapurungitá', 'yaikú', 'nheengatú', 'ixé', 'se', 'ruka', 'upé', 'aikú', 'rembeú', 'aintá', 'supé', 'puranga', 'ixé', 'aikwé', 'kaxuwera', 'presizu', 'aintá', 'uistudari', 'português', 'upé', 'ti', 'apitá', 'ayuíri', 'kwá', 'kití', 'ti', 'tapira', 'apigawa', 'uyuká', 'nhaã', 'yawara', 'aé', 'usuú', 'apigawa', 'indé', 'remurari', 'apekatú', 'kwá', 'suí', 'tetama', 'suí', 'maã', 'taá', 'rewasemu', 'puxuwera', 'taína', 'umaã', 'maã', 'kuxiíma', 'aikwé', 'yepé', 'feiticeiro', 'akunheseri', 'waá', 'ayururé', 'se', 'manha', 'upitá', 'arama', 'yané', 'rendawa', 'upé', 'se', 'ratiwa', 'uxari', 'waá', 'yandé', 'arã', 'aintá', 'ukuntari', 'uakonteseri', 'waá', 'garapé', 'apira', 'kití', 'aintá', 'upisika', 'paá', 'yandé', 'yaú', 'ramé', 'timbiú', 'irusanga', 'yaú', 'timbiú', 'sakú', 'ti', 'arama', 'kurupira-itá', 'urasú', 'yandé', 'yamaã', 'timbiú', 'apigawa', 'uú', 'arama']
>>> print(*words,sep='\n')
yamunhã
timbiú
yapinaitika
yamunhã
kaxirí
yamburi
maniaka
paranã
upé
i
membeka
arama
ayuíri-putari
se
retama
kití
yandé
yapurungitá
yaikú
nheengatú
ixé
se
ruka
upé
aikú
rembeú
aintá
supé
puranga
ixé
aikwé
kaxuwera
presizu
aintá
uistudari
português
upé
ti
apitá
ayuíri
kwá
kití
ti
tapira
apigawa
uyuká
nhaã
yawara
aé
usuú
apigawa
indé
remurari
apekatú
kwá
suí
tetama
suí
maã
taá
rewasemu
puxuwera
taína
umaã
maã
kuxiíma
aikwé
yepé
feiticeiro
akunheseri
waá
ayururé
se
manha
upitá
arama
yané
rendawa
upé
se
ratiwa
uxari
waá
yandé
arã
aintá
ukuntari
uakonteseri
waá
garapé
apira
kití
aintá
upisika
paá
yandé
yaú
ramé
timbiú
irusanga
yaú
timbiú
sakú
ti
arama
kurupira-itá
urasú
yandé
yamaã
timbiú
apigawa
uú
arama
>>> "ADB".lower()
'adb'
>>> def mkfreqdist(words):
	freqdist={}
	for word in words:
		if freqdist.get(word):
			freqdist[word]+=1
		else:
			freqdist[word]=1
	return freqdist

>>> fd=mkfreqdist(words)
>>> maxfreq=1
>>> for word,freq in fd.items():
	if freq>maxfreq:
		maxfreq=freq

		
>>> maxfreq
4
>>> 
