import pytest

@pytest.mark.ir
def test_clientes_existentes(db_cursor):
  db_cursor.execute("""
  SELECT p.payment_id, p.customer_id
  FROM payment p
  LEFT JOIN customer c ON c.customer_id = p.customer_id
  WHERE c.customer_id IS NULL
  """)
  payments = db_cursor.fetchall()
  assert len(payments) == 0, \
  f"Se encontraron pagos asociados a clientes no existentes: {payments}"

@pytest.mark.ir
def test_tiendas_validas(db_cursor):
  db_cursor.execute("""
  SELECT p.payment_id, p.staff_id
  FROM payment p
  LEFT JOIN staff s ON p.staff_id = s.staff_id
  WHERE s.staff_id IS NULL
  """)
  payments = db_cursor.fetchall()
  assert len(payments) == 0, \
  f"Se encontraron pagos asociados a tiendas no válidas: {payments}"

@pytest.mark.ir
def test_pagos_con_alquiler(db_cursor):
  db_cursor.execute("""
  SELECT p.payment_id
  FROM payment p
  LEFT JOIN rental r ON r.rental_id = p.rental_id
  WHERE r.rental_id IS NULL
  """)
  payments = db_cursor.fetchall()
  assert len(payments) == 0, \
  f"Se encontraron pagos sin alquiler: {payments}"

@pytest.mark.idu
def test_fecha_pago_anterior(db_cursor):
  db_cursor.execute("""
  SELECT p.payment_id, p.rental_id
  FROM payment p
  LEFT JOIN rental r ON r.rental_id = p.rental_id
  WHERE timediff(p.payment_date,r.rental_date) < 0
  """)
  payments = db_cursor.fetchall()
  assert len(payments) == 0, \
  f"Se encontraron pagos con fecha de realización anterior a la de alquiler: {payments}"

@pytest.mark.ie
def test_pagos_duplicados(db_cursor):
  db_cursor.execute("""
  SELECT payment_id, customer_id, rental_id
  FROM payment
  GROUP BY customer_id, rental_id
  HAVING COUNT(*) > 1
  """)
  payments = db_cursor.fetchall()
  assert len(payments) == 0, \
  f"Se encontraron pagos con fecha de realización anterior a la de alquiler: {payments}"
