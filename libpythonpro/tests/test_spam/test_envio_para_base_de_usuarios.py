from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviardorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviardorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'rodrigo@pynthon',
        'Curso Pynthon Pro',
        'Confira módulos fantásticos'
    )