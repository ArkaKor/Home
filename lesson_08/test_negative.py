from yougile_api import YouGile_API

api = YouGile_API('https://yougile.com/api-v2/projects/')


def test_add_noname_project():
    name = ''
    add = api.creat_project(name)
    assert add == 400


def test_delete_project_noid():
    id = ''
    res = api.delete_project(id)
    assert res == 404


def test_find_noid_project():
    id = ''
    res = api.find_by_id(id)
    assert res == 404
