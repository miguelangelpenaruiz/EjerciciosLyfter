# Herencia múltiple en la vida real

En código real, la herencia múltiple casi siempre aparece en forma de **mixins**: una clase padre principal, que define qué **es** el objeto, más uno o varios mixins, que le agregan cosas que **puede hacer**. Un mixin aporta una sola capacidad, no tiene `__init__` y va a la izquierda en la lista de padres para que sus métodos se encuentren primero en el MRO.

Estos son los usos más comunes en proyectos reales.

## 1. Inicio de sesión de usuarios (Flask-Login)

**El problema:** toda aplicación web con cuentas necesita que el usuario responda preguntas como "¿inició sesión?", "¿su cuenta está activa?" o "¿cuál es su identificador?". Pero la clase `User` ya es una tabla de la base de datos.

**La solución:**

```python
class User(UserMixin, db.Model):
    ...
```

`User` **es** una tabla (`db.Model`) y **puede** manejar sesiones gracias a `UserMixin`, que ya trae `is_authenticated`, `is_active`, `is_anonymous` y `get_id()`.

**Sin herencia múltiple:** habría que escribir esos cuatro métodos a mano en cada proyecto.

## 2. Columnas que se repiten en todas las tablas (SQLAlchemy)

**El problema:** en un sistema de ventas, casi todas las tablas (pedidos, clientes, productos) necesitan saber cuándo se creó y cuándo se modificó cada registro, para auditoría.

**La solución**, tomada de la documentación de SQLAlchemy 2.0:

```python
class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime]


class MyModel(TimestampMixin, Base):
    __tablename__ = "test"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
```

Toda tabla que herede de `TimestampMixin` recibe las columnas `created_at` y `updated_at`.

**Sin herencia múltiple:** copiar las mismas columnas en cada modelo, y cambiarlas en todos si la regla cambia.

## 3. Páginas que requieren permisos (Django)

**El problema:** muchas páginas solo deben verlas usuarios con sesión iniciada: "mis pedidos", "mi perfil", un panel de administración.

**La solución:**

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

class OrderListView(LoginRequiredMixin, ListView):
    ...
```

`ListView` muestra la lista de pedidos y `LoginRequiredMixin` revisa la sesión **antes** de mostrar la página. Por eso la documentación de Django indica que este mixin debe ir en la posición **más a la izquierda**: tiene que ejecutarse primero.

**Sin herencia múltiple:** repetir la revisión en cada página. Basta con olvidarla en una para tener un hueco de seguridad.

## 4. APIs armadas por piezas (Django REST Framework)

**El problema:** una API ofrece operaciones sobre sus datos (listar, crear, consultar, actualizar y borrar), pero no todos los recursos necesitan todas. Un catálogo público solo se consulta; los pedidos sí se crean y se editan.

**La solución:** cada operación es un mixin, y cada vista combina solo las que necesita:

| Mixin | Operación |
|---|---|
| `ListModelMixin` | Listar registros |
| `CreateModelMixin` | Crear un registro |
| `RetrieveModelMixin` | Consultar un registro |
| `UpdateModelMixin` | Actualizar un registro |
| `DestroyModelMixin` | Borrar un registro |

Según su documentación, cada vista concreta se construye combinando `GenericAPIView` con uno o más de estos mixins. Por ejemplo, `ListCreateAPIView` combina `GenericAPIView`, `ListModelMixin` y `CreateModelMixin`: lista y crea, pero no borra.

**Sin herencia múltiple:** programar cada operación de nuevo para cada recurso. Este es el caso que más usa herencia múltiple: todo el framework está armado así.

## 5. Servidores que atienden a varios clientes a la vez (librería estándar)

**El problema:** un servidor básico atiende a un cliente a la vez; mientras tanto, los demás esperan.

**La solución**, en el módulo `socketserver` de Python:

```python
class ThreadingUDPServer(ThreadingMixIn, UDPServer):
    pass
```

`ThreadingMixIn` cambia la forma en que el servidor procesa las peticiones para que cada cliente se atienda por separado. La documentación explica que el mixin va primero porque **sobrescribe** un método de `UDPServer`.

**Sin herencia múltiple:** modificar la clase del servidor o duplicarla para cada tipo de servidor.

## 6. Opciones fijas que también son texto (`Enum` + `str`)

**El problema:** el estado de un pedido solo puede ser "pending" o "shipped". Un `Enum` evita errores de dedo, pero sus valores no se comportan como texto:

```python
class OrderStatus(Enum):
    PENDING = "pending"

OrderStatus.PENDING == "pending"            # False
json.dumps({"status": OrderStatus.PENDING})
# TypeError: Object of type OrderStatus is not JSON serializable
```

**La solución:** que la clase sea las dos cosas, opción fija **y** texto:

```python
class OrderStatus(str, Enum):
    PENDING = "pending"
    SHIPPED = "shipped"

OrderStatus.PENDING == "pending"            # True
json.dumps({"status": OrderStatus.PENDING})  # '{"status": "pending"}'
```

Es tan común que desde Python 3.11 existe `StrEnum`, que la documentación describe como "igual que `Enum`, pero sus miembros también son strings". También existe `IntEnum` para números.

## Conclusión

- **El patrón dominante es padre principal + mixins** (casos 1 a 5): capacidades pequeñas y reutilizables que se suman a una clase.
- **El orden importa:** los mixins van a la izquierda porque deben encontrarse primero en el MRO, como piden Django y `socketserver`.
- **Los casos de "es dos cosas a la vez" existen, pero son raros** (caso 6).

## Relación con el ejercicio

Encontré que la mayoría de estos usos aparecen en temas más avanzados, como frameworks web, bases de datos y redes. Para el ejemplo busqué algo que sí pudiera aplicar bien con lo que he visto: un juego de adivinar palabras donde `GameBase` es el padre principal y `BackwardsMixin` y `HideLettersMixin` son capacidades que se combinan en `GameModeHard`, siguiendo el mismo patrón de padre principal + mixins.

## Fuentes

- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
- [SQLAlchemy 2.0: Composing Mapped Hierarchies with Mixins](https://docs.sqlalchemy.org/en/20/orm/declarative_mixins.html)
- [Django: commit que agregó LoginRequiredMixin, PermissionRequiredMixin y UserPassesTestMixin](https://github.com/django/django/commit/e5cb4e14118f3a508e3bc00ee7cd50bb0f18a61d)
- [Django REST Framework: Generic views](https://www.django-rest-framework.org/api-guide/generic-views)
- [socketserver (documentación de Python)](https://docs.python.org/3/library/socketserver.html)
- [enum (documentación de Python)](https://docs.python.org/3/library/enum.html)

*Investigación elaborada con apoyo de Claude (Anthropic).*
