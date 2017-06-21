import unittest
from acharString import AcharString


class Tests(unittest.TestCase):
    """."""

    def test(self):
        """."""
        tamanho_obj = 10
        tamanho_pop = 500
        t = AcharString(
            tamanho_objetivo=tamanho_obj, tamanho_populacao=tamanho_pop)

        melhor, obj = t.iniciar()

        m = vars(melhor)

        print "objetivo: %s\n" % (obj)

        for key in m.keys():
            print '%s: %s\n' % (key, m[key])

if __name__ == '__main__':
    unittest.main()
