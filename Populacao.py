class Populacao(object):
    """Classe Populacao."""

    class Individuo(object):
        """Classe individuo."""

        def __init__(self, genes=None, fitness=None, geracao=0):
            """Init para classe individuo."""
            self.genes = genes
            self.fitness = fitness
            self.geracao = geracao

    def fitness(self):
        """Funcao fitness para o individuo."""
        pass

    def mutacao(self):
        """Funcao de mutacao para o individuo."""
        pass

    def criar_populacao_inicial(self):
        """Funcao para criar os individuos da populacao."""
        pass

    def julgar_populacao(self):
        """Funcao para order os individuos pelo fitness."""
        pass

    def iniciar(self):
        """Funcao para iniciar o processo."""
        pass

    def display(self):
        """Print das informacoes do individuo."""
        pass

    def evoluir(self):
        """Funcao para executar a evolucao da populacao."""
        pass

    def __init__(self, objetivo, manter_populacao, selecao_aleatoria,
                 chance_mutacao, tamanho_populacao, fitness_maximo, **kwargs):
        """Init da classe Populacao."""
        self.objetivo = objetivo
        self.manter_populacao = manter_populacao
        self.selecao_aleatoria = selecao_aleatoria
        self.chance_mutacao = chance_mutacao
        map(lambda key: setattr(self, key, kwargs[key]), kwargs.keys())
