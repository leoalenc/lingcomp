Python 3.8.10 (default, May 26 2023, 14:05:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 100 - 54/10181*100
99.46960023573322
>>> import re
>>> "Quem casa, quer casa."
'Quem casa, quer casa.'
>>> re.findall(r"casa","Quem casa, quer casa.")
['casa', 'casa']
>>> special_characters='''$()*+.?
[\^{|'''
>>> s="quem casa, quer casa."
>>> re.findall(r"^qu",s)
['qu']
>>> re.findall(r"^qu..",s)
['quem']
>>> re.findall(r"asa.$",s)
['asa.']
>>> re.findall(r"asa.",s)
['asa,', 'asa.']
>>> s='''Quem casa, quer casa.
Segunda linha.
Terceira linha.
Quarta linha.'''
>>> re.findall(r"linha\.",s)
['linha.', 'linha.', 'linha.']
>>> s="""1
2
3
"""
>>> 'a'
'a'
>>> "a"
'a'
>>> re.findall(r"linha\.$",s)
[]
>>> "escape"
'escape'
>>> s='''Quem casa, quer casa.
Segunda linha.
Terceira linha.
Quarta linha.
Várias linhas.'''
>>> "Kleene star"
'Kleene star'
>>> re.findall(r"linhas?\.",s)
['linha.', 'linha.', 'linha.', 'linhas.']
>>> "PEMDAS"
'PEMDAS'
>>> re.findall(r"a (linha)?\.",s)
['linha', 'linha', 'linha']
>>> s='''Quem casa, quer casa.
Segunda linha.
Terceira linha.
Quarta linha.
Várias linhas.
Outra coisa.'''
>>> re.findall(r"a (linha)?\.",s)
['linha', 'linha', 'linha']
>>> re.findall(r"a (linha)?",s)
['linha', 'linha', 'linha', '']
>>> s='abbbc ac aggc'
>>> re.findall(r"a[bg]c?",s)
['ab', 'ag']
>>> re.findall(r"a[bg]?c",s)
['ac']
>>> s='abbc ac aggc'
>>> re.findall(r"a[bg]?c",s)
['ac']
>>> re.findall(r"a[bg]?c",s)
['ac']
>>> s='abc ac agc'
>>> re.findall(r"a[bg]?c",s)
['abc', 'ac', 'agc']
>>> s='abbc ac aggc'
>>> re.findall(r"abb?c",s)
['abbc']
>>> re.findall(r"a(bb)?c",s)
['bb', '']
>>> s='''Quem casa, quer casa.
Segunda linha.
Terceira linha.
Quarta linha.
Várias linhas.
Outra coisa.'''
>>> re.findall(r"a (linha)?\.",s)
['linha', 'linha', 'linha']
>>> re.findall(r"a linha?\.",s)
['a linha.', 'a linha.', 'a linha.']
>>> w="abc"
>>> 3*abc
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#48>", line 1, in <module>
NameError: name 'abc' is not defined
>>> 3*w
'abcabcabc'
>>> 3*abc
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#50>", line 1, in <module>
NameError: name 'abc' is not defined
>>> 3*"abc"
'abcabcabc'
>>> 1*"abc"
'abc'
>>> 0*"abc"
''
>>> a*3-2
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#54>", line 1, in <module>
NameError: name 'a' is not defined
>>> 5*3-2
13
>>> '''leonel@yawarate:~$ echo "a linha." | grep -E "a (linha)?\."
a linha.
leonel@yawarate:~$ echo "a ." | grep -E "a (linha)?\."
a .
leonel@yawarate:~$ echo "a ." | grep -E "a linha?\."
leonel@yawarate:~$ 
'''
'leonel@yawarate:~$ echo "a linha." | grep -E "a (linha)?\\."\na linha.\nleonel@yawarate:~$ echo "a ." | grep -E "a (linha)?\\."\na .\nleonel@yawarate:~$ echo "a ." | grep -E "a linha?\\."\nleonel@yawarate:~$ \n'
>>> re.findall(r"a ?(linha)?\.",s)
['', 'linha', 'linha', 'linha', '']
>>> re.findall(r"a ?linha?\.",s)
['a linha.', 'a linha.', 'a linha.']
>>> s='''Quem casa, quer casa.
Segunda linha.
Terceiraa linha.
Quarta linhaa.'''
>>> re.findall(r".+a{1,2}",s)
['Quem casa, quer casa', 'Segunda linha', 'Terceiraa linha', 'Quarta linhaa']
>>> re.findall(r"\w+a{1,2}",s)
['casa', 'casa', 'Segunda', 'linha', 'Terceiraa', 'linha', 'Quarta', 'linhaa']
>>> re.findall(r"\w+a{2,3}",s)
['Terceiraa', 'linhaa']
>>> s='''Quem casa, quer casa.
Segunda linha.
Tterceiraa linha.
Quarta linhaa.'''
>>> re.findall(r"\w+a|t{2,3}",s)
['casa', 'casa', 'Segunda', 'linha', 'Tterceiraa', 'linha', 'Quarta', 'linhaa']
>>> s='''Quem casa, quer casa.
Segunda llinha.
Tterceiraa linha.
Quarta linhaa.'''
>>> re.findall(r"\w+l|t{2,3}",s)
['ll']
>>> s='''Quem casa, quer casa.
Segunda linha.
Tterceiraa linha.
Quarta linhaa?'''
>>> re.findall(r"\w+?",s)
['Q', 'u', 'e', 'm', 'c', 'a', 's', 'a', 'q', 'u', 'e', 'r', 'c', 'a', 's', 'a', 'S', 'e', 'g', 'u', 'n', 'd', 'a', 'l', 'i', 'n', 'h', 'a', 'T', 't', 'e', 'r', 'c', 'e', 'i', 'r', 'a', 'a', 'l', 'i', 'n', 'h', 'a', 'Q', 'u', 'a', 'r', 't', 'a', 'l', 'i', 'n', 'h', 'a', 'a']
>>> re.findall(r"\w+l|t{2,3}",'Segunda llinha.')
['ll']
>>> re.findall(r"\w+l|t{2,3}",'Segunda,llinha.')
['ll']
>>> re.findall(r"\w+l|t{2,3}",',,,')
[]
>>> re.findall(r"\w+",',,,')
[]
>>> s='''Quem casa, quer casa.
Segunda linha.
llerceiraa linha.
Quarta linhaa?'''
>>> s='''Quem casa, quer casa.
Segunda linha.
tterceiraa linha.
Quarta linhaa?'''
>>> re.findall(r"\w+l|t{2,3}",s)
['tt']
>>> s='''Quem casa, quer casa.
Segunda llinha.
Tterceiraa linha.
Quarta linhaa.'''
>>> re.findall(r"\w+l|t{2,3}",s)
['ll']
>>> re.findall(r"\w+l|t{2,3}","llinha tttereceira")
['ll', 'ttt']
>>> s='''Quem casa, quer casa.
Segunda linha.
Tterceiraa linha.
Quarta linhaa?'''
>>> re.findall(r"\w+[lt]{2,3}",s)
[]
>>> re.findall(r"\w+(lt){2,3}",s)
[]
>>> re.findall(r"\w+(l|t){2,3}",s)
[]
>>> re.findall(r"\w+(la|ta){2,3}","ab lala tata la ta")
[]
>>> re.findall(r"\w+(la|ta){2,3}","ab lala tata la ta")
[]
>>> re.findall(r"\w+(la|ta){2,3}","ab alala tata la ta")
['la']
>>> s='''Quem casa, quer casa.
Segunda linha.
Tterceiraa linha.
Quarta linhaa?'''
>>> re.findall(r"\w+[la|ta]{2,3}","ab alala tata la ta")
['alala', 'tata']
>>> 5*3-2
13
>>> (5*3)-2
13
>>> 5*(3-2)
5
>>> s='''Quem casa, quer casa.
Segunda linha.
Tterceiraa linha.
Quarta linhaa?'''
>>> re.findall(r"\w+?",s)
['Q', 'u', 'e', 'm', 'c', 'a', 's', 'a', 'q', 'u', 'e', 'r', 'c', 'a', 's', 'a', 'S', 'e', 'g', 'u', 'n', 'd', 'a', 'l', 'i', 'n', 'h', 'a', 'T', 't', 'e', 'r', 'c', 'e', 'i', 'r', 'a', 'a', 'l', 'i', 'n', 'h', 'a', 'Q', 'u', 'a', 'r', 't', 'a', 'l', 'i', 'n', 'h', 'a', 'a']
>>> re.findall(r"\w+?",s)re.findall(r"\w+?","isso?")
SyntaxError: invalid syntax
>>> re.findall(r"\w+?","isso?")
['i', 's', 's', 'o']
>>> re.findall(r"\w+\?","isso?")
['isso?']
>>> re.findall(r"[a-f]","isso?")
[]
>>> 
>>> re.findall(r"[a-j]","isso?")
['i']
>>> re.findall(r"[a-j]","ela tem isso?")
['e', 'a', 'e', 'i']
>>> re.findall(r"[A-Z]","ELA tem isso?")
['E', 'L', 'A']
>>> re.findall(r"[A-K]","ELA tem isso?")
['E', 'A']
>>> re.findall(r"ela","ELA tem isso, ela?")
['ela']
>>> re.findall(r"(?i)ela","ELA tem isso, ela?")
['ELA', 'ela']
>>> "i=case insensitivity"
'i=case insensitivity'
>>> re.findall(r"(?i)ELA","ELA tem isso, ela?")
['ELA', 'ela']
>>> s='''Quem casa, quer casa.
Segunda linha.
Tterceiraa linha.
Quarta linhaa?'''
>>> if re.search(r"casa",s):
	print("Ocorrência de 'casa'.")

	
Ocorrência de 'casa'.
>>> s='''
Segunda linha.
Tterceiraa linha.
Quarta linhaa?'''
>>> if re.search(r"casa",s):
	print("Ocorrência de 'casa'.")

	
>>> ret=re.search(r"casa",s)
>>> ret
>>> type(ret)
<class 'NoneType'>
>>> s='''Quem casa, quer casa.
Segunda linha.
Tterceiraa linha.
Quarta linhaa?'''
>>> ret=re.search(r"casa",s)
>>> ret
<re.Match object; span=(5, 9), match='casa'>
>>> s='''Quem casa, quer casa.
Segunda linha.
Tterceiraa linha desta casa.
Quarta linhaa?'''
>>> ret=re.search(r"casa",s)
>>> ret
<re.Match object; span=(5, 9), match='casa'>
>>> ret=re.search(r"linha",s)
>>> ret
<re.Match object; span=(30, 35), match='linha'>
>>> s[30:35]
'linha'
>>> regex=re.compile(r"casa")
>>> regex
re.compile('casa')
>>> regex.search(s)
<re.Match object; span=(5, 9), match='casa'>
>>> ret=re.match(r"casa",s)
>>> ret
>>> ret=re.match(r"Quem",s)
>>> ret
<re.Match object; span=(0, 4), match='Quem'>
>>> ret=re.match(r"(?i)Quem?",s)
>>> ret
<re.Match object; span=(0, 4), match='Quem'>
>>> s='''Que casa, quem quer casa.
Segunda linha.
Tterceiraa linha desta casa.
Quarta linhaa?'''
>>> ret=re.match(r"(?i)Quem?",s)
>>> ret
<re.Match object; span=(0, 3), match='Que'>
>>> ret.groups()
()
>>> ret=re.match(r"(?i)(Que)m?",s)
>>> ret.groups()
('Que',)
>>> ret=re.match(r"(?i).+(\w+@\w+\.\com)","O e-mail dele é antonio@htt.com, tudo em minúsculas.")
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#140>", line 1, in <module>
  File "/usr/lib/python3.8/re.py", line 191, in match
    return _compile(pattern, flags).match(string)
  File "/usr/lib/python3.8/re.py", line 304, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/usr/lib/python3.8/sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "/usr/lib/python3.8/sre_parse.py", line 948, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.8/sre_parse.py", line 443, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
  File "/usr/lib/python3.8/sre_parse.py", line 834, in _parse
    p = _parse_sub(source, state, sub_verbose, nested + 1)
  File "/usr/lib/python3.8/sre_parse.py", line 443, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
  File "/usr/lib/python3.8/sre_parse.py", line 525, in _parse
    code = _escape(source, this, state)
  File "/usr/lib/python3.8/sre_parse.py", line 426, in _escape
    raise source.error("bad escape %s" % escape, len(escape))
re.error: bad escape \c at position 16
>>> ret=re.match(r"(?i).+(\w+@\w+\.com)","O e-mail dele é antonio@htt.com, tudo em minúsculas.")
>>> ret
<re.Match object; span=(0, 31), match='O e-mail dele é antonio@htt.com'>
>>> ret.groups()
('o@htt.com',)
>>> ret=re.match(r"(?i)\W+(\w+@\w+\.com)","O e-mail dele é antonio@htt.com, tudo em minúsculas.")
>>> ret
>>> ret=re.match(r"(?i).*\W+(\w+@\w+\.com)","O e-mail dele é antonio@htt.com, tudo em minúsculas.")
>>> ret
<re.Match object; span=(0, 31), match='O e-mail dele é antonio@htt.com'>
>>> ret.groups()
('antonio@htt.com',)
>>> ret=re.match(r"(?i).*\W+(\w+@\w+\.com)","O e-mail dele é antonio@htt.com, tudo em minúsculas. Outro: a@b.com também.")
>>> ret
<re.Match object; span=(0, 67), match='O e-mail dele é antonio@htt.com, tudo em minúscul>
>>> ret.groups()
('a@b.com',)
>>> s="O e-mail dele é antonio@htt.com, tudo em minúsculas. Outro: a@b.com também."
>>> s[0:67]
'O e-mail dele é antonio@htt.com, tudo em minúsculas. Outro: a@b.com'
>>> s='Do you like 13 or 42?'
>>> matchobj = re.search(r"\b13\b", s)
>>> if matchobj:
	print(matchobj.group())

	
13
>>> s='Do you like 1333, 13, 42 or 130?'
>>> if matchobj:
	print(matchobj.group())

	
13
>>> if matchobj:
	print(matchobj.group())

	
13
>>> s='Do you like 1333, 138, 42 or 130?'
>>> if matchobj:
	print(matchobj.group())

	
13
>>> matchobj = re.search(r"\b13\b", s)
>>> if matchobj:
	print(matchobj.group())

	
>>> s='Do you like 1333, 13, 42 or 130?'
>>> matchobj = re.search(r"\b13\b", s)
>>> if matchobj:
	print(matchobj.group())

	
13
>>> "b=boundary"
'b=boundary'
>>> s='Do you like 1333, 136, 42 or 13.'
>>> matchobj = re.search(r"\b13\b", s)
>>> if matchobj:
	print(matchobj.group())

	
13
>>> s='Do you like 1333, 136, 42 or 13'
>>> matchobj = re.search(r"\b13\b", s)
>>> if matchobj:
	print(matchobj.group())

	
13
>>> 