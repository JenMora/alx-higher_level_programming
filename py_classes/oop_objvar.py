class Robot:
    """A RObot with a name."""
    ...
    population = 0

    def __init__(self, name):
        """initialize the data"""

        self.name = name
        print("(initializing{})".format(self.name))
        #when the robot was creeated
        #aaditional info to the population field
        Robot.population = population + 1

    def die(self):
        """I will never die before i fulfill my purpose"""
        print("{} will be destroyed".format(self.name))

        Robot.population = population - 1

        if Robot.population == 0:
            pprint("{} was the last one.".format(self.name))
        else:
            print("There are still{:d} robots working.".format(Robot.population))
    def say_hi(self):
        """Greetings
        YEs, that is a simple task"""
        print("Greetings, my name is {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population"""
        print("there are {:d} robots.".format(cls.population))

        droid1 = Robot("R2-D2")
        droid1.say_hi()
        Robot.how_many()

        droid2 = Robot("C-3PO")
        droid2.say_hi()
        Robot.how_many()

        print("\nRobots can do some work here.\n")

        print("I am done here\n")

        droid1.die()
        droid2.die()

        Robot.how_many()
