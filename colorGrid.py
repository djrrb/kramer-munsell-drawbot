# uses https://github.com/samdroid-apps/python-munsell
from munsell import _xyy_to_rgb_linear

def lerp(start, stop, amt):
	"""
	Return the interpolation factor (between 0 and 1) of a VALUE between START and STOP.
	https://processing.org/reference/lerp_.html
	"""
	return float(amt-start) / float(stop-start)
	
def norm(value, start, stop):
	"""
	Interpolate using a value between 0 and 1
	See also: https://processing.org/reference/norm_.html
	"""
	return start + (stop-start) * value

w, h = 1000, 1000
grid = 50
pages = 10

color1Min = 0 # x
color1Max = 1 # x

color2Min = 0 # y
color2Max = 1 # y

color3Min = 1 # pages
color3Max = 255 # pages


for z in range(pages):
    newPage(w, h)
    factor = lerp(0, pages, z)
    color3 = norm(factor, color3Min, color3Max)
    # loop through columns
    for y in range(0, height(), grid):
        # interpolate between 0 and 1 to get color value
        factor = lerp(0, height(), y)
        color2 = norm(factor, color2Min, color2Max)
        for x in range(0, width(), grid):

            factor = lerp(0, width(), x)
            color1 = norm(factor, color1Min, color1Max)

            r, g, b = _xyy_to_rgb_linear(
                color1, 
                color2, 
                color3)
            fill(r, g, b)
            rect(x, y, grid, grid)
            
saveImage('grid.gif')
