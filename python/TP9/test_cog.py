import unittest
from cog import cog



class CogTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CogTest, self).__init__(*args, **kwargs)
        self.c=cog()

    def test1(self):
        actual=self.c.department_name(91)
        expected='Essonne'
        self.assertEqual(actual, expected)

    def test2(self):
        actual=self.c.department_name(26)
        expected='Drôme'
        self.assertEqual(actual, expected)

    def test3(self):
        actual=self.c.department_name('2A')
        expected='Corse-du-Sud'
        self.assertEqual(actual, expected)

    def broken(self):
        self.c.department_name(100)

    def test4(self):
        self.assertRaises(ValueError, self.broken)

    def test5(self):
        actual=self.c.department_set('ILE-DE-FRANCE')
        expected={'Essonne',
                  'Hauts-de-Seine',
                   'Paris',
                   'Seine-Saint-Denis',
                   'Seine-et-Marne',
                   "Val-d'Oise",
                   'Val-de-Marne',
                   'Yvelines'}
        self.assertEqual(actual, expected)

    
    def test6(self):
        actual=self.c.department_set('BRETAGNE')
        expected={"Côtes-d'Armor", 'Finistère', 'Ille-et-Vilaine', 'Morbihan'}
        self.assertEqual(actual, expected)

    def test7(self):
        actual=self.c.department_set('CENTRE')
        expected={'Cher', 'Eure-et-Loir', 'Indre', 'Indre-et-Loire', 'Loir-et-Cher', 'Loiret'}
        self.assertEqual(actual, expected)

    def test8(self):
        actual=self.c.department_set('MORDOR')
        expected=set()
        self.assertEqual(actual, expected)

if __name__=='__main__':
    unittest.main()