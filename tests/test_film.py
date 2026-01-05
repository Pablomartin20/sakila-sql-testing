import pytest

@pytest.mark.idu
def test_duracion_alquiler(db_cursor):
  db_cursor.execute("""
  SELECT film_id
  FROM film
  WHERE rental_duration NOT BETWEEN 3 AND 7
  """)
  films = db_cursor.fetchall()
  assert len(films) == 0, \
  f"Se encontraron películas con una duración de alquiler inválida: {films}"

@pytest.mark.id
def test_precios_alquiler_positivo(db_cursor):
  db_cursor.execute("""
  SELECT film_id
  FROM film
  WHERE rental_rate <= 0
  """)
  films = db_cursor.fetchall()
  assert len(films) == 0, \
  f"Se encontraron películas con precio de alquiler negativo o cero: {films}"

@pytest.mark.id
def test_precios_reemplazo_positivo(db_cursor):
  db_cursor.execute("""
  SELECT film_id
  FROM film
  WHERE replacement_cost <= 0
  """)
  films = db_cursor.fetchall()
  assert len(films) == 0, \
  f"Se encontraron películas con precio de reposición negativo o cero: {films}"

@pytest.mark.idu
def test_precio_alquiler_menor(db_cursor):
  db_cursor.execute("""
  SELECT film_id
  FROM film
  WHERE rental_rate >= replacement_cost
  """)
  films = db_cursor.fetchall()
  assert len(films) == 0, \
  f"Se encontraron películas con precio de alquiler mayor o igual al de reposición: {films}"

@pytest.mark.idu
def test_clasificacion_edad(db_cursor):
  db_cursor.execute("""
  SELECT film_id
  FROM film
  WHERE rating IS NULL OR rating NOT IN ('G','PG','PG-13','R','NC-17')
  """)
  films = db_cursor.fetchall()
  assert len(films) == 0, \
  f"Se encontraron películas con clasificación de edad nula o inválida: {films}"

@pytest.mark.ir
def test_lenguaje_principal_existe(db_cursor):
  db_cursor.execute("""
  SELECT f.film_id
  FROM film f
  LEFT JOIN language l ON f.language_id = l.language_id
  WHERE f.language_id IS NULL OR l.language_id IS NULL
  """)
  films = db_cursor.fetchall()
  assert len(films) == 0, \
  f"Se encontraron películas con lenguaje principal nulo o inválido: {films}"

@pytest.mark.ir
def test_lenguaje_original_existe(db_cursor):
  db_cursor.execute("""
  SELECT f.film_id
  FROM film f
  LEFT JOIN language l ON f.original_language_id = l.language_id
  WHERE l.language_id IS NULL AND f.original_language_id IS NOT NULL
  """)
  films = db_cursor.fetchall()
  assert len(films) == 0, \
  f"Se encontraron películas con lenguaje original no válido: {films}"

@pytest.mark.id
def test_sin_precio_alquiler(db_cursor):
  db_cursor.execute("""
  SELECT film_id
  FROM film
  WHERE rental_rate IS NULL
  """)
  films = db_cursor.fetchall()
  assert len(films) == 0, \
  f"Se encontraron películas sin precio de alquiler: {films}"

@pytest.mark.ie
def test_mismo_titulo_anio_duracion(db_cursor):
  db_cursor.execute("""
  SELECT film_id, title, release_year, length, COUNT(*)
  FROM film
  GROUP BY title, release_year, length
  HAVING COUNT(*) > 1
  """)
  films = db_cursor.fetchall()
  assert len(films) == 0, \
  f"Se encontraron películas con título, año de lanzamiento y duración duplicados: {films}"