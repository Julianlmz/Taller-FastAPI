# API Nutribox 🍎

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
├── main.py              # Punto de entrada de la aplicación
├── Database.py          # Configuración de base de datos y sesiones
├── Models.py            # Modelos de datos SQLModel
├── Usuario.py           # Endpoints de usuarios
├── Loncheras.py         # Endpoints de loncheras
├── Alimentos.py         # Endpoints de alimentos
├── Pedidos.py           # Endpoints de pedidos
├── requirements.txt     # Dependencias del proyecto
└── pets.sqlite3         # Base de datos SQLite (generada automáticamente)
```

## Instalación

1. **Clonar el repositorio:**
```bash
git clone <url-del-repositorio>
cd "Taller FastAPI"
```

2. **Crear entorno virtual:**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
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

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/usuarios/` | Crear nuevo usuario |
| GET | `/usuarios/` | Listar todos los usuarios |
| GET | `/usuarios/{user_id}` | Obtener usuario por ID |
| PATCH | `/usuarios/{user_id}` | Actualizar usuario |
| DELETE | `/usuarios/{user_id}` | Eliminar usuario |

### Loncheras (`/loncheras`)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/loncheras/` | Crear nueva lonchera |
| GET | `/loncheras/` | Listar todas las loncheras |
| GET | `/loncheras/{lonchera_id}` | Obtener lonchera por ID |
| PATCH | `/loncheras/{lonchera_id}` | Actualizar lonchera |
| DELETE | `/loncheras/{lonchera_id}` | Eliminar lonchera |

### Alimentos (`/alimentos`)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/alimentos/` | Crear nuevo alimento |
| GET | `/alimentos/` | Listar todos los alimentos |
| GET | `/alimentos/{alimento_id}` | Obtener alimento por ID |
| PATCH | `/alimentos/{alimento_id}` | Actualizar alimento |
| DELETE | `/alimentos/{alimento_id}` | Eliminar alimento |

### Pedidos (`/pedidos`)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/pedidos/` | Crear nuevo pedido |
| GET | `/pedidos/` | Listar todos los pedidos |
| GET | `/pedidos/{pedido_id}` | Obtener pedido por ID (incluye alimentos) |
| PATCH | `/pedidos/{pedido_id}` | Actualizar pedido |
| DELETE | `/pedidos/{pedido_id}` | Eliminar pedido |

## Modelos de Datos

### Usuario
```json
{
  "email": "usuario@ejemplo.com",
  "nombre": "Juan Pérez",
  "edad": 25
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
  "cliente_id": 1,
  "alimentos_ids": [1, 2, 3]
}
```

## Relaciones entre Modelos

- Un **Usuario** puede tener múltiples **Loncheras** y **Pedidos**
- Una **Lonchera** pertenece a un **Usuario** (propietario)
- Un **Pedido** pertenece a un **Usuario** (cliente) y puede contener múltiples **Alimentos**
- Un **Alimento** puede estar en múltiples **Pedidos** (relación many-to-many)

## Características

✅ CRUD completo para todos los recursos  
✅ Validación automática de datos con Pydantic  
✅ Documentación interactiva automática (Swagger/OpenAPI)  
✅ Manejo de relaciones entre entidades  
✅ Relación many-to-many entre Pedidos y Alimentos  
✅ Validación de claves foráneas  
✅ Mensajes de error descriptivos  
✅ Base de datos SQLite persistente  

## Documentación Interactiva

Una vez iniciado el servidor, puedes acceder a:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Ejemplo de Uso

### 1. Crear un usuario
```bash
curl -X POST "http://localhost:8000/usuarios/" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "juan@ejemplo.com",
    "nombre": "Juan Pérez",
    "edad": 25
  }'
```

### 2. Crear un alimento
```bash
curl -X POST "http://localhost:8000/alimentos/" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Manzana",
    "calorias": 52.0,
    "descripcion": "Fruta rica en fibra"
  }'
```

### 3. Crear un pedido con alimentos
```bash
curl -X POST "http://localhost:8000/pedidos/" \
  -H "Content-Type: application/json" \
  -d '{
    "fecha": "2024-11-05",
    "estado": "pendiente",
    "cliente_id": 1,
    "alimentos_ids": [1, 2]
  }'
```

## Comandos Útiles

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
uvicorn main:app --reload

# Ejecutar en un puerto específico
uvicorn main:app --reload --port 8080

# Ver ayuda de uvicorn
uvicorn --help
```

## Notas de Desarrollo

- La base de datos SQLite se crea automáticamente al iniciar la aplicación
- Las tablas se generan automáticamente basadas en los modelos de SQLModel
- Los cambios en el código se recargan automáticamente con `--reload`
- El campo `edad` es obligatorio para crear usuarios

## Autor

Proyecto desarrollado como taller de FastAPI.

## Licencia

Este proyecto es de código abierto y está disponible para fines educativos.