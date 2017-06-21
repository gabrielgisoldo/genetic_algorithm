import unittest
from acharString import AcharString
from acharLista import AcharLista


class Tests(unittest.TestCase):
    """."""

    def test_string(self):
        """."""
        print "Teste com String\n"

        tamanho_obj = 10
        tamanho_pop = 500
        t = AcharString(
            tamanho_objetivo=tamanho_obj, tamanho_populacao=tamanho_pop)

        melhor, obj = t.iniciar()

        m = vars(melhor)

        print "objetivo: %s\n" % (obj)

        for key in m.keys():
            print '%s: %s\n' % (key, m[key])

    def test_lista(self):
        """."""
        print "Teste com Lista\n"

        t = AcharLista(
            minimo=0, maximo=100, tamanho_genes=18, objetivo=1750)

        melhor, obj = t.iniciar()

        m = vars(melhor)

        print "objetivo: %s\n" % (obj)

        for key in m.keys():
            print '%s: %s\n' % (key, m[key])

suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
unittest.TextTestRunner(verbosity=2).run(suite)
