import unittest as un

def add(a,b):
    return a+b

class demoTest(un.TestCase):
    def test_add_4_5(self):
        self.assertEqual(add(4,5),9)
if __name__=='__main__':
    #un.main()
    un.TextTestRunner().run(un.TestLoader().loadTestsFromTestCase(demoTest))