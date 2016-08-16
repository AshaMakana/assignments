def string_(a):
	b = []
	if type(a) == str:
		b.append(len(a))
		return b
	elif type(a) == list:
	  for i in a:
	    return len(i)

print(string_('asha'))
print(string_["two","one","yui"])
