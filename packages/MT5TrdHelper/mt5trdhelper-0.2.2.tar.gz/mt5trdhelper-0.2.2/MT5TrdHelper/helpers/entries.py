import enum


class MyEnumMeta(enum.EnumMeta):
    """
    It will be used to check if the value exist in enum
    """
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        else:
            return True


class Entry(enum.Enum, metaclass=MyEnumMeta):
    """
    Use like Entry.Buy,
    to check 0 in Entry
    """
    Buy = 1,
    Sell = 2
    Buy_Bet = 3
    Sell_Bet = 4
    HOLD = 5
    EXIT = 6

    def __str__(self):
        return self.name
