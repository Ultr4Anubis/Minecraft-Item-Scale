import json
print('Thankyou for using my scale generator.')
res = int(input('Please enter your resolution. For example, if your using a 128x128 resolution, only input 128!'))
##
a=0.075
b=0.125
##
d = res / 16
e = a / d
##
f = res /16
g = b /f
##
h = res / 16
i = a /h
##
data = {'minecraft:render_offsets': {'main_hand': {'first_person': {'scale': [e,g,i,]},'third_person': {'scale': [e,g,i]}},'off_hand': {'first_person': {'scale': [e,g,i]},'third_person': {'scale': [e,g,i]}}}}
jstr = json.dumps(data, indent=4)
print(jstr)
