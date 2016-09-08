import json

f = open('amostradados.txt')

attrs = set()
for l in f:
	if l[0] == '{':
		obj = json.loads(l)
		attrs = attrs | set(obj.keys())

all_attrs = list(attrs)
all_attrs.sort()

print(*all_attrs, sep=',')

f.seek(0)
for l in f:
	if l[0] == '{':
		obj = json.loads(l)

		s = ''
		for a in all_attrs:
			if a in obj.keys():
				s = s + '1,'
			else:
				s = s + '0,'

		print(s)