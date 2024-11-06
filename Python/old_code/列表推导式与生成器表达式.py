x='ABC'
codes=[ord(x) for x in x]
print(x)    #ABC,x没变
print(codes)    #[65,66,67]
codes_=[last:=ord(c) for c in x]    #海象表达式
print(codes_)   #[65,66,67]
print(last)    #67
colors=['black','white']
sizes=['S','M','L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)