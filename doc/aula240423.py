Python 3.8.10 (default, Mar 13 2023, 10:26:41)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import orthconv


# aula de 24 de abril de 2023
>>> "abcdef".split('')
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#365>", line 1, in <module>
ValueError: empty separator
>>> "ab c d ef".split(' ')
['ab', 'c', 'd', 'ef']
>>> "ab c          d ef".split(' ')
['ab', 'c', '', '', '', '', '', '', '', '', '', 'd', 'ef']
>>> output="ab c          d ef".split(' ')
>>> output[2]
''
>>> if output[2]:
	print("cadeia vazia=False")


>>> if not output[2]:
	print("cadeia vazia=False")


cadeia vazia=False
>>> "abc" + "" == "abc"
True
>>> "abc" + "d" == "abc"
False
>>> "abc" + "d" == "abcd"
True
>>> "Axel Thue & Emil Post = formal language theory pioneers"
'Axel Thue & Emil Post = formal language theory pioneers'
>>> for e in output:
	if not e:
		print("vazia")


vazia
vazia
vazia
vazia
vazia
vazia
vazia
vazia
vazia
>>> i=1
>>> for e in output:
	if not e:
		i+=1


>>> i
10
>>> i=0
>>> for e in output:
	if not e:
		i+=1


>>> i
9
>>> i=0
>>> for e in "ab c          d ef":
	if not e:
		i+=1


>>> i
0
>>> len("          ")
10
>>> "abgavgthaaht".split('a')
['', 'bg', 'vgth', '', 'ht']
>>> "cabgavgthaaht".split('a')
['c', 'bg', 'vgth', '', 'ht']
>>> "abgavgthaaht".lstrip()
'abgavgthaaht'
>>> "abgavgthaaht".split()
['abgavgthaaht']
>>> help("abgavgthaaht".lstrip)
Help on built-in function lstrip:

lstrip(chars=None, /) method of builtins.str instance
    Return a copy of the string with leading whitespace removed.

    If chars is given and not None, remove characters in chars instead.

>>> help(lstrip)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#401>", line 1, in <module>
NameError: name 'lstrip' is not defined
>>> help("".lstrip)
Help on built-in function lstrip:

lstrip(chars=None, /) method of builtins.str instance
    Return a copy of the string with leading whitespace removed.

    If chars is given and not None, remove characters in chars instead.

>>> "abgavgthaaht".lstrip()
'abgavgthaaht'
>>> "  abgavgthaaht".lstrip()
'abgavgthaaht'
>>> "  abgavgthaaht".rstrip()
'  abgavgthaaht'
>>> "  abgavgthaaht  ".rstrip()
'  abgavgthaaht'
>>> "  abgavgthaaht  ".strip()
'abgavgthaaht'
>>> "yyyabgavgthaahtmmm".strip(['y','m'])
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#408>", line 1, in <module>
TypeError: strip arg must be None or str
>>> "yyyabgavgthaahtmmm".strip('ym')
'abgavgthaaht'
>>> for e in " yyyab: gav, gt, ha — ah! 'tm' mm? ".strip().split(' '):
	e.strip('''!?,:—'"''')


'yyyab'
'gav'
'gt'
'ha'
''
'ah'
'tm'
'mm'
>>> import string
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> for e in " yyyab: gav, gt, ha — ah! 'tm' mm? ".strip().split(' '):
	e.strip(string.punctuation)


'yyyab'
'gav'
'gt'
'ha'
'—'
'ah'
'tm'
'mm'
>>> for e in " yyyab: gav, gt, ha — ah! 'tm' mm? ".strip().split(' '):
	e.strip(string.punctuation + "—")


'yyyab'
'gav'
'gt'
'ha'
''
'ah'
'tm'
'mm'
>>> palavras=[]
>>> for e in " yyyab: gav, gt, ha — ah! 'tm' mm? ".strip().split(' '):
	if e.strip(string.punctuation + "—"):
		palavras.append(e)


>>> print(palavras*,sep='\n')
SyntaxError: invalid syntax
>>> print(*palavras,sep='\n')
yyyab:
gav,
gt,
ha
ah!
'tm'
mm?
>>> palavras=[]
>>> for e in " yyyab: gav, gt, ha — ah! 'tm' mm? ".strip().split(' '):
	r=e.strip(string.punctuation + "—")
	if r:
		palavras.append(r)


>>> print(*palavras,sep='\n')
yyyab
gav
gt
ha
ah
tm
mm
>>> print(*palavras,sep='+')
yyyab+gav+gt+ha+ah+tm+mm
>>> "=".join(palavras)
'yyyab=gav=gt=ha=ah=tm=mm'
>>> print(palavras,sep='\n')
['yyyab', 'gav', 'gt', 'ha', 'ah', 'tm', 'mm']
>>> list('abcdefgh')
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
>>> help(list)

>>> "list comprehension"
'list comprehension'
>>> cadeia='''yyyab: gav, gt, ha — ah! 'tm' mm? '''
>>> [e.strip(string.punctuation + "—") for e in cadeia.strip().split(' ')]
['yyyab', 'gav', 'gt', 'ha', '', 'ah', 'tm', 'mm']
>>> [e.strip(string.punctuation + "—") for e in cadeia.strip().split(' ') if e.strip()]
['yyyab', 'gav', 'gt', 'ha', '', 'ah', 'tm', 'mm']
>>> [e.strip(string.punctuation + "—") for e in cadeia.strip().split(' ') if e.strip() != '']
['yyyab', 'gav', 'gt', 'ha', '', 'ah', 'tm', 'mm']
>>> ''.strip()
''
>>> [e.strip(string.punctuation + "—") for e in cadeia.strip().split(' ') if e]
['yyyab', 'gav', 'gt', 'ha', '', 'ah', 'tm', 'mm']
>>> [e.strip(string.punctuation + "—") for e in cadeia.strip().split(' ') if strip(string.punctuation + "—")]
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#443>", line 1, in <module>
  File "<pyshell#443>", line 1, in <listcomp>
NameError: name 'strip' is not defined
>>> [e.strip(string.punctuation + "—") for e in cadeia.strip().split(' ') if e.strip(string.punctuation + "—")]
['yyyab', 'gav', 'gt', 'ha', 'ah', 'tm', 'mm']
>>> print("abcd\nxyz\nh\th\th\n")
abcd
xyz
h	h	h

>>> int('\n')
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#446>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '\n'
>>> int('a')
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#447>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'a'
>>> i=0
>>> m=10
>>> while(i<=10):
	print(i)
	i+=1


0
1
2
3
4
5
6
7
8
9
10
>>> i
11
>>> s='amor'
>>> i=-1
>>> s[-1]
'r'
>>> s[-2]
'o'
>>> s[-3]
'm'
>>> s[-4]
'a'
>>> len(s)
4
>>> i=-1
>>> while(i=> -len(s)):

SyntaxError: invalid syntax
>>> while(i >= -len(s)):
	print(s[i])
	i-=1


r
o
m
a
>>> def inverte(s):
	r=''
	i=-1
	while(i >= -len(s)):
		r=r+s[i]
		i-=1
	return r

>>> inverte('amor')
'roma'
>>> inverte('roma')
'amor'
>>> 'ntu'
'ntu'
>>> 'apurakintu = apurakí nhuntu'
'apurakintu = apurakí nhuntu'
>>> 'abcde'.split(' ')
['abcde']
>>> import os
>>> os.getcwd()
'/home/leonel/lingcomp'
>>> import split
>>> for w in split.TEST:
	split.split2(w)


[]
['abc']
['abc', ' de']
['abc', ' de', ' fg']
>>> for w in split.TEST:
	split.split(w)


['abcde']
['abc', 'de']
['abc', 'de', 'fg']
['abc', 'de', 'fg', 'gh']
>>> "abcfdaagt".replace('a','y')
'ybcfdyygt'
>>> reload(orthconv)
<module 'orthconv' from '/home/leonel/lingcomp/src/orthconv.py'>
>>> import orthconv
>>> orthconv.leftcont7('kunya','a','ã',['ny'])
'kunyã'
>>> linhas=open("data/rules.txt").readlines()
>>> linhas[0]
'kwá ; kua ; u-> w || k _ a|e\n'
>>> regras=[]
>>> for linha in linhas.strip():
	exemplo={}
	chegada, partida, regra = linha.split(";")
	exemplo['chegada']=chegada
	exemplo['partida']= partida
	exemplo['regra']=regra
	regras.append(exemplo)


Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#501>", line 1, in <module>
AttributeError: 'list' object has no attribute 'strip'
>>> exemplos=[]
>>> for linha in linhas:
	exemplo={}
	chegada, partida, regra = linha.split(";")
	exemplo['chegada']=chegada
	exemplo['partida']= partida
	exemplo['regra']=regra.strip()
	regras.append(exemplo)


>>> exemplos[0]
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#505>", line 1, in <module>
IndexError: list index out of range
>>> exemplos=[]
>>> for linha in linhas:
	exemplo={}
	chegada, partida, regra = linha.split(";")
	exemplo['chegada']=chegada
	exemplo['partida']= partida
	exemplo['regra']=regra.strip()
	exemplos.append(exemplo)


>>> exemplos[0]
{'chegada': 'kwá ', 'partida': ' kua ', 'regra': 'u-> w || k _ a|e'}
>>> for exemplo in exemplos:
	old=exemplo['partida']
	new = exemplo['chegada']
	new == orthconv.leftcont7(old,'a','ã',['ny'])


False
False
False
False
False
False
False
False
False
False
False
>>> for exemplo in exemplos:
	old=exemplo['partida']
	new = exemplo['chegada']
	print(old,new)
	new == orthconv.leftcont7(old,'a','ã',['ny'])


 kua  kwá
False
 kuaye  kwayé
False
 kuera  kwera
False
 kunya   kunhã
False
 penye  penhẽ
False
 kunya   kunhã
False
 penye  penhẽ
False
 hambeu  ambeú
False
 hambeu  ambeú
False
 repuamu  repuãmu
False
 upukásawa  upukasawa
False
>>> exemplos[0]['partida']
' kua '
>>> regras=[]
>>> exemplos=[]
>>> for linha in linhas:
	exemplo={}
	chegada, partida, regra = linha.split(";")
	exemplo['chegada']=chegada.strip()
	exemplo['partida']= partida.strip()
	exemplo['regra']=regra.strip()
	exemplos.append(exemplo)


>>> for exemplo in exemplos:
	old=exemplo['partida']
	new = exemplo['chegada']
	print(old,new, new == orthconv.leftcont7(old,'a','ã',['ny']))


kua kwá False
kuaye kwayé False
kuera kwera False
kunya kunhã False
penye penhẽ False
kunya kunhã False
penye penhẽ False
hambeu ambeú False
hambeu ambeú False
repuamu repuãmu False
upukásawa upukasawa False
>>> exemplos[0]['partida']
'kua'
>>> exemplos[6]['partida']
'penye'
>>> exemplos[6]['chegada']
'penhẽ'
>>> exemplos[5]['chegada']
'kunhã'
>>> exemplos[5]['partida']
'kunya'
>>> linhas=open("data/rules.txt").readlines()
>>> exemplos=[]
>>> for linha in linhas:
	exemplo={}
	chegada, partida, regra = linha.split(";")
	exemplo['chegada']=chegada.strip()
	exemplo['partida']= partida.strip()
	exemplo['regra']=regra.strip()
	exemplos.append(exemplo)


>>> for exemplo in exemplos:
	old=exemplo['partida']
	new = exemplo['chegada']
	print(old,new, new == orthconv.leftcont7(old,'a','ã',['ny']))


kua kwá False
kuaye kwayé False
kuera kwera False
kunya kunyã True
penye penyẽ False
kunyã kunhã False
penye penhẽ False
hambeu ambeú False
hambeu ambeú False
repuamu repuãmu False
upukásawa upukasawa False
>>> orthconv.leftcont7('hambeu','h','0',['#'])
'ambeu'
>>> orthconv.leftcont7('hambeuh','h','0',['#'])
'ambeuh'
>>> orthconv.leftcont7('ahambeuh','h','0',['#'])
'ahambeuh'
>>> for c in "bhnthgtajjkyaafg":
	if c == a:
		print(a)


>>> for c in "bhnthgtajjkyaafg":
	if c == 'a':
		print(a)


False
False
False
>>> for c in "bhnthgtajjkyaafg":
	if c == 'a':
		print(c)


a
a
a
>>> for c in "bhnthgtajjkyaafg":
	if c == 'a':
		print(c)
		break


a
>>>
