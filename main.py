items = ['A','B','S','B','A','D','S','S','A','Z','D','S','A','A','B','K']

out = dict()
for i in items:
    if i not in out:
        out[i] = 1
    else:
        out[i] = out[i] + 1
print(out)
