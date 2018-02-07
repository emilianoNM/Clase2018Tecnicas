class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for  cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print ("B")
    except D:
        print ("D")
    except C:
        print ("C")
#    except B:
#        print ("B")
