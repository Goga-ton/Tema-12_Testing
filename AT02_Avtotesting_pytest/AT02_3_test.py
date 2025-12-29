import pytest
from AT02_3_code import init_db, add_user, get_user

@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()

def test_add_user(db_conn):
    add_user(db_conn, 'Sergey', 36)
    user = get_user(db_conn, 'Sergey')
    assert user == (1, "Sergey", 36)