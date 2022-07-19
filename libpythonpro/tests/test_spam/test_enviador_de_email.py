import pytest

from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('destinatario', ['aaa@bar.com.br', 'rodrigo@python.com'])
def test_remetente(destinatario):
    enviador = Enviador()
    destinatarios = ['aaa@bar.com.br', 'rodrigo@python.com']
    destinatario
    resultado = enviador.enviar(
        destinatario,
        'luciano@python.com',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta'
    )
    assert destinatario in resultado
