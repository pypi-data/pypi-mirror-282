from typing import List, Dict, Tuple, Union


class Info:
    """
    ^^^^^^^
    """
    @classmethod
    def print(cls):
        print(cls.__doc__)


Datas = List[Dict[int, Tuple[float, float, float, float]]]
Setups = Dict[str, Union[list, str, Dict[str, Union[int, str]], int]]
Record = List[List[Union[float, str, int]]]
