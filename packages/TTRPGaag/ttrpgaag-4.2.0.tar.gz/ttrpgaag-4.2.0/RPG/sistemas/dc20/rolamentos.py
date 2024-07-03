from ...dado import Dado


class Rolamento:
    def __init__(self,
                 modificador: int = 0,
                 dc: int = 10,
                 vantagens: int = 0,
                 desvantagens: int = 0) -> None:
        """
        Gera um rolamento para determinada habilidade ou ataque

        rolamento = Rolamento(modificador: 4, dc: 15, vantagens: 1)

        print(rolamento) -> Rolamento: 0 vs DC 10. Vant: 0, DesVant: 0. Total: 10 # valor aleatório

        * modificador: o modificador no rolamento dos dados (valor da habilidade). Padrão: 0
        * dc: o número alvo para o rolamento. Padrão: 10
        * vantagens: a quantidade de vantagens no rolamento. Padrão 0
        * desvantagens: a quantidade de desvantagens no rolamento. Padrão 0
        """
        self.modificador = modificador
        self.dc = dc
        self.vantagens = vantagens
        self.desvantagens = desvantagens

        self._qtd_dados = self._calcular_dados()
        self._vantagem = self._calcula_vantagem()
        self._desvantagem = self._calcula_desvantagem()

        self._rolar_dados()


    def __str__(self) -> str:
        return f'Rolamento: {self.modificador} vs DC {self.dc}. Vant: {self.vantagens}, DesVant: {self.desvantagens}. Resultado: {self.total}. {self.resultado}'


    def __repr__(self) -> str:
        return f'<Rolamento {self.modificador} vs DC {self.dc}, {self.vantagens} Vant, {self.desvantagens} DesVant. Rolamento: {self.dados}'


    # Métodos privados =========================================================
    def _calcular_dados(self):
        return 1 + abs(self.vantagens - self.desvantagens)


    def _calcula_vantagem(self):
        return self.vantagens > self.desvantagens


    def _calcula_desvantagem(self):
        return self.desvantagens > self.vantagens


    def _rolar_dados(self):
        self._dados = Dado(self._qtd_dados, 20)


    def _escolhe_dado(self):
        if self._vantagem:
            return self._dados.maior

        if self._desvantagem:
            return self._dados.menor

        return self._dados[0]


    # Métodos ==================================================================
    def rerolar(self):
        self._dados.rerolar


    # Propriedades =============================================================
    @property
    def dados(self):
        return self._dados.rolamento


    @property
    def dado(self):
        return self._escolhe_dado()


    @property
    def total(self):
        return self.dado + self.modificador


    @property
    def sucesso(self):
        return self.total >= self.dc


    @property
    def critico(self):
        return self.dado == 1 or self.dado == 20


    @property
    def diferenca(self):
        return abs(self.total - self.dc)


    @property
    def resultado(self):
        texto = 'Sucesso' if self.sucesso else 'Falha'

        if self.critico:
            texto += ' crítico' if self.sucesso else ' crítica'

        texto += f'. Diferença: {self.diferenca}'

        return texto
