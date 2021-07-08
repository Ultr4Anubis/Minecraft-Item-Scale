import json
print('Thankyou for using my scale generator.')
res = int(input('Please enter your resolution. For example, if your using a 128x128 resolution, only input 128! '))

## Equation 1= 0.075/(texture_resolution/16)
## Equation 2= 0.125/(texture_resolution/16)

val1=0.075
val2=0.125

## Scale 1 value in offset
scale1 = val1/(res / 16)

## Scale 2 value in offset
scale2 = val2/(res/16)

## Scale 3 value in offset
scale3 = val1/(res / 16)

##Print offset component with scale values
data = {'minecraft:render_offsets': {'main_hand': {'first_person': {'scale': [scale1,scale2,scale3]},'third_person': {'scale': [scale1,scale2,scale3]}},'off_hand': {'first_person': {'scale': [scale1,scale2,scale3]},'third_person': {'scale': [scale1,scale2,scale3]}}}}
jstr = json.dumps(data, indent=4)
print(jstr)
