

import numbers
import pytest

VOLUME_LIMIT = 1_000_000
LENGTH_LIMIT = 150
WEIGHT_LIMIT = 20


@pytest.mark.parametrize('w,h,l,m,expected', [
    (1,1,1,1,'STANDARD'),    
    (10,10,10,10,'STANDARD'),    
    (100,100,100,100,'REJECTED'),    
    (10,100,100,100,'SPECIAL'),    
    ('',1,1,1,ValueError),
    (0,0,0,0,ValueError),
])
def test_sort(w, h, l, m, expected):
    if expected is ValueError:
        with pytest.raises(ValueError):
            sort(w,h,l,m)
    else:
        assert sort(w,h,l,m) == expected


def sort(width: float, height: float, length: float, mass:float) -> str:

    inputs = [width, height, length, mass]
    if not all([isinstance(x, numbers.Number) for x in inputs]):
        raise ValueError("All input values must be numbers")

    if any([x == 0 for x in inputs]):
        raise ValueError("Check your inputs, no measurement should be zero")

    # assuming that all linear meassurements should be positive
    width = abs(width)
    height = abs(height)
    length = abs(length)

    bulky, heavy = False, False
    if max(width, height, length) >= LENGTH_LIMIT or width*height*length >= VOLUME_LIMIT:
        bulky = True
    if mass >= WEIGHT_LIMIT:
        heavy = True

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"

# sort(1,1,1,1)
# sort('',1,1,1)
