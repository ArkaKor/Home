from sqlalchemy import create_engine, inspect, text


db_connection_string = "postgresql://postgres:admin@localhost:5432/SkyPro QA"
db = create_engine(db_connection_string)
my_params = {
    'email': 'trig@use.com',
    'teacher_id': 3238
    }


def test_open():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[4] == 'teacher'


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO teacher(\"email\") VALUES (:email)")
    connection.execute(sql, my_params)

    name = text("select teacher_id, email from teacher where email = :email")
    res = connection.execute(name, my_params).fetchall()
    assert len(res) >= 1

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text(
        "UPDATE teacher SET teacher_id = :teacher_id WHERE email = :email")
    connection.execute(sql, my_params)

    name = text("select teacher_id, email from teacher where email = :email")
    res = connection.execute(name, my_params).fetchall()
    assert res[0][0] == my_params['teacher_id']

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM teacher WHERE email = :email")
    connection.execute(sql, my_params)

    name = text("select teacher_id, email from teacher where email = :email")
    res = connection.execute(name, my_params).fetchall()
    assert len(res) == 0

    transaction.commit()
    connection.close()
