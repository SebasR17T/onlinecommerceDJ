# OnlineCommerceDJ

Pequeño proyecto Django para comercio en línea, con una app `onlinecommerceApp` que maneja productos, tiendas, carrito y reseñas.

## Requisitos

- Python 3.10+
- Dependencias en `requirements.txt`

## Instalación rápida

1. Crear y activar un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Migrar la base de datos y crear superusuario:

```bash
python project\manage.py migrate
python project\manage.py createsuperuser
```

4. Ejecutar servidor de desarrollo:

```bash
python project\manage.py runserver
```

## Estructura relevante

- `project/` — configuración del proyecto y `manage.py`.
- `project/onlinecommerceApp/` — app principal (modelos, vistas, templates, static).
- `project/db.sqlite3` — base de datos SQLite (dev).
- `requirements.txt` — dependencias del proyecto.

## Notas

- Los archivos estáticos y media están en `project/onlinecommerceApp/static` y `project/media`.
- Para producción, ajustar `project/settings.py` y configurar un servidor WSGI/ASGI y almacenamiento de media.

Si quieres, puedo ampliar este README con secciones sobre pruebas, despliegue, o ejemplos de uso.