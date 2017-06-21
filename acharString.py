import random
from Populacao import Populacao
from datetime import datetime


class AcharString(Populacao):
    """."""

    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"

    def __init__(self, tamanho_objetivo, manter_populacao=0.4,
                 selecao_aleatoria=0.05, chance_mutacao=0.1,
                 tamanho_populacao=300):
        """."""
        self.tamanho_objetivo = tamanho_objetivo
        self.manter_populacao = manter_populacao
        self.selecao_aleatoria = selecao_aleatoria
        self.chance_mutacao = chance_mutacao
        self.tamanho_populacao = tamanho_populacao
        self.objetivo = ''.join(
            random.choice(self.geneset) for _ in xrange(tamanho_objetivo))

        self.fitness_maximo = len(self.objetivo)

        self.manter_tamanho = int(
            self.tamanho_populacao * self.manter_populacao)

        self.melhor_fitness_anterior = 0

        super(AcharString, self).__init__(
            self.objetivo, self.manter_populacao, self.selecao_aleatoria,
            self.chance_mutacao, self.tamanho_populacao, self.fitness_maximo)

    def fitness(self, individuo):
        """Funcao fitness."""
        return sum(
            1 for esp, atual in zip(self.objetivo,
                                    individuo.genes) if esp == atual)

    def criar_populacao_inicial(self):
        """Funcao para criar a populacao inicial."""
        self.populacao = []
        for i in xrange(self.tamanho_populacao):
            g = ''.join(random.choice(self.geneset)
                        for _ in xrange(self.tamanho_objetivo))
            self.populacao.append(self.Individuo(genes=g))

    def julgar_populacao(self):
        """Funcao para julgar qualidade do individuo."""
        for individuo in self.populacao:
            individuo.fitness = self.fitness(individuo=individuo)

        self.populacao = sorted(
            self.populacao, key=lambda ind: ind.fitness, reverse=True)

    def iniciar(self):
        """Inicia o processo."""
        random.seed()
        self.hora_inicio = datetime.now()
        self.criar_populacao_inicial()
        self.intervalo_geracao = datetime.now()
        return self.evoluir()

    def mutacao(self, individuo):
        """Funcao para mutar os genes de um individuo."""
        if self.chance_mutacao > random.random():
            gene_novo, gene_alt = random.sample(self.geneset, 2)
            lista_genes = list(individuo.genes)
            pos = random.randrange(0, len(lista_genes))
            lista_genes[pos] = gene_novo == lista_genes[pos] and\
                gene_alt or gene_novo
            individuo.genes = ''.join(lista_genes)

    def display(self, individuo):
        """Print das informacoes do individuo."""
        d = vars(individuo)
        if self.melhor_fitness_anterior < d['fitness']:
            log = open('log.txt', 'a+')
            tempo_passado_exec = datetime.now() - self.hora_inicio
            t = ('%s: %s\n' % ('Tempo de execu\xe7\xe3o',
                               str(tempo_passado_exec)))
            log.write(t)

            intervalo_geracao_tmp = datetime.now() - self.intervalo_geracao
            t = ('%s: %s\n' % ('Intervalo tempo gera\xe7\xe3o',
                               str(intervalo_geracao_tmp)))
            log.write(t)
            for key in d.keys():
                t = '%s: %s\n' % (key, d[key])
                log.write(t)
                if key == 'genes':
                    t = '%s: %s\n' % ('objet', self.objetivo)
                    log.write(t)

            log.write('\n')

            log.close()

            self.intervalo_geracao = datetime.now()
        return

    def evoluir(self):
        """Funcao para executar a evolucao da populacao."""
        self.julgar_populacao()

        melhor_individuo = self.populacao[0]

        self.display(individuo=melhor_individuo)

        self.melhor_fitness_anterior = melhor_individuo.fitness

        if melhor_individuo.fitness == self.fitness_maximo:
            return (melhor_individuo, self.objetivo)

        while True:
            progenitores = self.populacao[:self.manter_tamanho]

            for individuo in self.populacao[self.manter_tamanho:]:
                if self.selecao_aleatoria > random.random():
                    progenitores.append(individuo)

            progenitores_tam = len(progenitores)
            tamanho_desejado = self.tamanho_populacao - progenitores_tam
            descendentes = []
            while len(descendentes) < tamanho_desejado:
                pai = random.randrange(progenitores_tam)
                mae = random.randrange(progenitores_tam)

                if mae != pai:
                    pai = progenitores[pai]
                    mae = progenitores[mae]
                    meio = len(pai.genes) / 2
                    geracao_filho = max((mae.geracao, pai.geracao)) + 1
                    genes_filho = pai.genes[meio:] + mae.genes[:meio]
                    filho = self.Individuo(
                        genes=genes_filho, geracao=geracao_filho)
                    descendentes.append(filho)

            for individuo in descendentes:
                self.mutacao(individuo=individuo)

            progenitores.extend(descendentes)

            self.populacao = progenitores

            self.julgar_populacao()

            melhor_individuo = self.populacao[0]

            self.display(individuo=melhor_individuo)

            self.melhor_fitness_anterior = melhor_individuo.fitness

            if melhor_individuo.fitness == self.fitness_maximo:
                return (melhor_individuo, self.objetivo)
