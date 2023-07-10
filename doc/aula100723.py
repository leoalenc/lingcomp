Python 3.8.10 (default, May 26 2023, 14:05:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'/home/leonel/lingcomp'
>>> f='data/Gaviao_Sentenca_3.conllu'
>>> text=open(f).read()
>>> print(text)
# generator = UDPipe 2, https://lindat.mff.cuni.cz/services/udpipe
# udpipe_model = portuguese-bosque-ud-2.10-220711
# udpipe_model_licence = CC BY-NC-SA
# reviewer = Leonel Figueiredo de Alencar (LFdeA)
# title = Da tartaruga e o gavião (Rodrigues, 1890)
# sent_id = 3a
# text = O filho ia caçar camaleões, sempre encontrava penas de pássaro.
1	O	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	SpacesBefore=\s|TokenRange=1:2
2	filho	filho	NOUN	_	Gender=Masc|Number=Sing	4	nsubj	_	TokenRange=3:8
3	ia	ir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	4	aux	_	TokenRange=9:11
4	caçar	caçar	VERB	_	VerbForm=Inf	0	root	_	TokenRange=12:17
5	camaleões	camaleão	NOUN	_	Gender=Masc|Number=Plur	4	obj	_	SpaceAfter=No|TokenRange=18:27
6	,	,	PUNCT	_	_	8	punct	_	TokenRange=27:28
7	sempre	sempre	ADV	_	_	8	advmod	_	TokenRange=29:35
8	encontrava	encontrar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	4	parataxis	_	TokenRange=36:46
9	penas	pena	NOUN	_	Gender=Fem|Number=Plur	8	obj	_	TokenRange=47:52
10	de	de	ADP	_	_	11	case	_	TokenRange=53:55
11	pássaro	pássaro	NOUN	_	Gender=Masc|Number=Sing	9	nmod	_	SpaceAfter=No|TokenRange=56:63
12	.	.	PUNCT	_	_	4	punct	_	SpaceAfter=No|TokenRange=63:64

# generator = UDPipe 2, https://lindat.mff.cuni.cz/services/udpipe
# udpipe_model = portuguese-bosque-ud-2.10-220711
# udpipe_model_licence = CC BY-NC-SA
# reviewer = Leonel Figueiredo de Alencar (LFdeA)
# title = Da tartaruga e o gavião (Rodrigues, 1890)
# sent_id = 3b
# text = O filho ia caçar camaleões, sempre encontrava penas de pássaro.
1	O	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	SpacesBefore=\s|TokenRange=1:2
2	filho	filho	NOUN	_	Gender=Masc|Number=Sing	4	nsubj	_	TokenRange=3:8
3	ia	ir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	0	root	_	TokenRange=9:11
4	caçar	caçar	VERB	_	VerbForm=Inf	3	xcomp	_	TokenRange=12:17
5	camaleões	camaleão	NOUN	_	Gender=Masc|Number=Plur	4	obj	_	SpaceAfter=No|TokenRange=18:27
6	,	,	PUNCT	_	_	8	punct	_	TokenRange=27:28
7	sempre	sempre	ADV	_	_	8	advmod	_	TokenRange=29:35
8	encontrava	encontrar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	3	parataxis	_	TokenRange=36:46
9	penas	pena	NOUN	_	Gender=Fem|Number=Plur	8	obj	_	TokenRange=47:52
10	de	de	ADP	_	_	11	case	_	TokenRange=53:55
11	pássaro	pássaro	NOUN	_	Gender=Masc|Number=Sing	9	nmod	_	SpaceAfter=No|TokenRange=56:63
12	.	.	PUNCT	_	_	3	punct	_	SpaceAfter=No|TokenRange=63:64

>>> f.close()
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#5>", line 1, in <module>
AttributeError: 'str' object has no attribute 'close'
>>> f=open('data/Gaviao_Sentenca_3.conllu')
>>> f
<_io.TextIOWrapper name='data/Gaviao_Sentenca_3.conllu' mode='r' encoding='UTF-8'>
>>> text=f.read()
>>> print(text)
# generator = UDPipe 2, https://lindat.mff.cuni.cz/services/udpipe
# udpipe_model = portuguese-bosque-ud-2.10-220711
# udpipe_model_licence = CC BY-NC-SA
# reviewer = Leonel Figueiredo de Alencar (LFdeA)
# title = Da tartaruga e o gavião (Rodrigues, 1890)
# sent_id = 3a
# text = O filho ia caçar camaleões, sempre encontrava penas de pássaro.
1	O	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	SpacesBefore=\s|TokenRange=1:2
2	filho	filho	NOUN	_	Gender=Masc|Number=Sing	4	nsubj	_	TokenRange=3:8
3	ia	ir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	4	aux	_	TokenRange=9:11
4	caçar	caçar	VERB	_	VerbForm=Inf	0	root	_	TokenRange=12:17
5	camaleões	camaleão	NOUN	_	Gender=Masc|Number=Plur	4	obj	_	SpaceAfter=No|TokenRange=18:27
6	,	,	PUNCT	_	_	8	punct	_	TokenRange=27:28
7	sempre	sempre	ADV	_	_	8	advmod	_	TokenRange=29:35
8	encontrava	encontrar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	4	parataxis	_	TokenRange=36:46
9	penas	pena	NOUN	_	Gender=Fem|Number=Plur	8	obj	_	TokenRange=47:52
10	de	de	ADP	_	_	11	case	_	TokenRange=53:55
11	pássaro	pássaro	NOUN	_	Gender=Masc|Number=Sing	9	nmod	_	SpaceAfter=No|TokenRange=56:63
12	.	.	PUNCT	_	_	4	punct	_	SpaceAfter=No|TokenRange=63:64

# generator = UDPipe 2, https://lindat.mff.cuni.cz/services/udpipe
# udpipe_model = portuguese-bosque-ud-2.10-220711
# udpipe_model_licence = CC BY-NC-SA
# reviewer = Leonel Figueiredo de Alencar (LFdeA)
# title = Da tartaruga e o gavião (Rodrigues, 1890)
# sent_id = 3b
# text = O filho ia caçar camaleões, sempre encontrava penas de pássaro.
1	O	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	SpacesBefore=\s|TokenRange=1:2
2	filho	filho	NOUN	_	Gender=Masc|Number=Sing	4	nsubj	_	TokenRange=3:8
3	ia	ir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	0	root	_	TokenRange=9:11
4	caçar	caçar	VERB	_	VerbForm=Inf	3	xcomp	_	TokenRange=12:17
5	camaleões	camaleão	NOUN	_	Gender=Masc|Number=Plur	4	obj	_	SpaceAfter=No|TokenRange=18:27
6	,	,	PUNCT	_	_	8	punct	_	TokenRange=27:28
7	sempre	sempre	ADV	_	_	8	advmod	_	TokenRange=29:35
8	encontrava	encontrar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	3	parataxis	_	TokenRange=36:46
9	penas	pena	NOUN	_	Gender=Fem|Number=Plur	8	obj	_	TokenRange=47:52
10	de	de	ADP	_	_	11	case	_	TokenRange=53:55
11	pássaro	pássaro	NOUN	_	Gender=Masc|Number=Sing	9	nmod	_	SpaceAfter=No|TokenRange=56:63
12	.	.	PUNCT	_	_	3	punct	_	SpaceAfter=No|TokenRange=63:64

>>> f.close()
>>> import re
>>> os.listdir('.')
['teste.txt', 'doc', '.git', 'data', 'src', 'README.md']
>>> f=open('data/Gaviao_Sentenca_3.conllu',mode='rU',encoding='utf-8')

Warning (from warnings module):
  File "<pyshell#13>", line 1
DeprecationWarning: 'U' mode is deprecated

>>> f=open('data/Gaviao_Sentenca_3.conllu',mode='r',encoding='utf-8')
>>> text=f.read()
>>> print(text)
# generator = UDPipe 2, https://lindat.mff.cuni.cz/services/udpipe
# udpipe_model = portuguese-bosque-ud-2.10-220711
# udpipe_model_licence = CC BY-NC-SA
# reviewer = Leonel Figueiredo de Alencar (LFdeA)
# title = Da tartaruga e o gavião (Rodrigues, 1890)
# sent_id = 3a
# text = O filho ia caçar camaleões, sempre encontrava penas de pássaro.
1	O	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	SpacesBefore=\s|TokenRange=1:2
2	filho	filho	NOUN	_	Gender=Masc|Number=Sing	4	nsubj	_	TokenRange=3:8
3	ia	ir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	4	aux	_	TokenRange=9:11
4	caçar	caçar	VERB	_	VerbForm=Inf	0	root	_	TokenRange=12:17
5	camaleões	camaleão	NOUN	_	Gender=Masc|Number=Plur	4	obj	_	SpaceAfter=No|TokenRange=18:27
6	,	,	PUNCT	_	_	8	punct	_	TokenRange=27:28
7	sempre	sempre	ADV	_	_	8	advmod	_	TokenRange=29:35
8	encontrava	encontrar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	4	parataxis	_	TokenRange=36:46
9	penas	pena	NOUN	_	Gender=Fem|Number=Plur	8	obj	_	TokenRange=47:52
10	de	de	ADP	_	_	11	case	_	TokenRange=53:55
11	pássaro	pássaro	NOUN	_	Gender=Masc|Number=Sing	9	nmod	_	SpaceAfter=No|TokenRange=56:63
12	.	.	PUNCT	_	_	4	punct	_	SpaceAfter=No|TokenRange=63:64

# generator = UDPipe 2, https://lindat.mff.cuni.cz/services/udpipe
# udpipe_model = portuguese-bosque-ud-2.10-220711
# udpipe_model_licence = CC BY-NC-SA
# reviewer = Leonel Figueiredo de Alencar (LFdeA)
# title = Da tartaruga e o gavião (Rodrigues, 1890)
# sent_id = 3b
# text = O filho ia caçar camaleões, sempre encontrava penas de pássaro.
1	O	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	SpacesBefore=\s|TokenRange=1:2
2	filho	filho	NOUN	_	Gender=Masc|Number=Sing	4	nsubj	_	TokenRange=3:8
3	ia	ir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	0	root	_	TokenRange=9:11
4	caçar	caçar	VERB	_	VerbForm=Inf	3	xcomp	_	TokenRange=12:17
5	camaleões	camaleão	NOUN	_	Gender=Masc|Number=Plur	4	obj	_	SpaceAfter=No|TokenRange=18:27
6	,	,	PUNCT	_	_	8	punct	_	TokenRange=27:28
7	sempre	sempre	ADV	_	_	8	advmod	_	TokenRange=29:35
8	encontrava	encontrar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	3	parataxis	_	TokenRange=36:46
9	penas	pena	NOUN	_	Gender=Fem|Number=Plur	8	obj	_	TokenRange=47:52
10	de	de	ADP	_	_	11	case	_	TokenRange=53:55
11	pássaro	pássaro	NOUN	_	Gender=Masc|Number=Sing	9	nmod	_	SpaceAfter=No|TokenRange=56:63
12	.	.	PUNCT	_	_	3	punct	_	SpaceAfter=No|TokenRange=63:64

>>> import re
>>> pat=re.compile(r" text =.+")
>>> type(pat)
<class 're.Pattern'>
>>> pat.search(text)
<re.Match object; span=(272, 343), match=' text = O filho ia caçar camaleões, sempre encont>
>>> m=pat.search(text)
>>> m.group()
' text = O filho ia caçar camaleões, sempre encontrava penas de pássaro.'
>>> pat=re.compile(r" text =(.+)")
>>> pat.search(text)
<re.Match object; span=(272, 343), match=' text = O filho ia caçar camaleões, sempre encont>
>>> m=pat.search(text)
>>> m.group()
' text = O filho ia caçar camaleões, sempre encontrava penas de pássaro.'
>>> m.groups()
(' O filho ia caçar camaleões, sempre encontrava penas de pássaro.',)
>>> tupla=m.groups()
>>> type(tupla)
<class 'tuple'>
>>> len(tupla)
1
>>> tupla[0]
' O filho ia caçar camaleões, sempre encontrava penas de pássaro.'
>>> pat=re.compile(r" text = (.+)")
>>> m=pat.search(text)
>>> tupla=m.groups()
>>> tupla[0]
'O filho ia caçar camaleões, sempre encontrava penas de pássaro.'
>>> sent=tupla[0]
>>> pat=re.compile(r"[A-Z]{3,}")
>>> upos_tags=[]
>>> upos_tags=pat.findall(text)
>>> len(upos_tags)
26
>>> for t in upos_tags:
	print(t, end=' ')

	
UDP DET NOUN AUX VERB NOUN PUNCT ADV VERB NOUN ADP NOUN PUNCT UDP DET NOUN VERB VERB NOUN PUNCT ADV VERB NOUN ADP NOUN PUNCT 
>>> pat=re.compile(r"\b[A-Z]{3,}\b")
>>> upos_tags=pat.findall(text)
>>> len(upos_tags)
24
>>> 'UDP' in upos_tags
False
>>> s='''xyz, jkl (abc) ktr: juy-io (defg) TR; ko.'''
>>> pat=re.compile(r"\([\)]+\)")
>>> pat.findall(s)
[]
>>> pat=re.compile(r"\([^)]+\)")
>>> pat.findall(s)
['(abc)', '(defg)']
>>> s='''xyz, jkl (abc ghi: hu) ktr: juy-io (def  g) TR; ko.'''
>>> pat.findall(s)
['(abc ghi: hu)', '(def  g)']
>>> s='''xyz, jkl ((abc ghi: hu)) ktr: juy-io (def  g) TR; ko.'''
>>> pat.findall(s)
['((abc ghi: hu)', '(def  g)']
>>> pat=re.compile(r"\(([^)]+)\)")
>>> pat.findall(s)
['(abc ghi: hu', 'def  g']
>>> pat=re.compile(r"\(([^\()]+)\)")
>>> pat.findall(s)
['abc ghi: hu', 'def  g']
>>> xml='''<entry>
  <headword>whale</headword>
  <pos>noun</pos>
  <sense>
    <gloss>any of the larger cetacean mammals having a streamlined
      body and breathing through a blowhole on the head</gloss>
    <synset>whale.n.02</synset>
  </sense>
  <sense>
    <gloss>a very large person; impressive in size or qualities</gloss>
    <synset>giant.n.04</synset>
  </sense>
</entry>'''
>>> pat=re.compile(r"<[^>]+>(.+)<[^>]+>")
>>> pat.findall(xml)
['whale', 'noun', 'whale.n.02', 'a very large person; impressive in size or qualities', 'giant.n.04']
>>> xml='''<entry>
  <headword>whale</headword>
  <pos>noun</pos>
  <sense>
    <gloss>any of the larger cetacean mammals having a streamlined
      body and breathing through a blowhole on the head</gloss>
    <synset>whale.n.02</synset>
  </sense>
  <sense>
    <gloss>a very large person; impressive
    in size or qualities</gloss>
    <synset>giant.n.04</synset>
  </sense>
</entry>'''
>>> pat.findall(xml)
['whale', 'noun', 'whale.n.02', 'giant.n.04']
>>> pat=re.compile(r"(?m)<[^>]+>(.+)<[^>]+>")
>>> pat.findall(xml)
['whale', 'noun', 'whale.n.02', 'giant.n.04']
>>> pat=re.compile(r"(?m)<[^>]+>(.+)</[^>]+>")
>>> pat.findall(xml)
['whale', 'noun', 'whale.n.02', 'giant.n.04']
>>> pat=re.compile(r"(?m)<[^>]+>(.+)<\/[^>]+>")
>>> pat.findall(xml)
['whale', 'noun', 'whale.n.02', 'giant.n.04']
>>> xml='''<entry>
  <headword>whale</headword>
  <pos>noun</pos>
  <sense>
    <gloss>any of the larger cetacean mammals having a streamlined
      body and breathing through a blowhole on the head</gloss>
    <synset>whale.n.02</synset>
  </sense>
  <sense>
    <gloss>a very large person; impressive in size or qualities</gloss>
    <synset>giant.n.04</synset>
  </sense>
</entry>'''
>>> pat.findall(xml)
['whale', 'noun', 'whale.n.02', 'a very large person; impressive in size or qualities', 'giant.n.04']
>>> xml='''<entry>
  <headword>whale</headword>
  <pos>noun</pos>
  <sense>
    <gloss>any of the larger cetacean mammals having a streamlined body and breathing through a blowhole on the head</gloss>
    <synset>whale.n.02</synset>
  </sense>
  <sense>
    <gloss>a very large person; impressive in size or qualities</gloss>
    <synset>giant.n.04</synset>
  </sense>
</entry>'''
>>> pat.findall(xml)
['whale', 'noun', 'any of the larger cetacean mammals having a streamlined body and breathing through a blowhole on the head', 'whale.n.02', 'a very large person; impressive in size or qualities', 'giant.n.04']
>>> marco=re.compile(r"(?m)<[^>]+>(.+)<\/[^>]+>")
>>> leo=re.compile(r"<[^>]+>(.+)<[^>]+>")
>>> marco.findall(xml)
['whale', 'noun', 'any of the larger cetacean mammals having a streamlined body and breathing through a blowhole on the head', 'whale.n.02', 'a very large person; impressive in size or qualities', 'giant.n.04']
>>> leo.findall(xml)
['whale', 'noun', 'any of the larger cetacean mammals having a streamlined body and breathing through a blowhole on the head', 'whale.n.02', 'a very large person; impressive in size or qualities', 'giant.n.04']
>>> xml='''<entry>
  <headword>whale</headword>
  <pos>noun</pos>
  <sense>
    <gloss>any of the larger cetacean mammals having a streamlined
      body and breathing through a blowhole on the head</gloss>
    <synset>whale.n.02</synset>
  </sense>
  <sense>
    <gloss>a very large person; impressive in size or qualities</gloss>
    <synset>giant.n.04</synset>
  </sense>
</entry>'''
>>> xml=re.sub(r"\n",' ',xml)
>>> leo.findall(xml)
['   <headword>whale</headword>   <pos>noun</pos>   <sense>     <gloss>any of the larger cetacean mammals having a streamlined       body and breathing through a blowhole on the head</gloss>     <synset>whale.n.02</synset>   </sense>   <sense>     <gloss>a very large person; impressive in size or qualities</gloss>     <synset>giant.n.04</synset>   </sense> ']
>>> marco.findall(xml)
['   <headword>whale</headword>   <pos>noun</pos>   <sense>     <gloss>any of the larger cetacean mammals having a streamlined       body and breathing through a blowhole on the head</gloss>     <synset>whale.n.02</synset>   </sense>   <sense>     <gloss>a very large person; impressive in size or qualities</gloss>     <synset>giant.n.04</synset>   </sense> ']
>>> xml
'<entry>   <headword>whale</headword>   <pos>noun</pos>   <sense>     <gloss>any of the larger cetacean mammals having a streamlined       body and breathing through a blowhole on the head</gloss>     <synset>whale.n.02</synset>   </sense>   <sense>     <gloss>a very large person; impressive in size or qualities</gloss>     <synset>giant.n.04</synset>   </sense> </entry>'
>>> leo=re.compile(r"<[^>]+>([^<]+)<[^>]+>")
>>> leo.findall(xml)
['   ', '   ', '   ', 'any of the larger cetacean mammals having a streamlined       body and breathing through a blowhole on the head', 'whale.n.02', '   ', 'a very large person; impressive in size or qualities', 'giant.n.04', ' ']
>>> marco=re.compile(r"(?m)<[^>]+>([^<]+)<\/[^>]+>")
>>> marco.findall(xml)
['whale', 'noun', 'any of the larger cetacean mammals having a streamlined       body and breathing through a blowhole on the head', 'whale.n.02', 'a very large person; impressive in size or qualities', 'giant.n.04', ' ']
>>> print(xml)
<entry>   <headword>whale</headword>   <pos>noun</pos>   <sense>     <gloss>any of the larger cetacean mammals having a streamlined       body and breathing through a blowhole on the head</gloss>     <synset>whale.n.02</synset>   </sense>   <sense>     <gloss>a very large person; impressive in size or qualities</gloss>     <synset>giant.n.04</synset>   </sense> </entry>
>>> xml='''<entry>
  <headword>whale</headword>
  <pos>noun</pos>
  <sense>
    <gloss>any of the larger cetacean mammals having a streamlined
      body and breathing through a blowhole on the head</gloss>
    <synset>whale.n.02</synset>
  </sense>
  <sense>
    <gloss>a very large person; impressive in size or qualities</gloss>
    <synset>giant.n.04</synset>
  </sense>
</entry>'''
>>> re.sub(r"</?[^>]+>",'',xml)
'\n  whale\n  noun\n  \n    any of the larger cetacean mammals having a streamlined\n      body and breathing through a blowhole on the head\n    whale.n.02\n  \n  \n    a very large person; impressive in size or qualities\n    giant.n.04\n  \n'
>>> print(re.sub(r"</?[^>]+>",'',xml))

  whale
  noun
  
    any of the larger cetacean mammals having a streamlined
      body and breathing through a blowhole on the head
    whale.n.02
  
  
    a very large person; impressive in size or qualities
    giant.n.04
  

>>> text=re.sub(r"</?[^>]+>",'',xml)
>>> re.sub(r"\s+"," ")
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#94>", line 1, in <module>
TypeError: sub() missing 1 required positional argument: 'string'
>>> re.sub(r"\s+"," ",text)
' whale noun any of the larger cetacean mammals having a streamlined body and breathing through a blowhole on the head whale.n.02 a very large person; impressive in size or qualities giant.n.04 '
>>> marco=re.compile(r"(?m)<[^/>]+>([^<]+)<\/[^>]+>")
>>> xml='''<entry>
  <headword>whale</headword>
  <pos>noun</pos>
  <sense>
    <gloss>any of the larger cetacean mammals having a streamlined
      body and breathing through a blowhole on the head</gloss>
    <synset>whale.n.02</synset>
  </sense>
  <sense>
    <gloss>a very large person; impressive in size or qualities</gloss>
    <synset>giant.n.04</synset>
  </sense>
</entry>'''
>>> xml=re.sub(r"\n",' ',xml)
>>> marco.findall(xml)
['whale', 'noun', 'any of the larger cetacean mammals having a streamlined       body and breathing through a blowhole on the head', 'whale.n.02', 'a very large person; impressive in size or qualities', 'giant.n.04']
>>> 