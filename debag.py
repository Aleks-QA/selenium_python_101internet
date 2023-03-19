import pytest

my_list = [5, 2, 3]


@pytest.fixture(scope="module", params=my_list)
def my_params(request):
    return request.param


class Test_suite:
    def test_1(self, my_params):
        print(my_params)
        assert 1 == 1

    def test_2(self, my_params):
        print(my_params)
        assert 1 == 1

    def test_3(self, my_params):
        print(my_params)
        assert 1 == 1
