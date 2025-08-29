## SEMANA 1

# Mi Primera API FastAPI - Bootcamp

**👤 Desarrollador**: $(git config Luisa Fernanda Betancourt buitrago)
**📧 Email**: $(git config 200136741+Fernanda1111122@users.noreply.github.com
)
**� Privacidad**: 200136741+Fernanda1111122@users.noreply.github.com
**�📅 Fecha de creación**: $(date 14-08-2025)
**📂 Ruta del proyecto**: $(/c/Users/carol/desarrollo-personal/Fernanda_Betancourt-bootcamp/mi-primera-api-fastapi
)
**💻 Equipo de trabajo**: $(Carol_y_Fer)

## 🔧 Configuración Local

Este proyecto está configurado para trabajo en equipo compartido:

- **Entorno virtual aislado**: \`venv-personal/\`
- **Configuración Git local**: Solo para este proyecto
- **Dependencias independientes**: No afecta otras instalaciones

## 🚀 Instalación y Ejecución

\`\`\`bash
# 1. Activar entorno virtual personal
source venv-personal/bin/activate

# 2. Instalar dependencias (si es necesario)
pip install -r requirements.txt

# 3. Ejecutar servidor de desarrollo
uvicorn main:app --reload --port 8000
\`\`\`

## 📝 Notas del Desarrollador

- **Configuración Git**: Local únicamente, no afecta configuración global
- **Email de GitHub**: Configurado con email privado para proteger información personal
- **Entorno aislado**: Todas las dependencias en venv-personal/
- **Puerto por defecto**: 8000 (cambiar si hay conflictos)
- **Estado del bootcamp**: Semana 1 - Configuración inicial

## 🛠️ Troubleshooting Personal

- Si el entorno virtual no se activa: \`rm -rf venv-personal && python3 -m venv venv-personal\`
- Si hay conflictos de puerto: cambiar --port en uvicorn
- Si Git no funciona: verificar \`git config user.name\` y \`git config user.email\`
- Si necesitas cambiar el email: usar el email privado de GitHub desde Settings → Emails

# Mi Primera API FastAPI

## ¿Qué hace?

Una API básica creada en el Bootcamp FastAPI Semana 1.

## ¿Cómo ejecutar?

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## 3 cosas que aprendi 

1. Cree una API básica con FastAPI.
2. Configurar el entorno de desarrollo.
3. Utilice la herramienta uvicorn para ejecutar la aplicación.

## SEMANA 2

## ¿Los type hints hacen tu código más claro? ¿Por qué?

Los type hints hacen que el código sea más legible porque indican qué tipo de dato espera y devuelve cada función. Esto ayuda a entender mejor la lógica, y además facilita la detección de errores antes de ejecutar el programa.

## ¿Cómo te ayuda Pydantic a crear APIs más robustas?

Pydantic ayuda a validar automáticamente los datos que recibe la API, asegurando que cumplan con los tipos definidos, esto evita errores comunes, como recibir texto en lugar de un número, y genera mensajes claros cuando la información no es válida, gracias a esto, la API es más robusta, confiable y fácil de mantener.

## ¿Cómo mejoraron estos conceptos tu API comparada con la Semana 1?

Con los nuevos conceptos aprendidos, la API ahora valida automáticamente los datos con Pydantic, maneja mejor los parámetros de ruta y devuelve respuestas más claras. Esto la hace más segura, confiable y organizada en comparación con la de la Semana 1.

# Mi API FastAPI 

## ¿Qué hace?

API mejorada con validación automática de datos y type hints.

## Nuevos Features 

- ✅ Type hints en todas las funciones
- ✅ Validación automática con Pydantic
- ✅ Endpoint POST para crear datos
- ✅ Parámetros de ruta (ejemplo: /products/{id})
- ✅ Búsqueda con parámetros query

## Reflexión

Lo más útil de esta semana fue aprender a usar Pydantic para validar datos y asegurar que la API reciba información correcta. También entendí cómo manejar parámetros de ruta para crear endpoints más flexibles y organizados. Esto hace que mi API sea más confiable y profesional.

## SEMANA 3

# 📚 Library Management API

Una API RESTful para la gestión de libros y préstamos en una biblioteca.  
Incluye validaciones, manejo de errores, documentación automática y tests.

## ⚙️ Instalación

Endpoints
Libros

GET /api/v1/books/ → Listar libros

POST /api/v1/books/ → Crear libro

GET /api/v1/books/{id} → Obtener libro por ID

PUT /api/v1/books/{id} → Actualizar libro

DELETE /api/v1/books/{id} → Eliminar libro

GET /api/v1/books/search → Buscar libros

GET /api/v1/books/stats → Estadísticas

Préstamos

POST /api/v1/borrowing/borrow/{book_id} → Prestar libro

POST /api/v1/borrowing/return/{book_id} → Devolver libro

GET /api/v1/borrowing/active → Listar préstamos activos

Categorías

GET /api/v1/categories/ → Listar categorías

GET /api/v1/categories/{genre}/books → Libros por género

# 🗄️ Esquema de base de datos

id (int, PK)

title (str)

author (str)

rating (float, 0-5)

bestseller (bool)

tags (list[str])

year (int)

price (float)

is_available (bool)

Borrowings

id (int, PK)

book_id (FK → Books)

user_id (int)

borrowed_at (datetime)

returned_at (datetime, nullable)

Categories

genre (str, único)

books (relación con Books)

# 🧪 Ejemplos de uso
Crear un libro

curl -X POST "http://localhost:8000/api/v1/books/" \
-H "Content-Type: application/json" \
-d '{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "rating": 4.7,
  "bestseller": true,
  "tags": ["programming", "best practices"],
  "year": 2008,
  "price": 40.0,
  "is_available": true
}'

# 🚀 Inicio rápido

Una vez en ejecución, accede a:

📑 Swagger UI → http://localhost:8000/docs
