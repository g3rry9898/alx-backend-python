#!/usr/bin/env python3
from typing import Any, Optional, Sequence

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None

