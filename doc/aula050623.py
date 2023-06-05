Python 3.8.10 (default, Mar 13 2023, 10:26:41) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import AnnotateConllu
>>> s='''Pituna ukiri uikú ií ripí-pe. (p. 164) - A noite estava dormindo no fundo da água. - Pitúna okệri oikộ ɨ rɨpɨpe.'''
>>> AnnotateConllu.parseExample(s,'Magalhaes1876',1,1,2)
# sent_id = Magalhaes1876:1:1:2
# text = Pituna ukiri uikú ií ripí-pe.
# text_eng = The night was sleeping at the bottom of the water.
# text_por = A noite estava dormindo no fundo da água.
# text_source = p. 164
# text_orig = Pitúna okệri oikộ ɨ rɨpɨpe.
# text_annotator = LFdeA
1	Pituna	pituna	NOUN	N	Number=Sing	2	nsubj	_	TokenRange=0:6
2	ukiri	kiri	VERB	V	Person=3|VerbForm=Fin	0	root	_	TokenRange=7:12
3	uikú	ikú	AUX	AUXFS	Person=3|VerbForm=Fin	2	aux	_	TokenRange=13:17
4	ií	ií	NOUN	N	Number=Sing	5	nmod:poss	_	TokenRange=18:20
5-6	ripí-pe	_	_	_	_	_	_	_	SpaceAfter=No|TokenRange=21:29
5	ripí	tipí	NOUN	N	Number=Sing|Rel=Cont	2	obl	_	_
6	pe	upé	ADP	ADP	Clitic=Yes	5	case	_	_
7	.	.	PUNCT	PUNCT	_	2	punct	_	SpaceAfter=No|TokenRange=30:31


>>> s='''Marupí/@ taá ne rapé? (Hartt, 358, adap.) -  Por onde é o teu caminho?'''
>>> AnnotateConllu.checkSentence(s)
False
>>> AnnotateConllu.parseExample(s,'Avila2021',0,0,571)
# sent_id = Avila2021:0:0:571
# text = Marupí taá ne rapé?
# text_eng = Where is your path?
# text_por = Por onde é o teu caminho?
# text_source = Hartt, 358, adap.
# text_annotator = LFdeA
1	Marupí	marupí	ADV	ADVLC	AdvType=Loc|PronType=Rel	0	root	_	TokenRange=0:6
1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	advmod	_	TokenRange=0:6
2	taá	taá	PART	CQ	PartType=Int	1	advmod	_	TokenRange=7:10
3	ne	ne	PRON	PRON2	Case=Gen|Number=Sing|Person=2|Poss=Yes|PronType=Prs	4	nmod:poss	_	TokenRange=11:13
4	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	1	_	_	SpaceAfter=No|TokenRange=14:18
5	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=18:19


>>> s='''Marupí/advrc@ taá ne rapé? (Hartt, 358, adap.) -  Por onde é o teu caminho?'''
>>> AnnotateConllu.parseExample(s,'Avila2021',0,0,571)
# sent_id = Avila2021:0:0:571
# text = Marupí taá ne rapé?
# text_eng = Where is your path?
# text_por = Por onde é o teu caminho?
# text_source = Hartt, 358, adap.
# text_annotator = LFdeA
1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	taá	taá	PART	CQ	PartType=Int	1	advmod	_	TokenRange=7:10
3	ne	ne	PRON	PRON2	Case=Gen|Number=Sing|Person=2|Poss=Yes|PronType=Prs	4	nmod:poss	_	TokenRange=11:13
4	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	1	nsubj	_	SpaceAfter=No|TokenRange=14:18
5	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=18:19


>>> s='''Marupí/advrc@ se rapé, se ramunha? (Rodrigues, 77, adap.) -  Por onde é o meu caminho, meu avô?'''
>>> parse(s):
	
SyntaxError: invalid syntax
>>> def parse(s,pref,textid,index,sentid):
	if not AnnotateConllu.checkSentence(s):
		AnnotateConllu.parseExample(s,pref,textid,index,sentid)

		
>>> parse(s)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#14>", line 1, in <module>
TypeError: parse() missing 4 required positional arguments: 'pref', 'textid', 'index', and 'sentid'
>>> parse(s,'Avila2021',0,0,572)
# sent_id = Avila2021:0:0:572
# text = Marupí se rapé, se ramunha?
# text_eng = Where is my path, my grandfather?
# text_por = Por onde é o meu caminho, meu avô?
# text_source = Rodrigues, 77, adap.
# text_annotator = LFdeA
1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	3	nmod:poss	_	TokenRange=7:9
3	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	6	nmod:poss	_	SpaceAfter=No|TokenRange=10:14
4	,	,	PUNCT	PUNCT	_	1	punct	_	TokenRange=14:15
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=16:18
6	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	1	nsubj	_	SpaceAfter=No|TokenRange=19:26
7	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=26:27


>>> tk=AnnotateConllu.parseSentence('Marupí/advrc@ se rapé, se ramunha?')
>>> from importlib import reload
>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> AnnotateConllu.handleVocative(tk)
>>> print(tk.serialize())
1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	3	nmod:poss	_	TokenRange=7:9
3	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	6	nmod:poss	_	SpaceAfter=No|TokenRange=10:14
4	,	,	PUNCT	PUNCT	_	1	punct	_	TokenRange=14:15
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=16:18
6	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	1	vocative	_	SpaceAfter=No|TokenRange=19:26
7	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=26:27


>>> tk=AnnotateConllu.parseSentence('Marupí/advrc@ se rapé, ramunha?')
>>> tk=AnnotateConllu.parseSentence('Marupí/advrc@ se rapé, Maria?')
>>> AnnotateConllu.handleVocative(tk)
>>> print(tk.serialize())
1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	3	nmod:poss	_	TokenRange=7:9
3	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	5	nmod:poss	_	SpaceAfter=No|TokenRange=10:14
4	,	,	PUNCT	PUNCT	_	1	punct	_	TokenRange=14:15
5	Maria	maria	PROPN	PROPN	_	1	vocative	_	SpaceAfter=No|TokenRange=16:21
6	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=21:22


>>> t1=tk[0]
>>> t1
{'id': 1, 'form': 'Marupí', 'lemma': 'marupí', 'upos': 'ADV', 'xpos': 'ADVRC', 'feats': {'AdvType': 'Loc', 'PronType': 'Int'}, 'head': 0, 'deprel': 'root', 'deps': None, 'misc': {'TokenRange': '0:6'}}
>>> AnnotateConllu.getPreviousToken(t1,tk)
>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> tk=AnnotateConllu.parseSentence('Maria, marupí/advrc@ se rapé?')
>>> AnnotateConllu.handleVocative(tk)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#30>", line 1, in <module>
  File "/home/leonel/scripts/AnnotateConllu.py", line 1229, in handleVocative
    if previous['upos'] == 'PUNCT':
TypeError: 'NoneType' object is not subscriptable
>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> tk=AnnotateConllu.parseSentence('Maria, marupí/advrc@ se rapé?')
>>> AnnotateConllu.handleVocative(tk)
>>> print(tk.serialize())
1	Maria	maria	PROPN	PROPN	_	3	vocative	_	SpaceAfter=No|TokenRange=0:5
2	,	,	PUNCT	PUNCT	_	3	punct	_	TokenRange=5:6
3	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=7:13
4	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	5	nmod:poss	_	TokenRange=14:16
5	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	3	nsubj	_	SpaceAfter=No|TokenRange=17:21
6	?	?	PUNCT	PUNCT	_	3	punct	_	SpaceAfter=No|TokenRange=21:22


>>> s='''Maria, marupí/advrc@ se rapé?
Se ramunha, marupí/advrc@ se rapé?
Marupí/advrc@ se rapé, Maria?
Marupí/advrc@ se rapé, se ramunha?'''
>>> for f in s.split('\n'):
	tk=AnnotateConllu.parseSentence(f)
	print(tk.serialize())

	
1	Maria	maria	PROPN	PROPN	_	3	nsubj	_	SpaceAfter=No|TokenRange=0:5
2	,	,	PUNCT	PUNCT	_	3	punct	_	TokenRange=5:6
3	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=7:13
4	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	5	nmod:poss	_	TokenRange=14:16
5	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	3	nsubj	_	SpaceAfter=No|TokenRange=17:21
6	?	?	PUNCT	PUNCT	_	3	punct	_	SpaceAfter=No|TokenRange=21:22


1	Se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	2	nmod:poss	_	TokenRange=0:2
2	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	4	nsubj	_	SpaceAfter=No|TokenRange=3:10
3	,	,	PUNCT	PUNCT	_	4	punct	_	TokenRange=10:11
4	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=12:18
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=19:21
6	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	4	nsubj	_	SpaceAfter=No|TokenRange=22:26
7	?	?	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=26:27


1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	3	nmod:poss	_	TokenRange=7:9
3	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	5	nmod:poss	_	SpaceAfter=No|TokenRange=10:14
4	,	,	PUNCT	PUNCT	_	1	punct	_	TokenRange=14:15
5	Maria	maria	PROPN	PROPN	_	1	nsubj	_	SpaceAfter=No|TokenRange=16:21
6	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=21:22


1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	3	nmod:poss	_	TokenRange=7:9
3	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	6	nmod:poss	_	SpaceAfter=No|TokenRange=10:14
4	,	,	PUNCT	PUNCT	_	1	punct	_	TokenRange=14:15
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=16:18
6	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	1	nsubj	_	SpaceAfter=No|TokenRange=19:26
7	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=26:27


>>> for f in s.split('\n'):
	tk=AnnotateConllu.parseSentence(f)
	AnnotateConllu.handleVocative(tk)
	print(tk.serialize())

	
1	Maria	maria	PROPN	PROPN	_	3	vocative	_	SpaceAfter=No|TokenRange=0:5
2	,	,	PUNCT	PUNCT	_	3	punct	_	TokenRange=5:6
3	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=7:13
4	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	5	nmod:poss	_	TokenRange=14:16
5	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	3	nsubj	_	SpaceAfter=No|TokenRange=17:21
6	?	?	PUNCT	PUNCT	_	3	punct	_	SpaceAfter=No|TokenRange=21:22


1	Se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	2	nmod:poss	_	TokenRange=0:2
2	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	4	vocative	_	SpaceAfter=No|TokenRange=3:10
3	,	,	PUNCT	PUNCT	_	4	punct	_	TokenRange=10:11
4	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=12:18
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=19:21
6	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	4	nsubj	_	SpaceAfter=No|TokenRange=22:26
7	?	?	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=26:27


1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	3	nmod:poss	_	TokenRange=7:9
3	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	5	nmod:poss	_	SpaceAfter=No|TokenRange=10:14
4	,	,	PUNCT	PUNCT	_	1	punct	_	TokenRange=14:15
5	Maria	maria	PROPN	PROPN	_	1	vocative	_	SpaceAfter=No|TokenRange=16:21
6	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=21:22


1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	3	nmod:poss	_	TokenRange=7:9
3	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	6	nmod:poss	_	SpaceAfter=No|TokenRange=10:14
4	,	,	PUNCT	PUNCT	_	1	punct	_	TokenRange=14:15
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=16:18
6	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	1	vocative	_	SpaceAfter=No|TokenRange=19:26
7	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=26:27


>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> for f in s.split('\n'):
	tk=AnnotateConllu.parseSentence(f)
	AnnotateConllu.handleVocative(tk)
	print(tk.serialize())

	
1	Maria	maria	PROPN	PROPN	_	3	vocative	_	SpaceAfter=No|TokenRange=0:5
2	,	,	PUNCT	PUNCT	_	3	punct	_	TokenRange=5:6
3	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=7:13
4	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	5	nmod:poss	_	TokenRange=14:16
5	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	3	nsubj	_	SpaceAfter=No|TokenRange=17:21
6	?	?	PUNCT	PUNCT	_	3	punct	_	SpaceAfter=No|TokenRange=21:22


1	Se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	2	nmod:poss	_	TokenRange=0:2
2	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	4	vocative	_	SpaceAfter=No|TokenRange=3:10
3	,	,	PUNCT	PUNCT	_	4	punct	_	TokenRange=10:11
4	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=12:18
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=19:21
6	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	4	nsubj	_	SpaceAfter=No|TokenRange=22:26
7	?	?	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=26:27


Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#48>", line 3, in <module>
  File "/home/leonel/scripts/AnnotateConllu.py", line 1235, in handleVocative
    mkVocative(token,beforeprevious)
UnboundLocalError: local variable 'beforeprevious' referenced before assignment
>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> for f in s.split('\n'):
	tk=AnnotateConllu.parseSentence(f)
	AnnotateConllu.handleVocative(tk)
	print(tk.serialize())

	
1	Maria	maria	PROPN	PROPN	_	3	vocative	_	SpaceAfter=No|TokenRange=0:5
2	,	,	PUNCT	PUNCT	_	3	punct	_	TokenRange=5:6
3	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=7:13
4	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	5	nmod:poss	_	TokenRange=14:16
5	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	3	nsubj	_	SpaceAfter=No|TokenRange=17:21
6	?	?	PUNCT	PUNCT	_	3	punct	_	SpaceAfter=No|TokenRange=21:22


1	Se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	2	nmod:poss	_	TokenRange=0:2
2	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	4	vocative	_	SpaceAfter=No|TokenRange=3:10
3	,	,	PUNCT	PUNCT	_	4	punct	_	TokenRange=10:11
4	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=12:18
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=19:21
6	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	4	nsubj	_	SpaceAfter=No|TokenRange=22:26
7	?	?	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=26:27


Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#51>", line 3, in <module>
  File "/home/leonel/scripts/AnnotateConllu.py", line 1235, in handleVocative
    mkVocative(token,previous)
  File "/home/leonel/scripts/AnnotateConllu.py", line 1224, in mkVocative
    punct['head'] = token['id']
NameError: name 'punct' is not defined
>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> for f in s.split('\n'):
	tk=AnnotateConllu.parseSentence(f)
	AnnotateConllu.handleVocative(tk)
	print(tk.serialize())

	
1	Maria	maria	PROPN	PROPN	_	3	vocative	_	SpaceAfter=No|TokenRange=0:5
2	,	,	PUNCT	PUNCT	_	3	punct	_	TokenRange=5:6
3	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=7:13
4	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	5	nmod:poss	_	TokenRange=14:16
5	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	3	nsubj	_	SpaceAfter=No|TokenRange=17:21
6	?	?	PUNCT	PUNCT	_	3	punct	_	SpaceAfter=No|TokenRange=21:22


1	Se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	2	nmod:poss	_	TokenRange=0:2
2	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	4	vocative	_	SpaceAfter=No|TokenRange=3:10
3	,	,	PUNCT	PUNCT	_	4	punct	_	TokenRange=10:11
4	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=12:18
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=19:21
6	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	4	nsubj	_	SpaceAfter=No|TokenRange=22:26
7	?	?	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=26:27


1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	3	nmod:poss	_	TokenRange=7:9
3	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	5	nmod:poss	_	SpaceAfter=No|TokenRange=10:14
4	,	,	PUNCT	PUNCT	_	5	punct	_	TokenRange=14:15
5	Maria	maria	PROPN	PROPN	_	1	vocative	_	SpaceAfter=No|TokenRange=16:21
6	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=21:22


1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	3	nmod:poss	_	TokenRange=7:9
3	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	6	nmod:poss	_	SpaceAfter=No|TokenRange=10:14
4	,	,	PUNCT	PUNCT	_	6	punct	_	TokenRange=14:15
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=16:18
6	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	1	vocative	_	SpaceAfter=No|TokenRange=19:26
7	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=26:27


>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> for f in s.split('\n'):
	tk=AnnotateConllu.parseSentence(f)
	AnnotateConllu.handleVocative(tk)
	print(tk.serialize())

	
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#57>", line 3, in <module>
  File "/home/leonel/scripts/AnnotateConllu.py", line 1248, in handleVocative
    mkVocative(token,beforeprevious)
UnboundLocalError: local variable 'beforeprevious' referenced before assignment
>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> for f in s.split('\n'):
	tk=AnnotateConllu.parseSentence(f)
	AnnotateConllu.handleVocative(tk)
	print(tk.serialize())

	
1	Maria	maria	PROPN	PROPN	_	3	vocative	_	SpaceAfter=No|TokenRange=0:5
2	,	,	PUNCT	PUNCT	_	1	punct	_	TokenRange=5:6
3	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=7:13
4	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	5	nmod:poss	_	TokenRange=14:16
5	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	3	nsubj	_	SpaceAfter=No|TokenRange=17:21
6	?	?	PUNCT	PUNCT	_	3	punct	_	SpaceAfter=No|TokenRange=21:22


1	Se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	2	nmod:poss	_	TokenRange=0:2
2	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	4	vocative	_	SpaceAfter=No|TokenRange=3:10
3	,	,	PUNCT	PUNCT	_	4	punct	_	TokenRange=10:11
4	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=12:18
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=19:21
6	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	4	nsubj	_	SpaceAfter=No|TokenRange=22:26
7	?	?	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=26:27


1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	3	nmod:poss	_	TokenRange=7:9
3	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	5	nmod:poss	_	SpaceAfter=No|TokenRange=10:14
4	,	,	PUNCT	PUNCT	_	5	punct	_	TokenRange=14:15
5	Maria	maria	PROPN	PROPN	_	1	vocative	_	SpaceAfter=No|TokenRange=16:21
6	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=21:22


1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	3	nmod:poss	_	TokenRange=7:9
3	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	6	nmod:poss	_	SpaceAfter=No|TokenRange=10:14
4	,	,	PUNCT	PUNCT	_	6	punct	_	TokenRange=14:15
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=16:18
6	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	1	vocative	_	SpaceAfter=No|TokenRange=19:26
7	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=26:27


>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> for f in s.split('\n'):
	tk=AnnotateConllu.parseSentence(f)
	AnnotateConllu.handleVocative(tk)
	print(tk.serialize())

	
1	Maria	maria	PROPN	PROPN	_	3	vocative	_	SpaceAfter=No|TokenRange=0:5
2	,	,	PUNCT	PUNCT	_	1	punct	_	TokenRange=5:6
3	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=7:13
4	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	5	nmod:poss	_	TokenRange=14:16
5	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	3	nsubj	_	SpaceAfter=No|TokenRange=17:21
6	?	?	PUNCT	PUNCT	_	3	punct	_	SpaceAfter=No|TokenRange=21:22


1	Se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	2	nmod:poss	_	TokenRange=0:2
2	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	4	vocative	_	SpaceAfter=No|TokenRange=3:10
3	,	,	PUNCT	PUNCT	_	2	punct	_	TokenRange=10:11
4	marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=12:18
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=19:21
6	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	4	nsubj	_	SpaceAfter=No|TokenRange=22:26
7	?	?	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=26:27


1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	3	nmod:poss	_	TokenRange=7:9
3	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	5	nmod:poss	_	SpaceAfter=No|TokenRange=10:14
4	,	,	PUNCT	PUNCT	_	5	punct	_	TokenRange=14:15
5	Maria	maria	PROPN	PROPN	_	1	vocative	_	SpaceAfter=No|TokenRange=16:21
6	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=21:22


1	Marupí	marupí	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=0:6
2	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	3	nmod:poss	_	TokenRange=7:9
3	rapé	pé	NOUN	N	Number=Sing|Rel=Cont	6	nmod:poss	_	SpaceAfter=No|TokenRange=10:14
4	,	,	PUNCT	PUNCT	_	6	punct	_	TokenRange=14:15
5	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	6	nmod:poss	_	TokenRange=16:18
6	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	1	vocative	_	SpaceAfter=No|TokenRange=19:26
7	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=26:27


>>> s='''Se ramunha, ti ana makití/advnl asú-kwáu. (Rodrigues, 187, adap.) -  Meu avô, não posso mais ir a lugar nenhum.'''
>>> parse(s,'Avila2021',0,0,573)
# sent_id = Avila2021:0:0:573
# text = Se ramunha, ti ana makití asú-kwáu.
# text_eng = My grandfather, I can't go anywhere anymore.
# text_por = Meu avô, não posso mais ir a lugar nenhum.
# text_source = Rodrigues, 187, adap.
# text_annotator = LFdeA
1	Se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	2	nmod:poss	_	TokenRange=0:2
2	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	7	nsubj	_	SpaceAfter=No|TokenRange=3:10
3	,	,	PUNCT	PUNCT	_	7	punct	_	TokenRange=10:11
4	ti	ti	PART	NEG	PartType=Neg|Polarity=Neg	7	advmod	_	TokenRange=12:14
5	ana	ana	PART	PFV	Aspect=Perf	7	advmod	_	TokenRange=15:18
6	makití	makití	ADV	ADVLC	AdvType=Loc|PronType=Rel	7	advmod	_	TokenRange=19:25
6	makití	makití	ADV	ADVRC	AdvType=Loc|PronType=Int	7	advmod	_	TokenRange=19:25
7-8	asú-kwáu	_	_	_	_	_	_	_	SpaceAfter=No|TokenRange=26:34
7	asú	sú	VERB	V	Number=Sing|Person=1|VerbForm=Fin	5	acl:relcl	_	_
8	kwáu	kwáu	AUX	AUXN	Compound=Yes|VerbForm=Inf	7	aux	_	_
9	.	.	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=35:36


>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> parse(s,'Avila2021',0,0,573)
# sent_id = Avila2021:0:0:573
# text = Se ramunha, ti ana makití asú-kwáu.
# text_eng = My grandfather, I can't go anywhere anymore.
# text_por = Meu avô, não posso mais ir a lugar nenhum.
# text_source = Rodrigues, 187, adap.
# text_annotator = LFdeA
1	Se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	2	nmod:poss	_	TokenRange=0:2
2	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	7	vocative	_	SpaceAfter=No|TokenRange=3:10
3	,	,	PUNCT	PUNCT	_	2	punct	_	TokenRange=10:11
4	ti	ti	PART	NEG	PartType=Neg|Polarity=Neg	7	advmod	_	TokenRange=12:14
5	ana	ana	PART	PFV	Aspect=Perf	7	advmod	_	TokenRange=15:18
6	makití	makití	ADV	ADVLC	AdvType=Loc|PronType=Rel	7	advmod	_	TokenRange=19:25
6	makití	makití	ADV	ADVRC	AdvType=Loc|PronType=Int	7	advmod	_	TokenRange=19:25
7-8	asú-kwáu	_	_	_	_	_	_	_	SpaceAfter=No|TokenRange=26:34
7	asú	sú	VERB	V	Number=Sing|Person=1|VerbForm=Fin	5	acl:relcl	_	_
8	kwáu	kwáu	AUX	AUXN	Compound=Yes|VerbForm=Inf	7	aux	_	_
9	.	.	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=35:36


>>> parse(s,'Avila2021',0,0,573)
# sent_id = Avila2021:0:0:573
# text = Se ramunha, ti ana makití asú-kwáu.
# text_eng = My grandfather, I can't go anywhere anymore.
# text_por = Meu avô, não posso mais ir a lugar nenhum.
# text_source = Rodrigues, 187, adap.
# text_annotator = LFdeA
1	Se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	2	nmod:poss	_	TokenRange=0:2
2	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	7	vocative	_	SpaceAfter=No|TokenRange=3:10
3	,	,	PUNCT	PUNCT	_	2	punct	_	TokenRange=10:11
4	ti	ti	PART	NEG	PartType=Neg|Polarity=Neg	7	advmod	_	TokenRange=12:14
5	ana	ana	PART	PFV	Aspect=Perf	7	advmod	_	TokenRange=15:18
6	makití	makití	ADV	ADVLC	AdvType=Loc|PronType=Rel	7	advmod	_	TokenRange=19:25
6	makití	makití	ADV	ADVRC	AdvType=Loc|PronType=Int	7	advmod	_	TokenRange=19:25
7-8	asú-kwáu	_	_	_	_	_	_	_	SpaceAfter=No|TokenRange=26:34
7	asú	sú	VERB	V	Number=Sing|Person=1|VerbForm=Fin	5	acl:relcl	_	_
8	kwáu	kwáu	AUX	AUXN	Compound=Yes|VerbForm=Inf	7	aux	_	_
9	.	.	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=35:36


>>> s='''Se ramunha, ti ana makití/advnc asú-kwáu. (Rodrigues, 187, adap.) -  Meu avô, não posso mais ir a lugar nenhum.'''
>>> parse(s,'Avila2021',0,0,573)
# sent_id = Avila2021:0:0:573
# text = Se ramunha, ti ana makití asú-kwáu.
# text_eng = My grandfather, I can't go anywhere anymore.
# text_por = Meu avô, não posso mais ir a lugar nenhum.
# text_source = Rodrigues, 187, adap.
# text_annotator = LFdeA
1	Se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	2	nmod:poss	_	TokenRange=0:2
2	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	7	vocative	_	SpaceAfter=No|TokenRange=3:10
3	,	,	PUNCT	PUNCT	_	2	punct	_	TokenRange=10:11
4	ti	ti	PART	NEG	PartType=Neg|Polarity=Neg	7	advmod	_	TokenRange=12:14
5	ana	ana	PART	PFV	Aspect=Perf	7	advmod	_	TokenRange=15:18
6	makití	makití	ADV	ADVLC	AdvType=Loc|PronType=Rel	7	advmod	_	TokenRange=19:25
6	makití	makití	ADV	ADVRC	AdvType=Loc|PronType=Int	7	advmod	_	TokenRange=19:25
7-8	asú-kwáu	_	_	_	_	_	_	_	SpaceAfter=No|TokenRange=26:34
7	asú	sú	VERB	V	Number=Sing|Person=1|VerbForm=Fin	5	acl:relcl	_	_
8	kwáu	kwáu	AUX	AUXN	Compound=Yes|VerbForm=Inf	7	aux	_	_
9	.	.	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=35:36


>>> parse(s,'Avila2021',0,0,573)
# sent_id = Avila2021:0:0:573
# text = Se ramunha, ti ana makití asú-kwáu.
# text_eng = My grandfather, I can't go anywhere anymore.
# text_por = Meu avô, não posso mais ir a lugar nenhum.
# text_source = Rodrigues, 187, adap.
# text_annotator = LFdeA
1	Se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	2	nmod:poss	_	TokenRange=0:2
2	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	7	vocative	_	SpaceAfter=No|TokenRange=3:10
3	,	,	PUNCT	PUNCT	_	2	punct	_	TokenRange=10:11
4	ti	ti	PART	NEG	PartType=Neg|Polarity=Neg	7	advmod	_	TokenRange=12:14
5	ana	ana	PART	PFV	Aspect=Perf	7	advmod	_	TokenRange=15:18
6	makití	makití	ADV	ADVNC	AdvType=Loc|PronType=Ind	7	advmod	_	TokenRange=19:25
7-8	asú-kwáu	_	_	_	_	_	_	_	SpaceAfter=No|TokenRange=26:34
7	asú	sú	VERB	V	Number=Sing|Person=1|VerbForm=Fin	0	root	_	_
8	kwáu	kwáu	AUX	AUXN	Compound=Yes|VerbForm=Inf	7	aux	_	_
9	.	.	PUNCT	PUNCT	_	7	punct	_	SpaceAfter=No|TokenRange=35:36


>>> s='''Apé tẽ uikú nhaã iwitera makití asú-putari wirandé. -  Lá mesmo está a serra à qual eu quero ir amanhã.'''
>>> parse(s,'Avila2021',0,0,574)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#73>", line 1, in <module>
  File "<pyshell#13>", line 3, in parse
  File "/home/leonel/scripts/AnnotateConllu.py", line 1846, in parseExample
    handleParse(handleSents(sents, pref,textid,index,sentid,annotator),copyboard=copyboard)
  File "/home/leonel/scripts/AnnotateConllu.py", line 1798, in handleSents
    sents[3],
IndexError: list index out of range
>>> s='''Apé tẽ uikú nhaã iwitera makití asú-putari wirandé. (Avila 2021) -  Lá mesmo está a serra à qual eu quero ir amanhã.'''
>>> parse(s,'Avila2021',0,0,574)
# sent_id = Avila2021:0:0:574
# text = Apé tẽ uikú nhaã iwitera makití asú-putari wirandé.
# text_eng = Right there is the mountain I want to go to tomorrow.
# text_por = Lá mesmo está a serra à qual eu quero ir amanhã.
# text_source = Avila 2021
# text_annotator = LFdeA
1	Apé	apé	_	_	_	0	_	_	TokenRange=0:3
2	tẽ	tẽ	PART	FOC	Foc=Yes|PartType=Emp	1	advmod	_	TokenRange=4:6
2	tẽ	tẽ	PART	NEGI	Mood=Imp|PartType=Neg|Polarity=Neg	3	advmod	_	TokenRange=4:6
3	uikú	ikú	VERB	V	Person=3|VerbForm=Fin	0	root	_	TokenRange=7:11
4	nhaã	nhaã	DET	DEMS	Deixis=Remt|Number=Sing|PronType=Dem	5	det	_	TokenRange=12:16
5	iwitera	iwitera	NOUN	N	Number=Sing	3	obj	_	TokenRange=17:24
6	makití	makití	ADV	ADVLC	AdvType=Loc|PronType=Rel	7	advmod	_	TokenRange=25:31
6	makití	makití	ADV	ADVNC	AdvType=Loc|PronType=Ind	3	advmod	_	TokenRange=25:31
6	makití	makití	ADV	ADVRC	AdvType=Loc|PronType=Int	7	advmod	_	TokenRange=25:31
7-8	asú-putari	_	_	_	_	_	_	_	TokenRange=32:42
7	asú	sú	VERB	V	Number=Sing|Person=1|VerbForm=Fin	5	acl:relcl	_	_
8	putari	putari	AUX	AUXN	Compound=Yes|VerbForm=Inf	7	aux	_	_
9	wirandé	wirandé	ADV	ADVT	AdvType=Tim	7	advmod	_	SpaceAfter=No|TokenRange=44:51
10	.	.	PUNCT	PUNCT	_	3	punct	_	SpaceAfter=No|TokenRange=51:52


>>> s='''Ape/advdi tẽ/foc uikú nhaã iwitera makití/advlc asú-putari wirandé. (Avila 2021) -  Lá mesmo está a serra à qual eu quero ir amanhã.'''
>>> s='''Ape/advdi@ tẽ/foc uikú nhaã iwitera makití/advlc asú-putari wirandé. (Avila 2021) -  Lá mesmo está a serra à qual eu quero ir amanhã. - Apé tẽ uikú nhaã iwitera makití asú-putari wirandé.'''
>>> parse(s,'Avila2021',0,0,574)
# sent_id = Avila2021:0:0:574
# text = Ape tẽ uikú nhaã iwitera makití asú-putari wirandé.
# text_eng = Right there is the mountain I want to go to tomorrow.
# text_por = Lá mesmo está a serra à qual eu quero ir amanhã.
# text_source = Avila 2021
# text_orig = Apé tẽ uikú nhaã iwitera makití asú-putari wirandé.
# text_annotator = LFdeA
1	Ape	ape	ADV	ADVDI	AdvType=Loc|Deixis=Remt|PronType=Dem	0	root	_	TokenRange=0:3
2	tẽ	tẽ	PART	FOC	Foc=Yes|PartType=Emp	1	advmod	_	TokenRange=4:6
3	uikú	ikú	VERB	V	Person=3|VerbForm=Fin	1	root	_	TokenRange=7:11
4	nhaã	nhaã	DET	DEMS	Deixis=Remt|Number=Sing|PronType=Dem	5	det	_	TokenRange=12:16
5	iwitera	iwitera	NOUN	N	Number=Sing	3	obj	_	TokenRange=17:24
6	makití	makití	ADV	ADVLC	AdvType=Loc|PronType=Rel	7	advmod	_	TokenRange=25:31
7-8	asú-putari	_	_	_	_	_	_	_	TokenRange=32:42
7	asú	sú	VERB	V	Number=Sing|Person=1|VerbForm=Fin	5	acl:relcl	_	_
8	putari	putari	AUX	AUXN	Compound=Yes|VerbForm=Inf	7	aux	_	_
9	wirandé	wirandé	ADV	ADVT	AdvType=Tim	7	advmod	_	SpaceAfter=No|TokenRange=44:51
10	.	.	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=51:52


>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> parse(s,'Avila2021',0,0,574)
# sent_id = Avila2021:0:0:574
# text = Ape tẽ uikú nhaã iwitera makití asú-putari wirandé.
# text_eng = Right there is the mountain I want to go to tomorrow.
# text_por = Lá mesmo está a serra à qual eu quero ir amanhã.
# text_source = Avila 2021
# text_orig = Apé tẽ uikú nhaã iwitera makití asú-putari wirandé.
# text_annotator = LFdeA
1	Ape	ape	ADV	ADVDI	AdvType=Loc|Deixis=Remt|PronType=Dem	0	root	_	TokenRange=0:3
2	tẽ	tẽ	PART	FOC	Foc=Yes|PartType=Emp	1	advmod	_	TokenRange=4:6
3	uikú	ikú	AUX	COP	Person=3|VerbForm=Fin	1	cop	_	TokenRange=7:11
4	nhaã	nhaã	DET	DEMS	Deixis=Remt|Number=Sing|PronType=Dem	5	det	_	TokenRange=12:16
5	iwitera	iwitera	NOUN	N	Number=Sing	3	obj	_	TokenRange=17:24
6	makití	makití	ADV	ADVLC	AdvType=Loc|PronType=Rel	7	advmod	_	TokenRange=25:31
7-8	asú-putari	_	_	_	_	_	_	_	TokenRange=32:42
7	asú	sú	VERB	V	Number=Sing|Person=1|VerbForm=Fin	5	acl:relcl	_	_
8	putari	putari	AUX	AUXN	Compound=Yes|VerbForm=Inf	7	aux	_	_
9	wirandé	wirandé	ADV	ADVT	AdvType=Tim	7	advmod	_	SpaceAfter=No|TokenRange=44:51
10	.	.	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=51:52


>>> sents=AnnotateConllu.extractConlluSents('corpus/universal-dependencies/yrl_complin-ud-test.conllu')
>>> for sent in sents:
	for token in sent:
		if token['deprel']=='cop' and token['xpos'] =! 'COP':
			
SyntaxError: invalid syntax
>>> sents=AnnotateConllu.extractConlluSents('corpus/universal-dependencies/yrl_complin-ud-test.conllu')
>>> for sent in sents:
	for token in sent:
		if token['deprel']=='cop' and not token['xpos'] == 'COP':
			print(sent.metadata['sent_id'], token['xpos'])
			token['xpos'] = 'COP'

			
Alencar2021:0:0:3 V
Alencar2021:0:0:7 V
Navarro2016:4:3:170 AUXFS
Avila2021:9:1:58 V
Avila2021:9:2:59 V
Avila2021:0:0:87 AUXFS
Avila2021:0:0:343 V
Avila2021:0:0:409 AUXFS
Avila2021:0:0:425 AUXFS
Avila2021:0:0:450 AUXFS
Avila2021:0:0:527 AUXFS
Avila2021:0:0:540 AUXFS
Avila2021:0:0:547 AUXFS
NTLN:0:0:5 AUXFS
>>> lines='''Alencar2021:0:0:3 V
Alencar2021:0:0:7 V
Navarro2016:4:3:170 AUXFS
Avila2021:9:1:58 V
Avila2021:9:2:59 V
Avila2021:0:0:87 AUXFS
Avila2021:0:0:343 V
Avila2021:0:0:409 AUXFS
Avila2021:0:0:425 AUXFS
Avila2021:0:0:450 AUXFS
Avila2021:0:0:527 AUXFS
Avila2021:0:0:540 AUXFS
Avila2021:0:0:547 AUXFS
NTLN:0:0:5 AUXFS'''.split('\n')
>>> len(lines)
14
>>> AnnotateConllu.writeSentsConllu(sents,'corpus/universal-dependencies/yrl_complin-ud-test.edt.conllu')
>>> s='''Se ramunha, ti ana makití/advnc asú-kwáu. (Rodrigues, 187, adap.) -  Meu avô, não posso mais ir a lugar nenhum.'''
>>> AnnotateConllu.TreebankSentence(s,'Avila2021',0,0,573)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#95>", line 1, in <module>
  File "/home/leonel/scripts/AnnotateConllu.py", line 1836, in TreebankSentence
    handleParse(handleSents(sents, pref,textid,index,sentid,annotator),copyboard=copyboard)
  File "/home/leonel/scripts/AnnotateConllu.py", line 1806, in handleSents
    sents[3],
IndexError: list index out of range
>>> AnnotateConllu.parseExample(s,'Avila2021',0,0,573)
# sent_id = Avila2021:0:0:573
# text = Se ramunha, ti ana makití asú-kwáu.
# text_eng = My grandfather, I can't go anywhere anymore.
# text_por = Meu avô, não posso mais ir a lugar nenhum.
# text_source = Rodrigues, 187, adap.
# text_annotator = LFdeA
1	Se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	2	nmod:poss	_	TokenRange=0:2
2	ramunha	tamunha	NOUN	N	Number=Sing|Rel=Cont	7	vocative	_	SpaceAfter=No|TokenRange=3:10
3	,	,	PUNCT	PUNCT	_	2	punct	_	TokenRange=10:11
4	ti	ti	PART	NEG	PartType=Neg|Polarity=Neg	7	advmod	_	TokenRange=12:14
5	ana	ana	PART	PFV	Aspect=Perf	7	advmod	_	TokenRange=15:18
6	makití	makití	ADV	ADVNC	AdvType=Loc|PronType=Ind	7	advmod	_	TokenRange=19:25
7-8	asú-kwáu	_	_	_	_	_	_	_	SpaceAfter=No|TokenRange=26:34
7	asú	sú	VERB	V	Number=Sing|Person=1|VerbForm=Fin	0	root	_	_
8	kwáu	kwáu	AUX	AUXN	Compound=Yes|VerbForm=Inf	7	aux	_	_
9	.	.	PUNCT	PUNCT	_	7	punct	_	SpaceAfter=No|TokenRange=35:36


>>> sents=AnnotateConllu.extractConlluSents('corpus/universal-dependencies/yrl_complin-ud-test.conllu')
>>> for sent in sents:
	for token in sent:
		if token['upos'] == 'ADV':
			feats=token.get('feats')if feats and feats.get('PronType') == 'Int'
			
SyntaxError: invalid syntax
>>> sents=AnnotateConllu.extractConlluSents('corpus/universal-dependencies/yrl_complin-ud-test.conllu')
>>> for sent in sents:
	for token in sent:
		if token['upos'] == 'ADV':
			feats=token.get('feats')
			if feats and feats.get('PronType') == 'Int':
				if not sent[-1]['lemma'] == '?':
					print(sent.metadata['sent_id'], token['lemma'], token['xpos'])

					
MooreFP1994:0:0:26 mamé ADVRC
MooreFP1994:1:6:33 mairamé ADVRT
Navarro2016:0:0:61 masuí ADVRC
Navarro2016:0:0:191 mamé ADVRC
Avila2021:6:2:31 masuí ADVRC
Avila2021:0:0:39 mayesawa ADVRA
Avila2021:0:0:44 mamé ADVRC
Avila2021:0:0:45 mayé ADVRA
Avila2021:7:2:48 makití ADVRC
Avila2021:0:0:98 mayé ADVRA
Avila2021:0:0:102 mayé ADVRA
Avila2021:0:0:107 mayé ADVRA
Avila2021:0:0:109 mayé ADVRA
Avila2021:0:0:110 mayé ADVRA
Avila2021:0:0:111 mayé ADVRA
Avila2021:0:0:112 mayé ADVRA
Avila2021:13:2:131 mamé ADVR
Avila2021:0:0:162 makití ADVRC
Avila2021:0:0:222 mayé ADVRA
Avila2021:24:1:245 masuí ADVRC
Avila2021:24:2:246 makití ADVRC
Avila2021:0:0:269 mamé ADVR
Avila2021:0:0:338 mayé ADVRA
Avila2021:0:0:368 mayé ADVRA
Avila2021:0:0:373 mamé ADVR
Avila2021:0:0:404 marupí ADVRC
Avila2021:0:0:405 marupí ADVRC
Avila2021:0:0:409 mamé ADVR
Avila2021:0:0:419 mayé ADVRA
Avila2021:0:0:441 mayé ADVRA
Avila2021:0:0:458 mayé ADVRA
Avila2021:0:0:460 mayé ADVRA
Avila2021:0:0:540 mayé ADVRA
Avila2021:0:0:549 mayé ADVRA
NTLN:0:0:3 mayé ADVRA
NTLN:2:11:22 mayé ADVRA
NTLN:0:0:24 mayé ADVRA
NTLN:5:3:39 mayé ADVRA
Cruz2011:0:0:30 mamé ADVRC
Cruz2011:0:0:34 marupí ADVRC
Casasnovas2006:1:14:14 mayé ADVRA
Casasnovas2006:1:15:15 mayé ADVRA
>>> for sent in sents:
	for token in sent:
		if token['upos'] == 'ADV':
			feats=token.get('feats')
			if feats and feats.get('PronType') == 'Int':
				if not sent[-1]['lemma'] == '?':
					xpos=token['xpos']
					if len(xpos)< 5:
						print(sent.metadata['sent_id'], token['lemma'], xpos)

						
Avila2021:13:2:131 mamé ADVR
Avila2021:0:0:269 mamé ADVR
Avila2021:0:0:373 mamé ADVR
Avila2021:0:0:409 mamé ADVR
>>> for sent in sents:
	for token in sent:
		if token['upos'] == 'ADV':
			feats=token.get('feats')
			if feats and feats.get('PronType') in ('Int','Rel','Ind'):
				xpos=token['xpos']
				if len(xpos)< 5:
					print(sent.metadata['sent_id'], token['lemma'], xpos)

					
Avila2021:13:2:131 mamé ADVR
Avila2021:15:1:163 makití ADVC
Avila2021:0:0:269 mamé ADVR
Avila2021:0:0:373 mamé ADVR
Avila2021:0:0:409 mamé ADVR
Avila2021:0:0:415 mamé ADVR
>>> sents=AnnotateConllu.extractConlluSents('corpus/universal-dependencies/yrl_complin-ud-test.conllu')
>>> for sent in sents:
	for token in sent:
		if token['upos'] == 'ADV':
			feats=token.get('feats')
			if feats and feats.get('PronType') in ('Int','Rel','Ind'):
				xpos=token['xpos']
				if len(xpos)< 5:
					print(sent.metadata['sent_id'], token['lemma'], xpos)

					
Avila2021:15:1:163 makití ADVC
Avila2021:0:0:415 mamé ADVR
>>> sents=AnnotateConllu.extractConlluSents('corpus/universal-dependencies/yrl_complin-ud-test.conllu')
>>> for sent in sents:
	for token in sent:
		if token['upos'] == 'PRON':
			feats=token.get('feats')
			if feats and feats.get('PronType') == 'Int':
				if not sent[-1]['lemma'] == '?':
					print(sent.metadata['sent_id'], token['lemma'], token['xpos'])

					
MooreFP1994:0:0:23 maã INT
Navarro2016:0:0:84 maã INT
Navarro2016:0:0:147 maã INT
Navarro2016:0:0:190 maã INT
Avila2021:0:0:77 maã INT
Avila2021:0:0:137 maã INT
Avila2021:0:0:137 maã INT
Avila2021:0:0:174 awá INT
Avila2021:0:0:276 awá INT
Avila2021:0:0:358 awá INT
Avila2021:0:0:528 maã INT
Cruz2011:0:0:21 awá INT
Cruz2011:0:0:31 maã INT
Cruz2011:0:0:33 maã INT
TerraPreta2013:1:7:7 awá INT
>>> s='''Ape/advdi paá usú nhaã tuyu. | Apekatu ã paá usaã usú, mairamé/sconjr paá uyuíri-putari ã. (Comunidade Indígena Anamuim, 9, adap.) -  Aí dizem que o velho partiu. | Sentiu que já fora longe, quando, dizem, quis retornar. - Then they say the old man left. | He felt that he had already gone far, when, they say, he wanted to return. '''
>>> AnnotateConllu.TreebankSentences(s,'Avila2021',43,1,575)
# sent_id = Avila2021:43:1:575
# text = Ape paá usú nhaã tuyu.
# text_eng = Then they say the old man left.
# text_por = Aí dizem que o velho partiu.
# text_source = Comunidade Indígena Anamuim, 9, adap.
# text_annotator = LFdeA
1	Ape	ape	ADV	ADVDI	AdvType=Loc|Deixis=Remt|PronType=Dem	3	advmod	_	TokenRange=0:3
2	paá	paá	PART	RPRT	Evident=Nfh|PartType=Mod	3	advmod	_	TokenRange=4:7
3	usú	sú	VERB	V	Person=3|VerbForm=Fin	0	root	_	TokenRange=8:11
4	nhaã	nhaã	DET	DEMS	Deixis=Remt|Number=Sing|PronType=Dem	5	det	_	TokenRange=12:16
5	tuyu	tuyu	NOUN	N	Number=Sing	3	obj	_	SpaceAfter=No|TokenRange=17:21
6	.	.	PUNCT	PUNCT	_	3	punct	_	SpaceAfter=No|TokenRange=21:22


# sent_id = Avila2021:43:2:576
# text = Apekatu ã paá usaã usú, mairamé paá uyuíri-putari ã.
# text_eng =  He felt that he had already gone far, when, they say, he wanted to return. 
# text_por = Sentiu que já fora longe, quando, dizem, quis retornar.
# text_source = Comunidade Indígena Anamuim, 9, adap.
# text_annotator = LFdeA
1	Apekatu	apekatu	_	_	_	0	_	_	TokenRange=0:7
2	ã	ã	PART	PFV	Aspect=Perf	4	advmod	_	TokenRange=8:9
3	paá	paá	PART	RPRT	Evident=Nfh|PartType=Mod	4	advmod	_	TokenRange=10:13
4	usaã	saã	VERB	V	Person=3|VerbForm=Fin	0	root	_	TokenRange=14:18
5	usú	sú	VERB	V	Person=3|VerbForm=Fin	4	parataxis	_	SpaceAfter=No|TokenRange=19:22
6	,	,	PUNCT	PUNCT	_	9	punct	_	TokenRange=22:23
7	mairamé	mairamé	SCONJ	SCONJR	_	9	mark	_	TokenRange=24:31
8	paá	paá	PART	RPRT	Evident=Nfh|PartType=Mod	5	advmod	_	TokenRange=32:35
9-10	uyuíri-putari	_	_	_	_	_	_	_	TokenRange=36:49
9	uyuíri	yuíri	VERB	V	Person=3|VerbForm=Fin	5	advcl	_	_
10	putari	putari	AUX	AUXN	Compound=Yes|VerbForm=Inf	9	aux	_	_
11	ã	ã	PART	PFV	Aspect=Perf	9	advmod	_	SpaceAfter=No|TokenRange=51:52
12	.	.	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=52:53


>>> s='''Ape/advdi paá usú nhaã tuyu. | Apekatú ã paá usaã usú, mairamé/sconjr paá uyuíri-putari ã. (Comunidade Indígena Anamuim, 9, adap.) -  Aí dizem que o velho partiu. | Sentiu que já fora longe, quando, dizem, quis retornar. - Then they say the old man left. | He felt that he had already gone far, when, they say, he wanted to return. '''
>>> AnnotateConllu.TreebankSentences(s,'Avila2021',43,1,575)
# sent_id = Avila2021:43:1:575
# text = Ape paá usú nhaã tuyu.
# text_eng = Then they say the old man left.
# text_por = Aí dizem que o velho partiu.
# text_source = Comunidade Indígena Anamuim, 9, adap.
# text_annotator = LFdeA
1	Ape	ape	ADV	ADVDI	AdvType=Loc|Deixis=Remt|PronType=Dem	3	advmod	_	TokenRange=0:3
2	paá	paá	PART	RPRT	Evident=Nfh|PartType=Mod	3	advmod	_	TokenRange=4:7
3	usú	sú	VERB	V	Person=3|VerbForm=Fin	0	root	_	TokenRange=8:11
4	nhaã	nhaã	DET	DEMS	Deixis=Remt|Number=Sing|PronType=Dem	5	det	_	TokenRange=12:16
5	tuyu	tuyu	NOUN	N	Number=Sing	3	obj	_	SpaceAfter=No|TokenRange=17:21
6	.	.	PUNCT	PUNCT	_	3	punct	_	SpaceAfter=No|TokenRange=21:22


# sent_id = Avila2021:43:2:576
# text = Apekatú ã paá usaã usú, mairamé paá uyuíri-putari ã.
# text_eng =  He felt that he had already gone far, when, they say, he wanted to return. 
# text_por = Sentiu que já fora longe, quando, dizem, quis retornar.
# text_source = Comunidade Indígena Anamuim, 9, adap.
# text_annotator = LFdeA
1	Apekatú	apekatú	ADJ	A	_	0	_	_	TokenRange=0:7
1	Apekatú	apekatú	ADV	ADVC	AdvType=Loc	4	advmod	_	TokenRange=0:7
2	ã	ã	PART	PFV	Aspect=Perf	4	advmod	_	TokenRange=8:9
3	paá	paá	PART	RPRT	Evident=Nfh|PartType=Mod	4	advmod	_	TokenRange=10:13
4	usaã	saã	VERB	V	Person=3|VerbForm=Fin	0	root	_	TokenRange=14:18
5	usú	sú	VERB	V	Person=3|VerbForm=Fin	4	parataxis	_	SpaceAfter=No|TokenRange=19:22
6	,	,	PUNCT	PUNCT	_	9	punct	_	TokenRange=22:23
7	mairamé	mairamé	SCONJ	SCONJR	_	9	mark	_	TokenRange=24:31
8	paá	paá	PART	RPRT	Evident=Nfh|PartType=Mod	5	advmod	_	TokenRange=32:35
9-10	uyuíri-putari	_	_	_	_	_	_	_	TokenRange=36:49
9	uyuíri	yuíri	VERB	V	Person=3|VerbForm=Fin	5	advcl	_	_
10	putari	putari	AUX	AUXN	Compound=Yes|VerbForm=Inf	9	aux	_	_
11	ã	ã	PART	PFV	Aspect=Perf	9	advmod	_	SpaceAfter=No|TokenRange=51:52
12	.	.	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=52:53


>>> s='''Ape/advdi paá usú nhaã tuyu. | Apekatú/advc ã paá usaã usú, mairamé/sconjr paá uyuíri-putari ã. (Comunidade Indígena Anamuim, 9, adap.) -  Aí dizem que o velho partiu. | Sentiu que já fora longe, quando, dizem, quis retornar. - Then they say the old man left. | He felt that he had already gone far, when, they say, he wanted to return. '''
>>> AnnotateConllu.TreebankSentences(s,'Avila2021',43,1,575)
# sent_id = Avila2021:43:1:575
# text = Ape paá usú nhaã tuyu.
# text_eng = Then they say the old man left.
# text_por = Aí dizem que o velho partiu.
# text_source = Comunidade Indígena Anamuim, 9, adap.
# text_annotator = LFdeA
1	Ape	ape	ADV	ADVDI	AdvType=Loc|Deixis=Remt|PronType=Dem	3	advmod	_	TokenRange=0:3
2	paá	paá	PART	RPRT	Evident=Nfh|PartType=Mod	3	advmod	_	TokenRange=4:7
3	usú	sú	VERB	V	Person=3|VerbForm=Fin	0	root	_	TokenRange=8:11
4	nhaã	nhaã	DET	DEMS	Deixis=Remt|Number=Sing|PronType=Dem	5	det	_	TokenRange=12:16
5	tuyu	tuyu	NOUN	N	Number=Sing	3	obj	_	SpaceAfter=No|TokenRange=17:21
6	.	.	PUNCT	PUNCT	_	3	punct	_	SpaceAfter=No|TokenRange=21:22


# sent_id = Avila2021:43:2:576
# text = Apekatú ã paá usaã usú, mairamé paá uyuíri-putari ã.
# text_eng =  He felt that he had already gone far, when, they say, he wanted to return. 
# text_por = Sentiu que já fora longe, quando, dizem, quis retornar.
# text_source = Comunidade Indígena Anamuim, 9, adap.
# text_annotator = LFdeA
1	Apekatú	apekatú	ADV	ADVC	AdvType=Loc	4	advmod	_	TokenRange=0:7
2	ã	ã	PART	PFV	Aspect=Perf	4	advmod	_	TokenRange=8:9
3	paá	paá	PART	RPRT	Evident=Nfh|PartType=Mod	4	advmod	_	TokenRange=10:13
4	usaã	saã	VERB	V	Person=3|VerbForm=Fin	0	root	_	TokenRange=14:18
5	usú	sú	VERB	V	Person=3|VerbForm=Fin	4	parataxis	_	SpaceAfter=No|TokenRange=19:22
6	,	,	PUNCT	PUNCT	_	9	punct	_	TokenRange=22:23
7	mairamé	mairamé	SCONJ	SCONJR	_	9	mark	_	TokenRange=24:31
8	paá	paá	PART	RPRT	Evident=Nfh|PartType=Mod	5	advmod	_	TokenRange=32:35
9-10	uyuíri-putari	_	_	_	_	_	_	_	TokenRange=36:49
9	uyuíri	yuíri	VERB	V	Person=3|VerbForm=Fin	5	advcl	_	_
10	putari	putari	AUX	AUXN	Compound=Yes|VerbForm=Inf	9	aux	_	_
11	ã	ã	PART	PFV	Aspect=Perf	9	advmod	_	SpaceAfter=No|TokenRange=51:52
12	.	.	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=52:53


>>> import BuildDictionary
>>> import AnnotateConllu
>>> reload(BuildDictionary)
<module 'BuildDictionary' from '/home/leonel/scripts/BuildDictionary.py'>
>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> AnnotateConllu.getparselist("aikú")
[['ikú', 'V+1+SG']]
>>> import Nheengatagger
>>> Nheengatagger.tagWord('aikú')
{'V'}
>>> s='''Kwá/demx suí tẽ ayuíri asarú arama/sconj i yuka tapiira, ayuuka arama/sconj i kãwera se membí arama/sconj. (Magalhães, 186, adap.) -  Daqui mesmo eu volto para esperar a anta apodrecer, para eu retirar seu osso para ser minha flauta.'''
>>> parse(s,'Avila2021',0,0,576)
# sent_id = Avila2021:0:0:576
# text = Kwá suí tẽ ayuíri asarú arama i yuka tapiira, ayuuka arama i kãwera se membí arama.
# text_eng = From here I come back to wait for the tapir to rot, so I can remove its bone to be my flute.
# text_por = Daqui mesmo eu volto para esperar a anta apodrecer, para eu retirar seu osso para ser minha flauta.
# text_source = Magalhães, 186, adap.
# text_annotator = LFdeA
1	Kwá	kwá	PRON	DEMX	Deixis=Prox|Number=Sing|PronType=Dem	4	obl	_	TokenRange=0:3
2	suí	suí	ADP	ADP	_	1	case	_	TokenRange=4:7
3	tẽ	tẽ	PART	FOC	Foc=Yes|PartType=Emp	1	advmod	_	TokenRange=8:10
3	tẽ	tẽ	PART	NEGI	Mood=Imp|PartType=Neg|Polarity=Neg	4	advmod	_	TokenRange=8:10
4	ayuíri	yuíri	VERB	V	Number=Sing|Person=1|VerbForm=Fin	0	root	_	TokenRange=11:17
5	asarú	sarú	VERB	V	Number=Sing|Person=1|VerbForm=Fin	4	advcl	_	TokenRange=18:23
6	arama	arama	SCONJ	SCONJ	_	5	mark	_	TokenRange=24:29
7	i	i	PRON	PRON2	Case=Gen|Number=Sing|Person=3|PronType=Prs	0	_	_	TokenRange=30:31
8	yuka	yuka	ADJ	A	_	0	_	_	TokenRange=32:36
8	yuka	yuka	VERB	V	VerbForm=Inf	5	parataxis	_	TokenRange=32:36
8	yuka	yuka	VERB	V2	_	5	parataxis	_	TokenRange=32:36
9	tapiira	tapiira	_	_	_	0	_	_	SpaceAfter=No|TokenRange=37:44
10	,	,	PUNCT	PUNCT	_	11	punct	_	TokenRange=44:45
11	ayuuka	yuuka	VERB	V	Number=Sing|Person=1|VerbForm=Fin	8	advcl	_	TokenRange=46:52
12	arama	arama	SCONJ	SCONJ	_	11	mark	_	TokenRange=53:58
13	i	i	PRON	PRON2	Case=Gen|Number=Sing|Person=3|Poss=Yes|PronType=Prs	14	nmod:poss	_	TokenRange=59:60
14	kãwera	kãwera	NOUN	N	Number=Sing	11	obj	_	TokenRange=61:67
15	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	16	nmod:poss	_	TokenRange=68:70
16	membí	membí	NOUN	N	Number=Sing	11	obj	_	TokenRange=71:76
17	arama	arama	SCONJ	SCONJ	_	11	mark	_	SpaceAfter=No|TokenRange=77:82
18	.	.	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=82:83


>>> s='''Kwá/demx suí tẽ ayuíri asarú arama/sconj i yuka/v2 tapiíra, ayuuka arama/sconj i kãwera se membí arama/sconj. (Magalhães, 186, adap.) -  Daqui mesmo eu volto para esperar a anta apodrecer, para eu retirar seu osso para ser minha flauta.'''
>>> parse(s,'Avila2021',0,0,576)
# sent_id = Avila2021:0:0:576
# text = Kwá suí tẽ ayuíri asarú arama i yuka tapiíra, ayuuka arama i kãwera se membí arama.
# text_eng = From here I come back to wait for the tapir to rot, so I can remove its bone to be my flute.
# text_por = Daqui mesmo eu volto para esperar a anta apodrecer, para eu retirar seu osso para ser minha flauta.
# text_source = Magalhães, 186, adap.
# text_annotator = LFdeA
1	Kwá	kwá	PRON	DEMX	Deixis=Prox|Number=Sing|PronType=Dem	4	obl	_	TokenRange=0:3
2	suí	suí	ADP	ADP	_	1	case	_	TokenRange=4:7
3	tẽ	tẽ	PART	FOC	Foc=Yes|PartType=Emp	1	advmod	_	TokenRange=8:10
3	tẽ	tẽ	PART	NEGI	Mood=Imp|PartType=Neg|Polarity=Neg	4	advmod	_	TokenRange=8:10
4	ayuíri	yuíri	VERB	V	Number=Sing|Person=1|VerbForm=Fin	0	root	_	TokenRange=11:17
5	asarú	sarú	VERB	V	Number=Sing|Person=1|VerbForm=Fin	4	advcl	_	TokenRange=18:23
6	arama	arama	SCONJ	SCONJ	_	5	mark	_	TokenRange=24:29
7	i	i	PRON	PRON2	Case=Gen|Number=Sing|Person=3|PronType=Prs	8	nsubj	_	TokenRange=30:31
8	yuka	yuka	VERB	V2	_	5	parataxis	_	TokenRange=32:36
9	tapiíra	tapiíra	NOUN	N	Number=Sing	8	obj	_	SpaceAfter=No|TokenRange=37:44
10	,	,	PUNCT	PUNCT	_	11	punct	_	TokenRange=44:45
11	ayuuka	yuuka	VERB	V	Number=Sing|Person=1|VerbForm=Fin	8	advcl	_	TokenRange=46:52
12	arama	arama	SCONJ	SCONJ	_	11	mark	_	TokenRange=53:58
13	i	i	PRON	PRON2	Case=Gen|Number=Sing|Person=3|Poss=Yes|PronType=Prs	14	nmod:poss	_	TokenRange=59:60
14	kãwera	kãwera	NOUN	N	Number=Sing	11	obj	_	TokenRange=61:67
15	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	16	nmod:poss	_	TokenRange=68:70
16	membí	membí	NOUN	N	Number=Sing	11	obj	_	TokenRange=71:76
17	arama	arama	SCONJ	SCONJ	_	11	mark	_	SpaceAfter=No|TokenRange=77:82
18	.	.	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=82:83


>>> s='''Kwá/demx suí tẽ/foc ayuíri asarú arama/sconj i yuka/v2 tapiíra, ayuuka arama/sconj i kãwera se membí arama/sconj. (Magalhães, 186, adap.) -  Daqui mesmo eu volto para esperar a anta apodrecer, para eu retirar seu osso para ser minha flauta. - Kwá suí tẽ ayuíri asarú arama i yuka tapiira, ayuuka arama i kãwera se membí arama.'''
>>> parse(s,'Avila2021',0,0,576)
# sent_id = Avila2021:0:0:576
# text = Kwá suí tẽ ayuíri asarú arama i yuka tapiíra, ayuuka arama i kãwera se membí arama.
# text_eng = From here I come back to wait for the tapir to rot, so I can remove its bone to be my flute.
# text_por = Daqui mesmo eu volto para esperar a anta apodrecer, para eu retirar seu osso para ser minha flauta.
# text_source = Magalhães, 186, adap.
# text_orig = Kwá suí tẽ ayuíri asarú arama i yuka tapiira, ayuuka arama i kãwera se membí arama.
# text_annotator = LFdeA
1	Kwá	kwá	PRON	DEMX	Deixis=Prox|Number=Sing|PronType=Dem	4	obl	_	TokenRange=0:3
2	suí	suí	ADP	ADP	_	1	case	_	TokenRange=4:7
3	tẽ	tẽ	PART	FOC	Foc=Yes|PartType=Emp	1	advmod	_	TokenRange=8:10
4	ayuíri	yuíri	VERB	V	Number=Sing|Person=1|VerbForm=Fin	0	root	_	TokenRange=11:17
5	asarú	sarú	VERB	V	Number=Sing|Person=1|VerbForm=Fin	4	advcl	_	TokenRange=18:23
6	arama	arama	SCONJ	SCONJ	_	5	mark	_	TokenRange=24:29
7	i	i	PRON	PRON2	Case=Gen|Number=Sing|Person=3|PronType=Prs	8	nsubj	_	TokenRange=30:31
8	yuka	yuka	VERB	V2	_	5	parataxis	_	TokenRange=32:36
9	tapiíra	tapiíra	NOUN	N	Number=Sing	8	obj	_	SpaceAfter=No|TokenRange=37:44
10	,	,	PUNCT	PUNCT	_	11	punct	_	TokenRange=44:45
11	ayuuka	yuuka	VERB	V	Number=Sing|Person=1|VerbForm=Fin	8	advcl	_	TokenRange=46:52
12	arama	arama	SCONJ	SCONJ	_	11	mark	_	TokenRange=53:58
13	i	i	PRON	PRON2	Case=Gen|Number=Sing|Person=3|Poss=Yes|PronType=Prs	14	nmod:poss	_	TokenRange=59:60
14	kãwera	kãwera	NOUN	N	Number=Sing	11	obj	_	TokenRange=61:67
15	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	16	nmod:poss	_	TokenRange=68:70
16	membí	membí	NOUN	N	Number=Sing	11	obj	_	TokenRange=71:76
17	arama	arama	SCONJ	SCONJ	_	11	mark	_	SpaceAfter=No|TokenRange=77:82
18	.	.	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=82:83


>>> s='''Kwá/demx suí tẽ/foc ayuíri asarú arama/sconj i yuka/v2 tapiíra, ayuuka arama/sconj i kãwera se membí arama/adp. (Magalhães, 186, adap.) -  Daqui mesmo eu volto para esperar a anta apodrecer, para eu retirar seu osso para ser minha flauta. - Kwá suí tẽ ayuíri asarú arama i yuka tapiira, ayuuka arama i kãwera se membí arama.'''
>>> parse(s,'Avila2021',0,0,577)
# sent_id = Avila2021:0:0:577
# text = Kwá suí tẽ ayuíri asarú arama i yuka tapiíra, ayuuka arama i kãwera se membí arama.
# text_eng = From here I come back to wait for the tapir to rot, so I can remove its bone to be my flute.
# text_por = Daqui mesmo eu volto para esperar a anta apodrecer, para eu retirar seu osso para ser minha flauta.
# text_source = Magalhães, 186, adap.
# text_orig = Kwá suí tẽ ayuíri asarú arama i yuka tapiira, ayuuka arama i kãwera se membí arama.
# text_annotator = LFdeA
1	Kwá	kwá	PRON	DEMX	Deixis=Prox|Number=Sing|PronType=Dem	4	obl	_	TokenRange=0:3
2	suí	suí	ADP	ADP	_	1	case	_	TokenRange=4:7
3	tẽ	tẽ	PART	FOC	Foc=Yes|PartType=Emp	1	advmod	_	TokenRange=8:10
4	ayuíri	yuíri	VERB	V	Number=Sing|Person=1|VerbForm=Fin	0	root	_	TokenRange=11:17
5	asarú	sarú	VERB	V	Number=Sing|Person=1|VerbForm=Fin	4	advcl	_	TokenRange=18:23
6	arama	arama	SCONJ	SCONJ	_	5	mark	_	TokenRange=24:29
7	i	i	PRON	PRON2	Case=Gen|Number=Sing|Person=3|PronType=Prs	8	nsubj	_	TokenRange=30:31
8	yuka	yuka	VERB	V2	_	5	parataxis	_	TokenRange=32:36
9	tapiíra	tapiíra	NOUN	N	Number=Sing	8	obj	_	SpaceAfter=No|TokenRange=37:44
10	,	,	PUNCT	PUNCT	_	11	punct	_	TokenRange=44:45
11	ayuuka	yuuka	VERB	V	Number=Sing|Person=1|VerbForm=Fin	8	advcl	_	TokenRange=46:52
12	arama	arama	SCONJ	SCONJ	_	11	mark	_	TokenRange=53:58
13	i	i	PRON	PRON2	Case=Gen|Number=Sing|Person=3|Poss=Yes|PronType=Prs	14	nmod:poss	_	TokenRange=59:60
14	kãwera	kãwera	NOUN	N	Number=Sing	11	obj	_	TokenRange=61:67
15	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	16	nmod:poss	_	TokenRange=68:70
16	membí	membí	NOUN	N	Number=Sing	11	obl	_	TokenRange=71:76
17	arama	arama	ADP	ADP	_	16	case	_	SpaceAfter=No|TokenRange=77:82
18	.	.	PUNCT	PUNCT	_	4	punct	_	SpaceAfter=No|TokenRange=82:83


>>> # exemplo complexo com quase 100% de acerto
>>> s='''― Makití/advrc@ se igara? | ― Aikwé. (Stradelli, 317, adap.) -  ― Onde está a minha canoa? | ― Aqui está. - “Where is my canoe?” | - "Here it is."'''
>>> AnnotateConllu.TreebankSentences(s,'Avila2021',44,1,578)
# sent_id = Avila2021:44:1:578
# text = ― Makití se igara?
# text_eng = “Where is my canoe?”
# text_por = ― Onde está a minha canoa?
# text_source = Stradelli, 317, adap.
# text_annotator = LFdeA
1	―	―	PUNCT	PUNCT	_	2	punct	_	TokenRange=-1:0
2	Makití	makití	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=1:7
3	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	4	nmod:poss	_	TokenRange=8:10
4	igara	igara	NOUN	N	Number=Sing	2	nsubj	_	SpaceAfter=No|TokenRange=11:16
5	?	?	PUNCT	PUNCT	_	2	punct	_	SpaceAfter=No|TokenRange=16:17


# sent_id = Avila2021:44:2:579
# text = ― Aikwé.
# text_eng =  - "Here it is."
# text_por = ― Aqui está.
# text_source = Stradelli, 317, adap.
# text_annotator = LFdeA
1	―	―	PUNCT	PUNCT	_	0	punct	_	TokenRange=-1:0
2	Aikwé	aikwé	PART	EXST	PartType=Exs	0	root	_	SpaceAfter=No|TokenRange=1:6
3	.	.	PUNCT	PUNCT	_	2	punct	_	SpaceAfter=No|TokenRange=6:7


>>> s='''― Makití/advrc@ se igara? | ― Aikwé. (Stradelli, 317, adap.) -  ― Onde está a minha canoa? | ― Aqui está. - “Where is my canoe?” | "Here it is."'''
>>> 
>>> AnnotateConllu.TreebankSentences(s,'Avila2021',44,1,578)
# sent_id = Avila2021:44:1:578
# text = ― Makití se igara?
# text_eng = “Where is my canoe?”
# text_por = ― Onde está a minha canoa?
# text_source = Stradelli, 317, adap.
# text_annotator = LFdeA
1	―	―	PUNCT	PUNCT	_	2	punct	_	TokenRange=-1:0
2	Makití	makití	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=1:7
3	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	4	nmod:poss	_	TokenRange=8:10
4	igara	igara	NOUN	N	Number=Sing	2	nsubj	_	SpaceAfter=No|TokenRange=11:16
5	?	?	PUNCT	PUNCT	_	2	punct	_	SpaceAfter=No|TokenRange=16:17


# sent_id = Avila2021:44:2:579
# text = ― Aikwé.
# text_eng =  "Here it is."
# text_por = ― Aqui está.
# text_source = Stradelli, 317, adap.
# text_annotator = LFdeA
1	―	―	PUNCT	PUNCT	_	0	punct	_	TokenRange=-1:0
2	Aikwé	aikwé	PART	EXST	PartType=Exs	0	root	_	SpaceAfter=No|TokenRange=1:6
3	.	.	PUNCT	PUNCT	_	2	punct	_	SpaceAfter=No|TokenRange=6:7


>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> s='''― Makití/advrc@ se igara? | ― Aikwé. (Stradelli, 317, adap.) -  ― Onde está a minha canoa? | ― Aqui está. - “Where is my canoe?” | "Here it is."'''
>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> AnnotateConllu.TreebankSentences(s,'Avila2021',44,1,578)
# sent_id = Avila2021:44:1:578
# text = ― Makití se igara?
# text_eng = “Where is my canoe?”
# text_por = ― Onde está a minha canoa?
# text_source = Stradelli, 317, adap.
# text_annotator = LFdeA
1	―	―	PUNCT	PUNCT	_	2	punct	_	TokenRange=-1:0
2	Makití	makití	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=1:7
3	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	4	nmod:poss	_	TokenRange=8:10
4	igara	igara	NOUN	N	Number=Sing	2	nsubj	_	SpaceAfter=No|TokenRange=11:16
5	?	?	PUNCT	PUNCT	_	2	punct	_	SpaceAfter=No|TokenRange=16:17


# sent_id = Avila2021:44:2:579
# text = ― Aikwé.
# text_eng =  "Here it is."
# text_por = ― Aqui está.
# text_source = Stradelli, 317, adap.
# text_annotator = LFdeA
1	―	―	PUNCT	PUNCT	_	0	punct	_	TokenRange=-1:0
2	Aikwé	aikwé	PART	EXST	PartType=Exs	0	root	_	SpaceAfter=No|TokenRange=1:6
3	.	.	PUNCT	PUNCT	_	2	punct	_	SpaceAfter=No|TokenRange=6:7


>>> reload(AnnotateConllu)
<module 'AnnotateConllu' from '/home/leonel/scripts/AnnotateConllu.py'>
>>> AnnotateConllu.TreebankSentences(s,'Avila2021',44,1,578)
# sent_id = Avila2021:44:1:578
# text = ― Makití se igara?
# text_eng = “Where is my canoe?”
# text_por = ― Onde está a minha canoa?
# text_source = Stradelli, 317, adap.
# text_annotator = LFdeA
1	―	―	PUNCT	PUNCT	_	2	punct	_	TokenRange=-1:0
2	Makití	makití	ADV	ADVRC	AdvType=Loc|PronType=Int	0	root	_	TokenRange=1:7
3	se	se	PRON	PRON2	Case=Gen|Number=Sing|Person=1|Poss=Yes|PronType=Prs	4	nmod:poss	_	TokenRange=8:10
4	igara	igara	NOUN	N	Number=Sing	2	nsubj	_	SpaceAfter=No|TokenRange=11:16
5	?	?	PUNCT	PUNCT	_	2	punct	_	SpaceAfter=No|TokenRange=16:17


# sent_id = Avila2021:44:2:579
# text = ― Aikwé.
# text_eng =  "Here it is."
# text_por = ― Aqui está.
# text_source = Stradelli, 317, adap.
# text_annotator = LFdeA
1	―	―	PUNCT	PUNCT	_	2	punct	_	TokenRange=-1:0
2	Aikwé	aikwé	PART	EXST	PartType=Exs	0	root	_	SpaceAfter=No|TokenRange=1:6
3	.	.	PUNCT	PUNCT	_	2	punct	_	SpaceAfter=No|TokenRange=6:7


>>> s='''Wará usú ã, ti ã uyuíri, usú retana karãu suí. (Hartt (1872), 75) -  O guará partiu, não voltou mais, afastou-se realmente do carão.'''
>>> parse(s,'Avila2021',0,0,580)
# sent_id = Avila2021:0:0:580
# text = Wará usú ã, ti ã uyuíri, usú retana karãu suí.
# text_eng = , 75
# text_por = 1872
# text_source = Hartt
# text_annotator = LFdeA
1	Wará	wará	_	_	_	0	_	_	TokenRange=0:4
2	usú	sú	VERB	V	Person=3|VerbForm=Fin	0	root	_	TokenRange=5:8
3	ã	ã	PART	PFV	Aspect=Perf	2	advmod	_	SpaceAfter=No|TokenRange=9:10
4	,	,	PUNCT	PUNCT	_	7	punct	_	TokenRange=10:11
5	ti	ti	PART	NEG	PartType=Neg|Polarity=Neg	7	advmod	_	TokenRange=12:14
6	ã	ã	PART	PFV	Aspect=Perf	7	advmod	_	TokenRange=15:16
7	uyuíri	yuíri	VERB	V	Person=3|VerbForm=Fin	2	parataxis	_	SpaceAfter=No|TokenRange=17:23
8	,	,	PUNCT	PUNCT	_	9	punct	_	TokenRange=23:24
9	usú	sú	VERB	V	Person=3|VerbForm=Fin	7	parataxis	_	TokenRange=25:28
10	retana	retana	ADV	ADVS	AdvType=Deg	9	advmod	_	TokenRange=29:35
11	karãu	karãu	_	_	_	0	_	_	TokenRange=36:41
12	suí	suí	ADP	ADP	_	0	case	_	SpaceAfter=No|TokenRange=42:45
13	.	.	PUNCT	PUNCT	_	2	punct	_	SpaceAfter=No|TokenRange=45:46


>>> s='''Wará usú ã, ti ã uyuíri, usú retana karãu suí. (Hartt 1872, 75) -  O guará partiu, não voltou mais, afastou-se realmente do carão.'''
>>> parse(s,'Avila2021',0,0,580)
# sent_id = Avila2021:0:0:580
# text = Wará usú ã, ti ã uyuíri, usú retana karãu suí.
# text_eng = The ibis left, it didn't come back, it really got away from the limpkin.
# text_por = O guará partiu, não voltou mais, afastou-se realmente do carão.
# text_source = Hartt 1872, 75
# text_annotator = LFdeA
1	Wará	wará	NOUN	N	Number=Sing	2	nsubj	_	TokenRange=0:4
2	usú	sú	VERB	V	Person=3|VerbForm=Fin	0	root	_	TokenRange=5:8
3	ã	ã	PART	PFV	Aspect=Perf	2	advmod	_	SpaceAfter=No|TokenRange=9:10
4	,	,	PUNCT	PUNCT	_	7	punct	_	TokenRange=10:11
5	ti	ti	PART	NEG	PartType=Neg|Polarity=Neg	7	advmod	_	TokenRange=12:14
6	ã	ã	PART	PFV	Aspect=Perf	7	advmod	_	TokenRange=15:16
7	uyuíri	yuíri	VERB	V	Person=3|VerbForm=Fin	2	parataxis	_	SpaceAfter=No|TokenRange=17:23
8	,	,	PUNCT	PUNCT	_	9	punct	_	TokenRange=23:24
9	usú	sú	VERB	V	Person=3|VerbForm=Fin	7	parataxis	_	TokenRange=25:28
10	retana	retana	ADV	ADVS	AdvType=Deg	9	advmod	_	TokenRange=29:35
11	karãu	karãu	NOUN	N	Number=Sing	9	obl	_	TokenRange=36:41
12	suí	suí	ADP	ADP	_	11	case	_	SpaceAfter=No|TokenRange=42:45
13	.	.	PUNCT	PUNCT	_	2	punct	_	SpaceAfter=No|TokenRange=45:46


>>> # 100% correta
>>> s='''Paraná uyuíri wã, uwiké uikú. (Hartt, 327, adap.) -  O rio já vazou, está enchendo.'''
>>> parse(s,'Avila2021',0,0,581)
# sent_id = Avila2021:0:0:581
# text = Paraná uyuíri wã, uwiké uikú.
# text_eng = The river has already emptied, it is filling up.
# text_por = O rio já vazou, está enchendo.
# text_source = Hartt, 327, adap.
# text_annotator = LFdeA
1	Paraná	paraná	NOUN	N	Number=Sing	2	nsubj	_	TokenRange=0:6
2	uyuíri	yuíri	VERB	V	Person=3|VerbForm=Fin	0	root	_	TokenRange=7:13
3	wã	wã	PART	PFV	Aspect=Perf	2	advmod	_	SpaceAfter=No|TokenRange=14:16
4	,	,	PUNCT	PUNCT	_	5	punct	_	TokenRange=16:17
5	uwiké	wiké	VERB	V	Person=3|VerbForm=Fin	2	parataxis	_	TokenRange=18:23
6	uikú	ikú	AUX	AUXFS	Person=3|VerbForm=Fin	5	aux	_	SpaceAfter=No|TokenRange=24:28
7	.	.	PUNCT	PUNCT	_	2	punct	_	SpaceAfter=No|TokenRange=28:29


>>> # 100% correta
>>> s='''Uyuíri ã será paraná? (Hartt, 347, adap.) -  Já vazou o rio?'''
>>> parse(s,'Avila2021',0,0,582)
# sent_id = Avila2021:0:0:582
# text = Uyuíri ã será paraná?
# text_eng = Has the river already emptied?
# text_por = Já vazou o rio?
# text_source = Hartt, 347, adap.
# text_annotator = LFdeA
1	Uyuíri	yuíri	VERB	V	Person=3|VerbForm=Fin	0	root	_	TokenRange=0:6
2	ã	ã	PART	PFV	Aspect=Perf	1	advmod	_	TokenRange=7:8
3	será	será	PART	PQ	PartType=Int	1	advmod	_	TokenRange=9:13
4	paraná	paraná	NOUN	N	Number=Sing	1	obj	_	SpaceAfter=No|TokenRange=14:20
5	?	?	PUNCT	PUNCT	_	1	punct	_	SpaceAfter=No|TokenRange=20:21


>>> # problema com sujeito pós-verbal (verbo inacusativo)
>>> s='Pitúna  okệri   oikộ    ɨ   rɨpɨpe.'
>>> s.split("\t")
['Pitúna  okệri   oikộ    ɨ   rɨpɨpe.']
>>> s
'Pitúna  okệri   oikộ    ɨ   rɨpɨpe.'
>>> s='Pitúna\tokệri\toikộ\tɨ\trɨpɨpe.'
>>> s.split("\t")
['Pitúna', 'okệri', 'oikộ', 'ɨ', 'rɨpɨpe.']
>>> p='A noite\tadormecida\testá\tda água\tno fundo.'
>>> p.split("\t")
['A noite', 'adormecida', 'está', 'da água', 'no fundo.']
>>> nheenga=s.split("\t")
>>> port=p.split("\t")
>>> i=0
>>> while(i<len(nheenga)):
	print(f"{nheenga[i]}\t{port[i]}")
	i+=1

	
Pitúna	A noite
okệri	adormecida
oikộ	está
ɨ	da água
rɨpɨpe.	no fundo.
>>> teste='''a	b	c	d
1 2 3	4	5 6 7'''
>>> teste.split("\n")
['a\tb\tc\td', '1 2 3\t4\t5 6 7']
>>> teste='''Boia-Uaçú	menbɨra,	ipahá,	oiumendári	iepé	kurumĩ-uaçú	irúmo.
Da Cobra-Grande	a filha,	contam,	casara-se	um	jovem	com.'''
>>> def alinha(texto):
	pares=texto.split('\n\n')
	for par in pares:
		yrl,por=par.split('\n')
		partes_yrl=yrl.split('\t')
		partes_por=por.split('\t')
		i=0
		while(i<len(partes_yrl)):
			print(f"{partes_yrl[i]}\t{partes_por[i]}")
			i+=1
		print('\n')

		
>>> texto='''Boia-Uaçú	menbɨra,	ipahá,	oiumendári	iepé	kurumĩ-uaçú	irúmo.
Da Cobra-Grande	a filha,	contam,	casara-se	um	jovem	com.

Quahá	kurumi-uaçú	orekộ	muçapíra	miaçúa	catú rẹtệ.
Este	jovem	tinha	três	vassalos	fiéis.'''
>>> alinha(texto)
Boia-Uaçú	Da Cobra-Grande
menbɨra,	a filha,
ipahá,	contam,
oiumendári	casara-se
iepé	um
kurumĩ-uaçú	jovem
irúmo.	com.


Quahá	Este
kurumi-uaçú	jovem
orekộ	tinha
muçapíra	três
miaçúa	vassalos
catú rẹtệ.	fiéis.


>>> texto
'Boia-Uaçú\tmenbɨra,\tipahá,\toiumendári\tiepé\tkurumĩ-uaçú\tirúmo.\nDa Cobra-Grande\ta filha,\tcontam,\tcasara-se\tum\tjovem\tcom.\n\nQuahá\tkurumi-uaçú\torekộ\tmuçapíra\tmiaçúa\tcatú rẹtệ.\nEste\tjovem\ttinha\ttrês\tvassalos\tfiéis.'
>>> print(texto)
Boia-Uaçú	menbɨra,	ipahá,	oiumendári	iepé	kurumĩ-uaçú	irúmo.
Da Cobra-Grande	a filha,	contam,	casara-se	um	jovem	com.

Quahá	kurumi-uaçú	orekộ	muçapíra	miaçúa	catú rẹtệ.
Este	jovem	tinha	três	vassalos	fiéis.
>>> 