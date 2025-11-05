# API Nutribox

API REST para la gestión de usuarios, loncheras, alimentos y pedidos desarrollada con FastAPI y SQLModel.

## Descripción

Nutribox es una aplicación que permite a los usuarios gestionar loncheras saludables, realizar pedidos y administrar alimentos con información nutricional. La API proporciona endpoints para operaciones CRUD completas en todos los recursos principales.

## Tecnologías

- **FastAPI**: Framework web moderno y de alto rendimiento
- **SQLModel**: ORM basado en Pydantic y SQLAlchemy
- **SQLite**: Base de datos ligera para almacenamiento
- **Python 3.13**: Lenguaje de programación

## Estructura del Proyecto

```
.
├── main.py           # Punto de entrada de la aplicación
├── Database.py       # Configuración de base de datos y sesiones
├── Models.py         # Modelos de datos SQLModel
├── Usuario.py        # Endpoints de usuarios
├── Loncheras.py      # Endpoints de loncheras
├── Alimentos.py      # Endpoints de alimentos
├── Pedidos.py        # Endpoints de pedidos
└── pets.sqlite3      # Base de datos SQLite
```

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd "Taller FastAPI"
```

2. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install fastapi sqlmodel uvicorn
```

## Ejecución

Iniciar el servidor de desarrollo:

```bash
uvicorn main:app --reload
```

La API estará disponible en: `http://localhost:8000`

Documentación interactiva: `http://localhost:8000/docs`

## Endpoints de la API

### Usuarios (`/usuarios`)

- `POST /usuarios/` - Crear nuevo usuario
- `GET /usuarios/` - Listar todos los usuarios
- `GET /usuarios/{user_id}` - Obtener usuario por ID
- `PATCH /usuarios/{user_id}` - Actualizar usuario
- `DELETE /usuarios/{user_id}` - Eliminar usuario

### Loncheras (`/loncheras`)

- `POST /loncheras/` - Crear nueva lonchera
- `GET /loncheras/` - Listar todas las loncheras
- `GET /loncheras/{lonchera_id}` - Obtener lonchera por ID
- `PATCH /loncheras/{lonchera_id}` - Actualizar lonchera
- `DELETE /loncheras/{lonchera_id}` - Eliminar lonchera

### Alimentos (`/alimentos`)

- `POST /alimentos/` - Crear nuevo alimento
- `GET /alimentos/` - Listar todos los alimentos
- `GET /alimentos/{alimento_id}` - Obtener alimento por ID
- `PATCH /alimentos/{alimento_id}` - Actualizar alimento
- `DELETE /alimentos/{alimento_id}` - Eliminar alimento

### Pedidos (`/pedidos`)

- `POST /pedidos/` - Crear nuevo pedido
- `GET /pedidos/` - Listar todos los pedidos
- `GET /pedidos/{pedido_id}` - Obtener pedido por ID
- `PATCH /pedidos/{pedido_id}` - Actualizar pedido
- `DELETE /pedidos/{pedido_id}` - Eliminar pedido

## Modelos de Datos

### Usuario
```json
{
  "email": "usuario@ejemplo.com",
  "nombre": "Juan Pérez",
  "password": "contraseña123"
}
```

### Lonchera
```json
{
  "nombre": "Lonchera Saludable",
  "descripcion": "Lonchera balanceada para el día",
  "propietario_id": 1
}
```

### Alimento
```json
{
  "nombre": "Manzana",
  "calorias": 52.0,
  "descripcion": "Fruta rica en fibra"
}
```

### Pedido
```json
{
  "fecha": "2024-11-05",
  "estado": "pendiente",
  "cliente_id": 1
}
```

## Relaciones entre Modelos

- Un **Usuario** puede tener múltiples **Loncheras** y **Pedidos**
- Una **Lonchera** pertenece a un **Usuario** (propietario)
- Un **Pedido** pertenece a un **Usuario** (cliente) y puede contener múltiples **Alimentos**

## Características

- ✅ CRUD completo para todos los recursos
- ✅ Validación automática de datos con Pydantic
- ✅ Documentación interactiva automática (Swagger/OpenAPI)
- ✅ Manejo de relaciones entre entidades
- ✅ Validación de claves foráneas
- ✅ Mensajes de error descriptivos
- ✅ Base de datos SQLite persistente

## Documentación Interactiva

Una vez iniciado el servidor, puedes acceder a:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Notas de Seguridad

⚠️ **Importante**: Este proyecto es para propósitos educativos. En producción deberías:

- Implementar un sistema de hash de contraseñas robusto (bcrypt, argon2)
- Agregar autenticación y autorización (JWT, OAuth2)
- Validar y sanitizar todos los inputs
- Usar variables de entorno para configuraciones sensibles
- Implementar rate limiting
- Usar HTTPS en producción

## Autor

Julian Leal - 67001277

## Licencia

Este proyecto es de código abierto y está disponible para fines educativos.
