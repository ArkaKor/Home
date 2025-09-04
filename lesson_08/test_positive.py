from yougile_api import YouGile_API

api = YouGile_API('https://yougile.com/api-v2/projects/')


def test_add_project():
    name = 'post test'
    add = api.creat_project(name)
    assert add == 201


def test_delete_project():
    name = 'put test'
    id = api.get_new_id(name)
    res = api.delete_project(id)
    assert res == 200


def test_list_project():
    res = api.get_list_project()
    assert res == 200


def test_cleaner():
    res = api.cleaner()
    assert res is None
