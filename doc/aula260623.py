Python 3.8.10 (default, May 26 2023, 14:05:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'/home/leonel/lingcomp'

>>> import re
>>> f=open('data/fabula_sentenca_10.conllu','r')
>>> f.read()
'# generator = UDPipe 2, https://lindat.mff.cuni.cz/services/udpipe\n# udpipe_model = portuguese-bosque-ud-2.10-220711\n# udpipe_model_licence = CC BY-NC-SA\n# reviewer = Leonel Figueiredo de Alencar (LFdeA)\n# newdoc = A cigarra com a formiga\n# newpar\n# sent_id = 10\n# text = Com vergonha de pedir, suportou calada por muito tempo.\n1\tCom\tcom\tADP\t_\t_\t2\tcase\t_\tTokenRange=0:3\n2\tvergonha\tvergonha\tNOUN\t_\tGender=Fem|Number=Sing\t6\tobl\t_\tTokenRange=4:12\n3\tde\tde\tSCONJ\t_\t_\t4\tmark\t_\tTokenRange=13:15\n4\tpedir\tpedir\tVERB\t_\tVerbForm=Inf\t2\tacl\t_\tSpaceAfter=No|TokenRange=16:21\n5\t,\t,\tPUNCT\t_\t_\t2\tpunct\t_\tTokenRange=21:22\n6\tsuportou\tsuportar\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin\t0\troot\t_\tTokenRange=23:31\n7\tcalada\tcalada\tADJ\t_\tGender=Fem|Number=Sing\t6\tadvcl\t_\tTokenRange=32:38\n8\tpor\tpor\tADP\t_\t_\t10\tcase\t_\tTokenRange=39:42\n9\tmuito\tmuito\tDET\t_\tGender=Masc|Number=Sing|PronType=Ind\t10\tdet\t_\tTokenRange=43:48\n10\ttempo\ttempo\tNOUN\t_\tGender=Masc|Number=Sing\t6\tobl\t_\tSpaceAfter=No|TokenRange=49:54\n11\t.\t.\tPUNCT\t_\t_\t6\tpunct\t_\tSpaceAfter=No|TokenRange=54:55\n'
>>> print(f.read())

>>> f.read()
''
>>> f.close()
>>> f=open('data/fabula_sentenca_10.conllu','r')
>>> text=f.read()
>>> print(text)
# generator = UDPipe 2, https://lindat.mff.cuni.cz/services/udpipe
# udpipe_model = portuguese-bosque-ud-2.10-220711
# udpipe_model_licence = CC BY-NC-SA
# reviewer = Leonel Figueiredo de Alencar (LFdeA)
# newdoc = A cigarra com a formiga
# newpar
# sent_id = 10
# text = Com vergonha de pedir, suportou calada por muito tempo.
1	Com	com	ADP	_	_	2	case	_	TokenRange=0:3
2	vergonha	vergonha	NOUN	_	Gender=Fem|Number=Sing	6	obl	_	TokenRange=4:12
3	de	de	SCONJ	_	_	4	mark	_	TokenRange=13:15
4	pedir	pedir	VERB	_	VerbForm=Inf	2	acl	_	SpaceAfter=No|TokenRange=16:21
5	,	,	PUNCT	_	_	2	punct	_	TokenRange=21:22
6	suportou	suportar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	0	root	_	TokenRange=23:31
7	calada	calada	ADJ	_	Gender=Fem|Number=Sing	6	advcl	_	TokenRange=32:38
8	por	por	ADP	_	_	10	case	_	TokenRange=39:42
9	muito	muito	DET	_	Gender=Masc|Number=Sing|PronType=Ind	10	det	_	TokenRange=43:48
10	tempo	tempo	NOUN	_	Gender=Masc|Number=Sing	6	obl	_	SpaceAfter=No|TokenRange=49:54
11	.	.	PUNCT	_	_	6	punct	_	SpaceAfter=No|TokenRange=54:55

>>> sent=re.findall(r"#\s+text\s+=.+$",text)
>>> sent
[]
>>> sent[:10]
[]
>>> text[:10]
'# generato'
>>> sent=re.findall(r"\s+text\s+=.+$",text)
>>> sent
[]
>>> re.findall(r"text\s+=.+$",text)
[]
>>> re.findall(r"lindat",text)
['lindat']
>>> re.findall(r"711",text)
['711']
>>> re.findall(r"udpipe",text)
['udpipe', 'udpipe', 'udpipe']
>>> re.findall(r"license",text)
[]
>>> re.findall(r"licence",text)
['licence']
>>> re.findall(r"text",text)
['text']
>>> os.list('.')
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#24>", line 1, in <module>
AttributeError: module 'os' has no attribute 'list'
>>> os.dir('.')
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#25>", line 1, in <module>
AttributeError: module 'os' has no attribute 'dir'
>>> os.listdir('.')
['teste.txt', 'doc', '.git', 'data', 'src', 'README.md']
>>> os.listdir('data')
['Fabula_Sentenca_7.pdf', 'fabula_sentenca_8.conllu', 'Fabula_Sentenca_5_Bosque.pdf', 'Fabula_Sentenca_5.pdf', 'fabula_sentenca_6.conllu', 'fabula_sentenca_3.conllu', 'rules.txt', 'fabula_sentenca_11.conllu', 'fabula_sentenca_9.conllu', 'fabula_sentenca_5.conllu', 'fabula_sentenca_10.conllu', 'fabula_sentenca_4.conllu', 'fabula_sentenca_7.conllu', 'magalhaes.txt']
>>> re.findall(r"text =",text)
['text =']
>>> re.findall(r"text\s+=",text)
['text =']
>>> re.findall(r"\s+text\s+=",text)
[' text =']
>>> re.findall(r"#\s+text\s+=",text)
['# text =']
>>> sent=re.findall(r"#\s+text\s+=",text)
>>> sent
['# text =']
>>> sent=re.findall(r"#\s+text\s+=.+$",text)
>>> sent
[]
>>> re.findall(r"#\s+text\s+=.+$",text)
[]
>>> re.findall(r"#\s+text\s+=.+",text)
['# text = Com vergonha de pedir, suportou calada por muito tempo.']
>>> sent=re.findall(r"#\s+text\s+=.+",text)
>>> pat=r"[ei]"
>>> re.findall(pat,sent[0])
['e', 'e', 'e', 'e', 'i', 'i', 'e']
>>> pat=r"\w*[ei]\w*"
>>> re.findall(pat,sent[0])
['text', 'vergonha', 'de', 'pedir', 'muito', 'tempo']
>>> 