OneEditApart("cat", "dog") -> false 
OneEditApart("cat", "cats") -> true 
OneEditApart("cat", "cut") -> true 
OneEditApart("cat", "cast") -> true 
OneEditApart("cat", "at") -> true 
OneEditApart("cat", "acts") -> false 


def OneEditApart(a, b):
    changed = False
    if len(b) > len(a):
        a, b = b, a
    if len(a) - len(b) > 1:
        return False
    elif len(a) - len(b) > 0:
        i = 0
        while i < len(a):
            if a[i] != b[i]:
                if changed:
                    return False
                else:
                    changed = True
                    del a[i]
                    continue
    else:
        # lens equal
        for i in range(len(a)):
            if a[i] != b[i]:
                if changed:
                    return False
                else:
                    changed = True
