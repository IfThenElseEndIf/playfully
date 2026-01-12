"A library for playing with strings."

__all__: tuple = (
    "height", "width", "size", "padding", "mirror", "box"
)

def height(__s: str, /) -> int:
    "Returns the height of the string."
    if not isinstance(__s, str):
        raise TypeError(f"expected 'str' but got {type(__s).__name__!r}")
    
    return len(__s.splitlines())

def width(__s: str, /) -> int:
    "Returns the width of the string."
    if not isinstance(__s, str):
        raise TypeError(f"expected 'str' but got {type(__s).__name__!r}")
    
    if not __s: return 0
    return len(max(__s.splitlines()))

def size(__s: str, /) -> int:
    "Returns the total (square) size of a string."
    if not isinstance(__s, str):
        raise TypeError(f"expected 'str' but got {type(__s).__name__!r}")
    
    if not __s: return 0
    return height(__s) * width(__s)

def padding(__s: str, /) -> str:
    "Returns the given string with padding."
    if not isinstance(__s, str):
        raise TypeError(f"expected 'str' but got {type(__s).__name__!r}")
    
    if (__s == "") or (height(__s) == 1): return __s
    
    return "\n".join(f"{line:<{width(__s)}}" for line in __s.splitlines())

def mirror(__s: str, /) -> str:
    "Returns the given string but with each line reversed (the order of the lines is not reversed)."
    if not isinstance(__s, str):
        raise TypeError(f"expected 'str' but got {type(__s).__name__!r}")
    
    if __s == "": return ""
    
    return "\n".join(line[::-1] for line in padding(__s).splitlines())

def box(__s: str, /) -> str:
    "Returns a 'box' with the given string as its content."
    if not isinstance(__s, str):
        raise TypeError(f"expected 'str' but got {type(__s).__name__!r}")
    
    if __s == "": return "┌┐\n└┘"
    result: list = [f"┌{'─' * width(__s)}┐"]
    
    for line in __s.splitlines():
        result.append(f"│{line + ' ' * (width(__s) - len(line))}│")
    
    result.append(f"└{'─' * width(__s)}┘")
    
    return "\n".join(result)

def join(__a: str, __b: str, /) -> str:
	if not isinstance(__a, str):
        raise TypeError(f"expected 'str' but got {type(__a).__name__!r}")
	if not isinstance(__b, str):
        raise TypeError(f"expected 'str' but got {type(__b).__name__!r}")
	result: str = ""

	if height(__a) > height(__b):
		for _ in range(height(__b)):
			result += f"{__a.splitlines()[_]:<{width(__a)}}" + f"{__b.splitlines()[_]}\n"

		for _ in range(height(__a) - height(__b)):
			result += f"{__a.splitlines()[_ + height(__b)]}\n"

		return result[:-1]

	elif height(__b) > height(__a):
		paddings: str = " " * width(__a)
		
		for _ in range(height(__a)):
			result += f"{__a.splitlines()[_]:<{width(__a)}}" + f"{__b.splitlines()[_]}\n"

		for _ in range(height(__b) - height(__a)):
			result += f"{paddings}{__b.splitlines()[_ + height(__a)]}\n"

		return result[:-1]

	else:
		for _ in range(height(__b)):
			result += f"{__a.splitlines()[_]:<{width(__a)}}" + f"{__b.splitlines()[_]}\n"

		return result[:-1]
