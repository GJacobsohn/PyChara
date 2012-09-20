__author__ = 'gabriel'

def a(b):
    try:
       if b>2:
          b=10
       for i in range(1,b):
          print "McCabe"
       else:
          b=10
       while (b>5):
          b-=1
       else:
          b=5
    except NameError:
        print "Help"
    except TypeError:
        print "Be should be function"
    finally:
        return 42

class testClass():
    def ABC(self, feeling):
        class av():
            def ab(self):
                id =2
        if (feeling == "good"):
            print "HEEELLLLOOO World."
        elif (feeling == "ok"):
            print "HELLO WORLD"
        else:
            print "bye World"

    def feelbarometer(self, feelnumber):
        def bvc():
            return 1+1
        while feelnumber >0:
            feelnumber -= 1
        else:
            feelnumber=0


def classy_function():
    try:
        print "nnon"
    except BytesWarning:
        print "yes yes"

