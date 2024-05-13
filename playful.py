def nocolor(__s: str, /) -> str:
  if not __s.strip(): return __s
  from colorama import Fore, Back, Style
  
  for element in (Fore, Back, Style):
    for attr in dir(element):
      if attr.startswith("_"): continue
      __s = __s.replace(getattr(element, attr), "")
  
  return __s

def fixspaces(__s: str, /) -> str:
  if not __s: return ""
  return __s.replace("\t", " ")

def width(__s: str, /) -> int:
    return len(max(nocolor(fixspaces(__s)).splitlines()))

def height(__s: str, /) -> int:
  return len(nocolor(fixspaces(__s)).splitlines())

def dimensions(__s: str) -> tuple:
  return width(__s), height(__s)
