import json
print('Thankyou for using my scale generator.')
res = int(input("Please enter your resolution. For example, if you're using a 128x128 resolution, only input 128! "))

## Equation 1= 0.075/(texture_resolution/16)
## Equation 2= 0.125/(texture_resolution/16)

val1=0.075
val2=0.125

## Scale 1 value in offset
scale_x = val1/(res / 16)

## Scale 2 value in offset
scale_y = val2/(res/16)

## Scale 3 value in offset
scale_z = val1/(res / 16)

##Print offset component with scale values
data = {'minecraft:render_offsets': {'main_hand': {'first_person': {'scale': [scale_x,scale_y,scale_z]},'third_person': {'scale': [scale_x,scale_y,scale_z]}},'off_hand': {'first_person': {'scale': [scale_x,scale_y,scale_z]},'third_person': {'scale': [scale_x,scale_y,scale_z]}}}}
jstr = json.dumps(data, indent=4)
print(jstr)
