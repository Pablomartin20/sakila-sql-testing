import pytest

@pytest.mark.idu
def test_fecha_devolucion_mayor(db_cursor):
  db_cursor.execute("""
  SELECT rental_id
  FROM rental
  WHERE return_date IS NOT NULL AND timediff(return_date, rental_date) <= 0
  """)
  rentals = db_cursor.fetchall()
  assert len(rentals) == 0, \
  f"Se encontraron alquileres con fecha de devolución menor a la de alquiler: {rentals}"

@pytest.mark.id
def test_cliente_nulo(db_cursor):
  db_cursor.execute("""
  SELECT rental_id
  FROM rental
  WHERE customer_id IS NULL
  """)
  rentals = db_cursor.fetchall()
  assert len(rentals) == 0, \
  f"Se encontraron alquileres con cliente nulo: {rentals}"

@pytest.mark.ir
def test_cliente_existente(db_cursor):
  db_cursor.execute("""
  SELECT r.rental_id, r.customer_id
  FROM rental r
  LEFT JOIN customer c ON r.customer_id = c.customer_id
  WHERE c.customer_id IS NULL
  """)
  rentals = db_cursor.fetchall()
  assert len(rentals) == 0, \
  f"Se encontraron alquileres con cliente no existente: {rentals}"

@pytest.mark.ir
def test_tienda_valida(db_cursor):
  db_cursor.execute("""
  SELECT r.rental_id, r.staff_id
  FROM rental r
  LEFT JOIN staff s ON r.staff_id = s.staff_id
  WHERE s.staff_id IS NULL
  """)
  rentals = db_cursor.fetchall()
  assert len(rentals) == 0, \
  f"Se encontraron alquileres con tienda no válida: {rentals}"

@pytest.mark.id
def test_inventario_existente(db_cursor):
  db_cursor.execute("""
  SELECT r.rental_id, r.inventory_id
  FROM rental r
  LEFT JOIN inventory i ON r.inventory_id = i.inventory_id
  WHERE i.inventory_id IS NULL
  """)
  rentals = db_cursor.fetchall()
  assert len(rentals) == 0, \
  f"Se encontraron alquileres asociados a inventario no existente: {rentals}"
