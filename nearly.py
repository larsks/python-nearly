def compare(this, that):
    if this is ... or that is ...:
        return True

    if type(this) != type(that):
        return False

    match this:
        case list() | tuple():
            if len(this) == 0:
                return len(that) == 0 or that[0] is ...

            if len(that) == 0:
                return len(this) == 0 or this[0] is ...

            if this[0] is ... and len(that) >= len(this):
                return compare(this[1:], that[-len(this) + 1 :])

            if this[-1] is ...:
                mark = this.index(...)
                if len(that) >= mark:
                    return compare(this[0:mark], that[0:mark])

            if that[0] is ... and len(this) >= len(that):
                return compare(that[1:], this[-len(that) + 1 :])

            if that[-1] is ...:
                mark = that.index(...)
                if len(this) >= mark:
                    return compare(this[0:mark], that[0:mark])

            if len(this) != len(that):
                return False

            for item in zip(this, that):
                if not compare(item[0], item[1]):
                    return False

            return True
        case set():
            if ... in this:
                return all(item in that for item in this if item is not ...)

            if ... in that:
                return all(item in this for item in that if item is not ...)
        case dict():
            if ... not in this and ... not in that:
                if this.keys() == that.keys():
                    return all(compare(this[k], that[k]) for k in this)

            if ... in this:
                try:
                    return all(compare(this[k], that[k]) for k in this if k is not ...)
                except KeyError:
                    return False

            if ... in that:
                try:
                    return all(compare(this[k], that[k]) for k in that if k is not ...)
                except KeyError:
                    return False

    return this == that


class Nearly:
    def __init__(self, proxy):
        self.proxy = proxy

    def __eq__(self, that):
        return compare(self.proxy, that)

    def __repr__(self):
        return self.proxy.__repr__()

    def __str__(self):
        return self.proxy.__str__()

    def __contains__(self, value):
        return value in self.proxy or ... in self.proxy
