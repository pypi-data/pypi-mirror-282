# aval

## Abstract

**Abstract Validator** (``AVal``) is a class implemented in Python, capable 
of taking a list of specific validation strategies (with parameters), as well 
as a method for handling exceptional situations, and applying these methods to 
the validation object. The **Abstract Validator** can be used by calling the 
validation **method** on an instance of a class, as well as a **decorator**.

## Installation

Use:

``pip install aval``

## Basic usage
```
def _is_string(obj: v.VObj, params: v.VParams) -> None:
    t = type(obj)
    if t != str:
        raise v.ValidationError('Some description')


def _correct_length(obj: v.VObj, params: v.VParams) -> None:
    mn = params.get('min_length', 1)
    mx = params.get('max_length', 32)
    ln = len(obj)
    if not mn <= ln <= mx:
        raise v.ValidationError('Some description'
        )


vld = v.Validator([_is_string, _correct_length])
vld.validate('Any message')
```

## Details

More detailed documentation (in Russian) can be found at
https://docs.mxustin.ru/micro/validator/manual/intro