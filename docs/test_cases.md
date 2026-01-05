# Casos de prueba

Antes de mostrar el conjunto de pruebas implementado en este proyecto, doy la definición de cada tipo de integridad de datos:

- Integridad de Entidad (IE): Garantiza que a cada dato almacenado en una tabla se le asigne una clave y un valor únicos, de modo que los registros no se dupliquen y los campos de una tabla no sean nulos.

- Integridad Referencial (IR): Es una serie de procesos que garantizan que los datos almacenados en las tablas se utilicen de manera uniforme, siguiendo reglas específicas para la modificación y eliminación de datos. La integridad referencial contribuye a la precisión de los datos.

- Integridad de Dominio (ID): La integridad de dominio mantiene la precisión de los datos dentro de un dominio mediante la aplicación de restricciones y medidas para controlar la cantidad de valores y los tipos de datos introducidos en las columnas de una tabla.

- Integridad definida por el usuario (IDU): Cuando los usuarios personalizan las reglas y restricciones creadas en torno a los datos para cumplir requisitos específicos, se denomina integridad definida por el usuario. Aplica medidas de validación y lógica empresarial personalizadas.

Fuente: [SentinelOne.com](https://www.sentinelone.com/es/cybersecurity-101/cybersecurity/what-is-data-integrity/).

## Casos relacionados a los clientes

### TC-01 - Cada cliente tiene un e-mail único (IE)

### TC-02 - Los clientes tienen asignada una tienda no nula (ID)

### TC-03 - Los clientes tienen asignada una tienda válida (IR)

### TC-04 - Los clientes tienen un estado válido (ID)

### TC-05 - Los clientes tienen una dirección registrada (ID)

### TC-06 - Los clientes inactivos no pueden tener alquileres activos (IDU)

### TC-07 - No se permite registrar clientes sin e-mail (ID)

## Casos relacionados a los films

### TC-08 - Los films tienen una duración de alquiler correcta (IDU)

### TC-09 - Los films tienen un precio de alquiler positivo (ID)

### TC-10 - Los films tienen un precio de reposición positivo (ID)

### TC-11 - El precio de alquiler debe ser menor al de reposición (IDU)

### TC-12 - Los films tienen una clasificación de edad correcta (IDU)

### TC-13 - Los films tienen un lenguaje principal que existe (IR)

### TC-14 - Los films tienen un lenguaje original que existe o bien es nulo (IR)

### TC-15 - No hay films sin precio de alquiler (ID)

### TC-16 - No hay dos films con el mismo título, año de estreno y duración (IE)

## Casos elacionados a los alquileres

### TC-17 - Las fechas de devolución deben ser mayores a las de alquiler (IDU)

### TC-18 - Los alquileres no tienen cliente nulo (ID)

### TC-19 - Los alquileres están asociados a un cliente existente (IR)

### TC-20 - Los alquileres tienen una tienda válida (IR)

### TC-21 - Los alquileres están asociados a un elemento del inventario existente (ID)

## Casos relacionados a los pagos

### TC-22 - Los pagos corresponden a clientes existentes (IR)

### TC-23 - Los pagos fueron realizados en tiendas válidas (IR)

### TC-24 - Todos los pagos tienen asociado un alquiler existente (IR)

### TC-25 - La fecha de pago no puede ser anterior a la fecha de alquiler (IDU)

### TC-26 - No hay pagos duplicados para el mismo alquiler (IE)

