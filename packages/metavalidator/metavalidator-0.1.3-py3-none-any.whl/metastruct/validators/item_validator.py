from typing import Type

from metastruct.basetypes import ErrEnum
from metastruct.validators.item_constructor import (contruct_item_from_data,
                                                    contruct_item_from_text)


def is_valid_item(raw, constructor: Type) -> bool:
    """Check if the raw text is of valid structure as per constructor.
    Parameters
    ----------
    rawtext : str
    constructor : Type
        Any class constructor

    Example
    -------
    >>> class Person:
    >>>     def __init__(self, name, age):
    >>>         self.name = name
    >>>         self.age = age
    >>>         print("Person created")
    >>> is_valid_rawtext('{"name": "John", "age": 30}', Person)

    Returns
    -------
    bool
        True if the raw text is _both_ a valid json _and_ a valid structure for
        the constructor, False otherwise
    """
    if isinstance(raw, str):
        status = contruct_item_from_text(raw, constructor)
        return status == ErrEnum.NO_ERR
    elif isinstance(raw, dict):
        return isinstance(
            contruct_item_from_data(raw, constructor),
            constructor
        )
    else:
        raise TypeError(f"Invalid type: {type(raw)}")
