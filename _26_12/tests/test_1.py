import pytest
from os import remove
from proga import CRUD, KwargsError

path = 'db.csv'

text = '''1, Deyman, Qr, 20.03.2007, Fish, 1
2, Waldis, Jr, 10.04.1999, Lion, 0
3, Terra, Faster, 20.03.2000, Ram, 0
4, Dima, Cherenkov, 26.11.1990, God, 1
5, Nikita, Maker, 03.08.2007, Virgin, 0
'''


class TestCRUD:
    def setup_class(cls):
        with open(path, 'w', encoding='UTF-8') as f:
            f.write(text)
        print('\nFile \'db.csv\' created')
        cls.crud = CRUD(path)
        print('CRUD created')

    def teardown_class(cls):
        remove(path)
        print('\nFile \'db.csv\' removed')
        del cls.crud
        print('CRUD removed')

    def test_read_1(self):
        assert self.crud.read(id=2) == [{
            'id': 2, 'name': 'Waldis', 'surname': 'Jr', 'bd': '10.04.1999', 'zodiac_sign': 'Lion', 'loves_green': 0
        }]

    def test_read_2(self):
        with pytest.raises(KwargsError) as e:
            self.crud.read(a=14)
        assert "'a' is not a key" in str(e)

    def test_read_3(self):
        with pytest.raises(TypeError) as e:
            self.crud.read(name=123)
        assert "'name' must be <class 'str'>, not <class 'int'>" in str(e)

    def test_read_4(self):
        assert len(self.crud.read(id=2, name="Deyman")) == 0

    def test_create_1(self):
        self.crud.create(id=10, name='Lol', surname='Kek', bd = '01.01.1000', zodiac_sign='Scorpion', loves_green=1)
        with open(path, encoding='UTF-8') as f:
            assert '10, Lol, Kek, 01.01.1000, Scorpion, 1' in ''.join(f.readlines())

    def test_create_2(self):
        with pytest.raises(KwargsError) as e:
            self.crud.create(name='Deymian', loves_green=1)
        assert 'Not all kwargs' in str(e)

    def test_create_3(self):
        with pytest.raises(ValueError) as e:
            self.crud.create(id=2, name='Lol', surname='Kek', bd = '01.01.1000', zodiac_sign='Scorpion', loves_green=1)
        assert 'id is alreay in use' in str(e)

    def test_create_4(self):
        self.crud.create(id=7, name='Lol', surname='Kek', bd = '01.01.1000', zodiac_sign='Scorpion', loves_green=1)
        with open(path, encoding='UTF-8') as f:
            assert ''.join(f.readlines()).count('Lol') == 2

    def test_update_1(self):
        self.crud.update(10, name='Lolik')
        with open(path, encoding='UTF-8') as f:
            for i in f:
                if i.split(', ')[0] == '10':
                    assert i.split(', ')[1] == 'Lolik'
                    break
            else:
                assert False

    def test_update_2(self):
        with pytest.raises(ValueError) as e:
            self.crud.update(11, name='a')
        assert 'id didn\'t used yet' in str(e)

    def test_update_3(self):
        with pytest.raises(ValueError) as e:
            self.crud.update(10, id=3)
        assert 'new id is alreay in use' in str(e)

    def test_update_4(self):
        with pytest.raises(KwargsError) as e:
            self.crud.update(10, lol='kek')
        assert "'lol' is not a key" in str(e)

    def test_delete_1(self):
        self.crud.delete(name='Lolik')
        with open(path, encoding='UTF-8') as f:
            assert 'Lolik' not in ''.join(f.readlines())

    def test_delete_2(self):
        with open(path, encoding='UTF-8') as f:
            data = f.readlines()
        self.crud.delete(id=12)
        with open(path, encoding='UTF-8') as f:
            assert data == f.readlines()

    def test_delete_3(self):
        with pytest.raises(KwargsError) as e:
            self.crud.delete(abc='def')
        assert "'abc' is not a key" in str(e)
