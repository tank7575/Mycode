from Duck import *
from Mouse import *

def describe(object):
    print("^>^>^>^ describe")
    object.talk()
    object.coat()

donald = Duck()
mickey = Mouse()

describe(donald)
describe(mickey)
