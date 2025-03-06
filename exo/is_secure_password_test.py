from exo.module_pwd import is_password_secure
def test_pass():
    assert is_password_secure('ldkjnqkdnfq68468484;!:;!:', 10)
    assert not is_password_secure('ldkjn', 10)
    assert not is_password_secure('!!!', 10)