class Atendente(object):
    def __init__(self, CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente):
        self.CpfAtendente = CpfAtendente
        self.NomeAtendente = NomeAtendente
        self.SobrenomeAtendente = SobrenomeAtendente
        self.RgAtendente = RgAtendente
        self.EnderecoAtendente = EnderecoAtendente
        self.SalarioAtendente = SalarioAtendente
        self.TelefoneAtendente = TelefoneAtendente


class Cliente(object):
    def __init__(self, CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, Cpfatendente, TelefoneCliente):
        self.CpfCliente = CpfCliente
        self.NomeCliente = NomeCliente
        self.SobrenomeCliente = SobrenomeCliente
        self.RgCliente = RgCliente
        self.EnderecoCliente = EnderecoCliente
        self.Cpfatendente = Cpfatendente
        self.TelefoneCliente = TelefoneCliente


class Manobrista(object):
    def __init__(self, CnhManobrista, NomeManobrista, SobrenomeManobrista, RgManobrista, EnderecoManobrista, SalarioManobrista, TelefoneManobrista):
        self.CnhManobrista = CnhManobrista
        self.NomeManobrista = NomeManobrista
        self.SobrenomeManobrista = SobrenomeManobrista
        self.RgManobrista = RgManobrista
        self.EnderecoManobrista = EnderecoManobrista
        self.SalarioManobrista = SalarioManobrista
        self.TelefoneManobrista = TelefoneManobrista


class Vaga(object):
    def __init__(self, NumeroVaga, Situacao):
        self.NumeroVaga = NumeroVaga
        self.Situacao = Situacao
