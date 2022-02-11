class inout:
    def __init__(self, s=""):
        self.val=s
    def __lshift__(self, other):
        if other.val=="\n":
            print(other.val)
        else:
            print(other.val, end="")
        return other
    def __rshift__(self, other):
        other.val=input()
        return other
    def __str__(self):
        return str(self.val)
    def __bool__(self):
        return bool(str(self.val))
    def __int__(self):
        return int(str(self.val))
cin=inout("cin")
cout=inout("cout")
endl=inout("\n")