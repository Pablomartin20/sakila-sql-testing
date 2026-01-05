import pytest

@pytest.mark.ie
def test_email_unico(db_cursor):
  db_cursor.execute("""
  SELECT LOWER(email), COUNT(*)
  FROM customer
  GROUP BY LOWER(email)
  HAVING COUNT(*) > 1
  """)
  clientes = db_cursor.fetchall()
  assert len(clientes) == 0, \
  f"Se encontraron clientes con email duplicado: {clientes}"

@pytest.mark.id
def test_clientes_sin_tienda(db_cursor):
  db_cursor.execute("""
  SELECT customer_id
  FROM customer
  WHERE store_id IS NULL
  """)
  clientes = db_cursor.fetchall()
  assert len(clientes) == 0, \
  f"Se encontraron clientes con tienda nula: {clientes}"

@pytest.mark.ir
def test_tienda_valida(db_cursor):
  db_cursor.execute("""
  SELECT c.customer_id, c.store_id
  FROM customer c
  LEFT JOIN store s ON c.store_id = s.store_id
  WHERE s.store_id IS NULL
  """)
  clientes = db_cursor.fetchall()
  assert len(clientes) == 0, \
  f"Se encontraron clientes con tienda no válida: {clientes}"

@pytest.mark.id
def test_estado_valido(db_cursor):
  db_cursor.execute("""
  SELECT customer_id
  FROM customer
  WHERE (active NOT IN (0,1) OR active IS NULL)
  """)
  clientes = db_cursor.fetchall()
  assert len(clientes) == 0, \
  f"Se encontraron clientes con un estado de cuenta no válido: {clientes}"

@pytest.mark.id
def test_direccion_valida(db_cursor):
  db_cursor.execute("""
  SELECT c.customer_id, c.address_id
  FROM customer c
  LEFT JOIN address a ON c.address_id = a.address_id
  WHERE a.address_id IS NULL
  """)
  clientes = db_cursor.fetchall()
  assert len(clientes) == 0, \
  f"Se encontraron clientes con dirección no registrada: {clientes}"

@pytest.mark.idu
def test_clientes_inactivos(db_cursor):
  db_cursor.execute("""
  SELECT c.customer_id
  FROM customer c
  LEFT JOIN rental r ON c.customer_id = r.customer_id
  WHERE c.active = 0 AND r.return_date IS NULL
  """)
  clientes = db_cursor.fetchall()
  assert len(clientes) == 0, \
  f"Se encontraron clientes inactivos con alquileres activos: {clientes}"

@pytest.mark.id
def test_clientes_sin_email(db_cursor):
  db_cursor.execute("""
  SELECT customer_id
  FROM customer
  WHERE email IS NULL
  """)
  clientes = db_cursor.fetchall()
  assert len(clientes) == 0, \
  f"Se encontraron clientes sin email registrado: {clientes}"
