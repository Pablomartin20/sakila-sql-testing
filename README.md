## 📌 Introducción

Este proyecto tiene como objetivo validar la integridad de los datos de la base de datos SQL 'Sakila', que modela una tienda de alquiler de DVDs. Esta validación se realiza mediante tests automatizados desarrollados en Python, con ayuda del framework pytest.

Los casos de prueba están enfocados en verificar reglas de:

- Integridad de entidad (IE)
- Integridad de dominio (ID)
- Integridad Referencial (IR)
- Integridad definida por el usuario o negocio (IDU)

Nótese que el conjunto de pruebas estará enfocado en validar la integridad lógica de la base de datos pero no tiene alcance sobre la integridad física.

Por otro lado, dichas validaciones se realizan directamente sobre la base de datos usando consultas SQL y se ejecutan automáticamente con pytest sobre una base SQLite, permitiendo detectar inconsistencias, duplicados y violaciones de reglas de negocio.

## 🤖 Integración Continua (CI)

El proyecto cuenta con integración continua (CI) implementada con GitHub Actions, lo que permite ejecutar el conjunto de tests completo ante:

- cada push
- cada pull request

## 📊 Casos de prueba

Los casos de prueba completos están documentados en [docs/test_cases.md](docs/test_cases.md).

## 🎯 Alcance de este test suite

Este conjunto de pruebas no pretende ser completo ni exhaustivo, sino representar un subconjunto de validaciones relevantes orientadas a demostrar criterios de calidad, integridad de datos, automatización y otros conocimientos adquiridos en la reciente Diplomatura en Control de Calidad de Software que cursé y completé en Diciembre de 2025 en la UNTREF.

## 🛠️ Tecnologías y herramientas utilizadas

- Visual Studio Code
- Python 3.13
- Pytest
- SQLite
- Git
- GitHub Issues
- GitHub Actions

## Instalación y ejecución local

Si preferís instalar el proyecto en local, seguí estas instrucciones:

1. Cloná el repo y abrilo:
   ```bash
   git clone https://github.com/Pablomartin20/sakila-sql-testing.git
   cd sakila-sql-testing
2. Instalá las dependencias:
   ```bash
   pip install -r requirements.txt
3. Ejecutá los tests:
   ```bash
   pytest