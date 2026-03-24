
class Cliente:
    def __init__(self, nome, telefone, mensagem, vendedora_responsavel):
        self.nome = nome
        self.telefone = self._formatar_telefone(telefone)
        self.mensagem = mensagem
        self.vendedora_responsavel = vendedora_responsavel
        self.status_envio = 'Pendente'

    def _formatar_telefone(self, tel):
        apenas_numeros = ''.join(filter(str.isdigit, str(tel)))

        if not apenas_numeros.startswith('55'):
            apenas_numeros = '55' + apenas_numeros

        return apenas_numeros
    
    def __repr__(self):
        return f'<Cliente: {self.nome} - {self.telefone}>'