Python 3.8.10 (default, Mar 13 2023, 10:26:41) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import orthconv
>>> orthconv.leftcont5('kunya','u','w','k')
'kwnya'
>>> from importlib import reload
>>> reload(orthconv)
<module 'orthconv' from '/home/leonel/lingcomp/src/orthconv.py'>
>>> orthconv.leftcont6('kunya','u','w',['k'])
'kwnya'
>>> orthconv.leftcont6('gunya','u','w',['k','g'])
'gwnya'
>>> orthconv.leftcont6('gunya','n','h',['ku','gu'])
'guhya'
>>> reload(orthconv)
<module 'orthconv' from '/home/leonel/lingcomp/src/orthconv.py'>
>>> orthconv.rightcont2('kunya','u','w',['a','e'])
'kwnya'
>>> reload(orthconv)
<module 'orthconv' from '/home/leonel/lingcomp/src/orthconv.py'>
>>> orthconv.rightcont2('kunya','u','w',['a','e'])
>>> reload(orthconv)
<module 'orthconv' from '/home/leonel/lingcomp/src/orthconv.py'>
>>> orthconv.rightcont2('kunya','u','w',['a','e'])
'kunya'
>>> orthconv.rightcont2('kuera','u','w',['a','e'])
'kwera'
>>> orthconv.rightcont2('kuayé','u','w',['a','e'])
'kwayé'
>>> reload(orthconv)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#15>", line 1, in <module>
  File "/usr/lib/python3.8/importlib/__init__.py", line 169, in reload
    _bootstrap._exec(spec, module)
  File "<frozen importlib._bootstrap>", line 604, in _exec
  File "<frozen importlib._bootstrap_external>", line 844, in exec_module
  File "<frozen importlib._bootstrap_external>", line 981, in get_code
  File "<frozen importlib._bootstrap_external>", line 911, in source_to_code
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "<fstring>", line 1
    (word[j:return new])
            ^
SyntaxError: invalid syntax
>>> reload(orthconv)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#16>", line 1, in <module>
  File "/usr/lib/python3.8/importlib/__init__.py", line 169, in reload
    _bootstrap._exec(spec, module)
  File "<frozen importlib._bootstrap>", line 604, in _exec
  File "<frozen importlib._bootstrap_external>", line 844, in exec_module
  File "<frozen importlib._bootstrap_external>", line 981, in get_code
  File "<frozen importlib._bootstrap_external>", line 911, in source_to_code
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "<fstring>", line 1
    (word[j:return new])
            ^
SyntaxError: invalid syntax
>>> reload(orthconv)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#17>", line 1, in <module>
  File "/usr/lib/python3.8/importlib/__init__.py", line 169, in reload
    _bootstrap._exec(spec, module)
  File "<frozen importlib._bootstrap>", line 604, in _exec
  File "<frozen importlib._bootstrap_external>", line 844, in exec_module
  File "<frozen importlib._bootstrap_external>", line 981, in get_code
  File "<frozen importlib._bootstrap_external>", line 911, in source_to_code
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "<fstring>", line 1
    (word[j:return new])
            ^
SyntaxError: invalid syntax
>>> reload(orthconv)
<module 'orthconv' from '/home/leonel/lingcomp/src/orthconv.py'>
>>> orthconv.rightcont2('kuayé','u','w',['a','e'])
'kwayé'
>>> orthconv.leftcont7('kunya', 'a', 'ã', ['ny'])
'kunyã'
>>> orthconv.leftcont7('kunya', 'a', 'ã', ['ny','m'])
'kunyã'
>>> orthconv.leftcont7('kuma', 'a', 'ã', ['ny','m'])
'kumã'
>>> orthconv.leftcont7('kunya', 'a', 'ã', ['kuny'])
'kunyã'
>>> orthconv.leftcont7('kunya', 'a', 'ã', ['akuny'])
'kunya'
>>> orthconv.leftcont7('kunya', 'a', 'ã', ['bakuny'])
'kunya'
>>> 'abcd'[-1]
'd'
>>> 'abcd'[-2]
'c'
>>> 'abcd'[-3]
'b'
>>> 'abcd'[-4]
'a'
>>> 'abcd'[-5]
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#30>", line 1, in <module>
IndexError: string index out of range
>>> 'abcd'[-5:]
'abcd'
>>> 'abcdefg'[2]
'c'
>>> orthconv.hasLeftChars(['pind'],'pindamonhangaba','4')
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#33>", line 1, in <module>
  File "/home/leonel/lingcomp/src/orthconv.py", line 185, in hasLeftChars
    if c == word[end-d:end]:
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> orthconv.hasLeftChars(['pind'],'pindamonhangaba',4)
True
>>> orthconv.hasLeftChars(['pind'],'pindamonhangaba',5)
False
>>> orthconv.hasLeftChars(['pinda'],'pindamonhangaba',5)
True
>>> orthconv.hasLeftChars(['nda'],'pindamonhangaba',5)
True
>>> reload(orthconv)
<module 'orthconv' from '/home/leonel/lingcomp/src/orthconv.py'>
>>> orthconv.rightleftcont('repuãmu','a','ã',['u'],['m'])
'repuãmu'
>>> orthconv.rightleftcont('repuãnu','a','ã',['u'],['m'])
'repuãnu'
>>> orthconv.rightleftcont('repuamu','a','ã',['u'],['m'])
'repuãmu'
>>> orthconv.rightleftcont('repuanu','a','ã',['u'],['m'])
'repuanu'
>>> orthconv.rightleftcont('repiamu','a','ã',['u'],['m'])
'repiamu'
>>> "se rurí"
'se rurí'
>>> "apurakí 'eu trabalho'"
"apurakí 'eu trabalho'"
>>> "se rurí 'sou feliz'"
"se rurí 'sou feliz'"
>>> "5 000 000"
'5 000 000'
>>> s='Maria igara'
>>> lexicon={'igara': 'canoa', 'kisé': 'faca'}
>>> tokens=s.split(' ')
>>> tokens
['Maria', 'igara']
>>> tokens.reverse()
>>> tokens
['igara', 'Maria']
>>> for token in tokens:
	print(lexicon.get(token),end=' ')

	
canoa None 
>>> for token in tokens:
	transl=lexicon.get(token)
	if transl:
		transl=token
	print(transl,end=' ')

	
igara None 
>>> for token in tokens:
	transl=lexicon.get(token)
	if not transl:
		transl=token
	print(transl,end=' ')

	
canoa Maria 
>>> tokens.pop(-1)
'Maria'
>>> tokens
['igara']
>>> tokens.append('Kelcyanni')
>>> for token in tokens:
	transl=lexicon.get(token)
	if not transl:
		transl=token
	print(transl,end=' ')

	
canoa Kelcyanni 
>>> lexicon['igara']
'canoa'
>>> lexicon['kisé']
'faca'
>>> lexicon['Pedro']
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#68>", line 1, in <module>
KeyError: 'Pedro'
>>> for key,value in lexicon.items():
	print(f"chave:{key}\tvalor:{value}")

	
chave:igara	valor:canoa
chave:kisé	valor:faca
>>> for key,value in lexicon.items():
	print(f"chave:{key}\nvalor:{value}")

	
chave:igara
valor:canoa
chave:kisé
valor:faca
>>> for key,value in lexicon.items():
	print(f"chave:{key}\nvalor:{value}")
	print()

	
chave:igara
valor:canoa

chave:kisé
valor:faca

>>> lexicon.get('Pedro')
>>> transl=lexicon.get('Pedro')
>>> transl
>>> type(transl)
<class 'NoneType'>
>>> if True:
	print("Verdade!")

	
Verdade!
>>> v='True'
>>> type(v)
<class 'str'>
>>> v=True
>>> type(v)
<class 'bool'>
>>> f=False
>>> if f:
	print('Falso!')

	
>>> if f or v:
	print('Falso!')

	
Falso!
>>> a=False
>>> b=False
>>> if a or b:
	print('Falso!')

	
>>> for token in tokens:
	transl=lexicon.get(token)
	if not transl:
		transl=token
	print(transl,end=' ')

	
canoa Kelcyanni 
>>> if "abc":
	print('OK!')

	
OK!
>>> 'Haskey'
'Haskey'
>>> if "":
	print('OK!')

	
>>> if 3:
	print('Ok!')

	
Ok!
>>> if -3:
	print('Ok!')

	
Ok!
>>> if 0.9:
	print('Ok!')

	
Ok!
>>> if 0:
	print('Ok!')

	
>>> if None:
	print('Ok!')

	
>>> if not None:
	print('Ok!')

	
Ok!
>>> if not 0:
	print('Ok!')

	
Ok!
>>> if not "":
	print('OK!')

	
OK!
>>> def translate(s):
	for token in tokens:
		transl=lexicon.get(token)
		if not transl:
		transl=tokenprint(transl,end=' ')
		
SyntaxError: expected an indented block
>>> def translate(s):
	for token in s.split(' ').reverse():
		transl=lexicon.get(token)
		if not transl:
			transl=token
		print(transl,end=' ')

		
>>> translate('Maria igara')
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#128>", line 1, in <module>
  File "<pyshell#127>", line 2, in translate
TypeError: 'NoneType' object is not iterable
>>> def translate(s):
	tokens=s.split(' ')
	tokens.reverse()
	for token in tokens:
		transl=lexicon.get(token)
		if not transl:
			transl=token
		print(transl,end=' ')

		
>>> translate('Maria igara')
canoa Maria 
>>> lista="a b c d".split(' ')
>>> lista
['a', 'b', 'c', 'd']
>>> retorno=lista.reverse()
>>> "abcde".replace('ab','xy')
'xycde'
>>> retorno
>>> type(retorno)
<class 'NoneType'>
>>> def func(s):
	print(s)

	
>>> func('Olá, mundo!')
Olá, mundo!
>>> retorno=func('Olá, mundo!')
Olá, mundo!
>>> type(retorno)
<class 'NoneType'>
>>> def func(s):
	print(s.upper())

	
>>> retorno=func('Olá, mundo!')
OLÁ, MUNDO!
>>> retorno=func('Olá, mundo!')
OLÁ, MUNDO!
>>> def func(s):
	print(s.title())

	
>>> retorno=func('Olá, mundo!')
Olá, Mundo!
>>> type(retorno)
<class 'NoneType'>
>>> translate('Pedro kisé')
faca Pedro 
>>> def translate2(s):
	tokens=s.split(' ')
	tokens.reverse()
	transl=[]
	for token in tokens:
		target=lexicon.get(token)
		if not target:
			target=token
		transl.append(target)
	print(f"a{transl[0]}de{transl[1]}")

	
>>> translate2('Maria igara')
acanoadeMaria
>>> def translate2(s):
	tokens=s.split(' ')
	tokens.reverse()
	transl=[]
	for token in tokens:
		target=lexicon.get(token)
		if not target:
			target=token
		transl.append(target)
	print(f"a {transl[0]} de {transl[1]}")

	
>>> translate2('Maria igara')
a canoa de Maria
>>> translate2('Pedro kisé')
a faca de Pedro
>>> lexicon
{'igara': 'canoa', 'kisé': 'faca'}
>>> lexicon={'igara': 'canoa', 'kisé': 'faca'}
>>> lexicon={'igara': 'canoa', 'kisé': 'faca'}
>>> lexicon=[{'lemma': 'igara', 'sense': 'canoa', 'gender': 'f'}, {'lemma': 'kisé', 'sense': 'faca', 'gender': 'f'}, {'lemma': 'pirá', 'sense': 'peixe', 'gender': 'm'}, {'lemma': 'pindá', 'sense': 'anzol', 'gender': 'm'}]
>>> lexicon=[{'lemma': 'igara', 'sense': 'canoa', 'gender': 'f'}, {'lemma': 'kisé', 'sense': 'faca', 'gender': 'f'}, {'lemma': 'pirá', 'sense': 'peixe', 'gender': 'm'}, {'lemma': 'pindá', 'sense': 'anzol', 'gender': 'm'}, {'lemma': 'kurumĩ', 'sense': 'menino', 'gender': 'm'}]
>>> for entry in lexicon:
	lemma=entry.get('igara')
	if lemma:
		print(entry)

		
>>> for entry in lexicon:
	lemma=entry.get('lemma')
	if lemma == 'igara':
		print(entry)

		
{'lemma': 'igara', 'sense': 'canoa', 'gender': 'f'}
>>> def getEntry(lemma):
	for entry in lexicon:
		lemma=entry.get('lemma')
		if lemma == 'igara':
			print(entry)

			
>>> def getEntry(lemma):
	for entry in lexicon:
		lemma=entry.get('lemma')
		if lemma == 'igara':
			return entry

		
>>> getEntry('kisé')
{'lemma': 'igara', 'sense': 'canoa', 'gender': 'f'}
>>> def getEntry(lemma):
	for entry in lexicon:
		lemma=entry.get('lemma')
		if lemma == lemma:
			return entry

		
>>> getEntry('kisé')
{'lemma': 'igara', 'sense': 'canoa', 'gender': 'f'}
>>> lemma
'kurumĩ'
>>> def getEntry(word):
	for entry in lexicon:
		lemma=entry.get('lemma')
		if lemma == word:
			return entry

		
>>> getEntry('kisé')
{'lemma': 'kisé', 'sense': 'faca', 'gender': 'f'}
>>> entry=getEntry('kisé')

>>> type(entry)
<class 'dict'>
>>> def translate3(s):
	tokens=s.split(' ')
	tokens.reverse()
	transl=[]
	articles={'m': 'o', 'f': 'a'}
	target=''
	for token in tokens:
		entry=getEntry(token)
		if not entry:
			target=token
		else:
			gender=entry['gender']
			sense=entry['sense']
			target=f"{article[gender]} {sense}"
		transl.append(target)
	print(f"{transl[0]} de {transl[1]}")

	
>>> translate3('Pedro kisé')
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#189>", line 1, in <module>
  File "<pyshell#188>", line 14, in translate3
NameError: name 'article' is not defined
>>> def translate3(s):
	tokens=s.split(' ')
	tokens.reverse()
	transl=[]
	articles={'m': 'o', 'f': 'a'}
	target=''
	for token in tokens:
		entry=getEntry(token)
		if not entry:
			target=token
		else:
			gender=entry['gender']
			sense=entry['sense']
			target=f"{articles[gender]} {sense}"
		transl.append(target)
	print(f"{transl[0]} de {transl[1]}")

	
>>> translate3('Pedro kisé')
a faca de Pedro
>>> def translate3(s):
	tokens=s.split(' ')
	tokens.reverse()
	transl=[]
	articles={'m': 'o', 'f': 'a'}
	target=''
	for token in tokens:
		entry=getEntry(token)
		if not entry:
			target=token
		else:
			gender=entry['gender']
			target=f"{articles[gender]} {entry['sense']}"
		transl.append(target)
	print(f"{transl[0]} de {transl[1]}")

	
>>> translate3('Pedro kisé')
a faca de Pedro
>>> translate3('Pedro pindá')
o anzol de Pedro
>>> translate3('Pedro pirá')
o peixe de Pedro
>>> translate3('Pedro igara')
a canoa de Pedro
>>> 