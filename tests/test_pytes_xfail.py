import pytest

@pytest.mark.xfail(reason="Найден баг в приложений, из за которого тест падает с ошибкой")
def test_with_bug():
    assert 1 + 1 == 3

@pytest.mark.xfail(reason="Баг уже исправлен, но на тесте все еще висит маркировака xfail")
def test_without_bug():
    ...

@pytest.mark.xfail(reason="Внешний сервис временно недоступен")
def test_external_service_is_unavailable():
    assert 1 + 1 == 3

