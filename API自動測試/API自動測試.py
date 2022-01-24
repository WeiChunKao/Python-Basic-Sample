import unittest
from WebApi import app
class MTestCase( unittest.TestCase):
    def test_1(self):
        app.testing=True
        response=app.test_client().get('/')
        print(type(response.data))
        print(response.data)
        source=response.data.decode('UTF-8')
        print(type(source))
        print(source)
        self.assertEquals(response.status_code,200)
    def test_2(self):
        app.testing=True
        response=app.test_client().post('/login',data={'A':1,'B':2})
        data=response.data.decode('UTF-8')
        self.assertEqual(data,'3')
if __name__=='__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(MTestCase))
    #unittest.main()
