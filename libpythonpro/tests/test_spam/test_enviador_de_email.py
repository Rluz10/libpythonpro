import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente', ['aaa@bar.com.br', 'rodrigo@python.com'])
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'luciano@python.com',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta'
    )
    assert remetente in resultado


@pytest.mark.parametrize('remetente', ['', 'rodrigo'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'luciano@python.com',
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta'
        )
