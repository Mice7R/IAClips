import sys
from urllib import unquote

d = True
for l in sys.stdin:
  l = l.rstrip()
  if not l:
    d = False
  elif "3ACLIPS_TOP_LEVEL_SLOT_CLASS" in l:
    d = True

  if not d:
    print unquote(l)
