class inout(object):
    def __init__(self, s=""):
        self.val=s
    def __lshift__(self, other):
        if str(other)=="\n":
            print(other)
        else:
            print(other, end="")
        return inout(other)
    def __rshift__(self, other):
        other.val=input()
        return inout(other)
    def __str__(self):
        return str(self.val)
    def __bool__(self):
        return bool(str(self.val))
    def __int__(self):
        return int(str(self.val))
cin=inout("cin")
cout=inout("cout")
endl=inout("\n")
