class HelloWorld(object):
    def __init__(self):
        self.name = "Noname"

    def hi(self):
        """ Say hi with out argument
        Examples:
        | Say Hi |
        """
        print("Say hi " + self.name)

    def hi2(self, name):
        """ Say hi with a argument.
        Examples:
        Say hi   <name>
        | Say Hi | name |
        """
        self.name = name
        print("Say hi " + self.name)
