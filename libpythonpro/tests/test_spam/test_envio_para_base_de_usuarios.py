import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviardorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Rodrigo', email='rodrigo@python'),
            Usuario(nome='Souza', email='rodrigo@python')
        ],
        [
            Usuario(nome='Rodrigo', email='rodrigo@python')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviardorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'rodrigo@pynthon',
        'Curso Pynthon Pro',
        'Confira módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados