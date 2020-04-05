#!/usr/bin/python3.4
# -*- coding=utf-8 -*-

REPLY="""Content-Type: text/html

<HTML>
<TITLE>Languages2</TITLE>
<BODY>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<H1>Hello World Selector</H1>
<HR>
<FORM method=POST action="lang2reply.py">
    <P><B>请选择一种语言:</B>
	<P><select name=%s>
		<option>ALL
		%s
	</select>
	<P><input type=Submit>
</FORM>
</BODY></HTML>
"""
from lang2com import hellos, inputkey

options = []
for lang in hellos:
	options.append("<option>" + lang)

options = "\n\t\t".join(options)
print(REPLY % (inputkey, options))


tet  enumerate eee
tet  enumerate eee
tet  enumerate eee
tet  enumerate eee
tet  enumerate eee
tet  enumerate eee
tet  enumerate eee
tet  enumerate eee
tet  enumerate eee
