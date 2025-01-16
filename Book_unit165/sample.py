''' Test '''

def hello_name(name: str) -> str:
    ''' Function 1 '''
    return f"Hello {name}"

def add_this(a: int, b: int) -> int:
    ''' Function 2 '''
    return a+b

# TODO: write something
print('test1')

# BUG: a bug
print('test2')

# FIXME: fixme tag
print('test3')


hello_name("iskren")

# python.exe -m pip install --upgrade pip
# pip install mypy-lang


print(add_this(1,2))

help(hello_name)

# use py -m pylint sample.py
