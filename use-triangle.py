from geometry.triangle import areatriangle

print(f'calculate area triangle {areatriangle(20,100)}')

"""
"from geometry.triangle import areatriangle" sometimes, this function might make mistake, we could have the same
function but in different file, thus we use alias
or we can use syntax:
import geometry.triangle as ta
print(f'calculate area triangle {gs.areatriangle(20,100)}')
"""

