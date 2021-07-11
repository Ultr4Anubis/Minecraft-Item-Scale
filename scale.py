
import json

print('Thankyou for using my scale generator.')

RESOLUTION = int(input("Please enter your resolution. For example, if you're using a 128x128 resolution, only input 128! "))

## x, z = 0.075/(texture_resolution/16)
## y    = 0.125/(texture_resolution/16)

values = [0.075, 0.125]

## Scale values in offset
scales = [
	values[0]/(RESOLUTION/16),
	values[1]/(RESOLUTION/16),
	values[0]/(RESOLUTION/16)
]

##Print offset component with scale values
data = {
	'minecraft:render_offsets': {
		'main_hand': {
			'first_person': {'scale': scales},
			'third_person': {'scale': scales}
		},
		'off_hand': {
			'first_person': {'scale': scales},
			'third_person': {'scale': scales}
		}
	}
}
jstr = json.dumps(data, indent=4)

print(jstr)
