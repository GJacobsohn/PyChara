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