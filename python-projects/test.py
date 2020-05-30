import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        num=10
        result=main.do_stuff(num)
        self.assertEqual(result,15)
    
    def test_do_stuff1(self):
        test_param='ftfgyj'
        result=main.do_stuff(test_param)
        self.assertIsInstance(result,ValueError)
        
    def test_do_stuff2(self):
        test_param=None
        result=main.do_stuff(test_param)
        self.assertEqual(result,'Please enter number')
    
    def test_do_stuff3(self):
        test_param=None
        result=main.do_stuff(test_param)
        self.assertEqual(result,'Please enter number')
        
    def test_do_stuff4(self):
        test_param=''
        result=main.do_stuff(test_param)
        self.assertEqual(result,'Please enter number')
        
   
if __name__=='__main__':
     unittest.main()
     
     #used for running all unittest files in app
     #python -m unittest
     #python -m unittest -v (v-verbose)
     