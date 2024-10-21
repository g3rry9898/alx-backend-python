#!/usr/bin/env python3

from typing import List, Tuple, Union

def zoom_array(lst: Tuple[Union[int, float], ...], factor: int = 2) -> List[Union[int, float]]:
    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array: Tuple[int, int, int] = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)

