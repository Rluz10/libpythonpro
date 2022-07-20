from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'Rluz10', 'id': 103536637, 'node_id': 'U_kgDOBivX_Q',
        'avatar_url': 'https://avatars.githubusercontent.com/u/103536637?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('rluz10')
    assert 'https://avatars.githubusercontent.com/u/103536637?v=4' == url