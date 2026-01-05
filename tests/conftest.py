import pytest
import sqlite3

#Conexión a la base de datos
@pytest.fixture(scope="session")
def db_connection():
  conn = sqlite3.connect("sakila.db")
  yield conn
  conn.close()

#Creamos el cursor para usar en los tests
@pytest.fixture
def db_cursor(db_connection):
  cursor = db_connection.cursor()
  yield cursor
  db_connection.rollback()
  cursor.close()