### ¿Qué son las API?
Las API (Application Programming Interface) son contratos que permiten que un software se comunique con otro software. 

### ¿Qué es un endpoint?    
Un endpoint es un punto de acceso en una API que permite acceder a cierta funcionalidad.

### ¿Qué es un método HTTP?
Un método HTTP (HTTP Method) es un tipo de operación que se puede realizar sobre un endpoint.

### ¿Qué es un estado HTTP?
Un estado HTTP (HTTP Status) es un código que indica el resultado de una operación HTTP.

### ¿Qué es un header HTTP?
Un header HTTP (HTTP Header) es un par clave-valor que contiene información adicional sobre la operación HTTP.

### ¿Qué es un body HTTP?
Un body HTTP (HTTP Body) es un par clave-valor que contiene información adicional sobre la operación HTTP.

### ¿Qué es un par clave-valor?
Un par clave-valor (Key-Value Pair) es un tipo de dato que consta de una clave y un valor.

### ¿Qué es un JSON?
JSON (JavaScript Object Notation) es un formato de datos que se utiliza para transmitir datos entre sistemas.

### Tipos de API
- API REST
- API GraphQL
- API SOAP


### ¿Qué es un API GraphQL?
Una API GraphQL es un tipo de interfaz para consultar y manipular datos desarrollada por Facebook en 2012 y liberada como open source en 2015. A diferencia de una API REST, donde cada endpoint devuelve un conjunto fijo de datos, en GraphQL el cliente puede especificar exactamente qué datos necesita y en qué estructura.

Principales características de una API GraphQL:

Permite al cliente definir la estructura de la respuesta, solicitando solo los campos necesarios.
Utiliza un único endpoint para todas las operaciones (normalmente /graphql).
Soporta operaciones de consulta (query), modificación (mutation) y suscripción a eventos en tiempo real (subscription).
Reduce el overfetching (recibir más datos de los necesarios) y el underfetching (recibir menos datos de los necesarios).
Tiene un sistema de tipado fuerte y autodescriptivo: el esquema define los tipos de datos y operaciones disponibles, lo que facilita la validación y la documentación automática.
En resumen, una API GraphQL ofrece mayor flexibilidad y eficiencia en la obtención y manipulación de datos, permitiendo a los clientes pedir exactamente lo que necesitan en una sola petición.

### ¿Qué es un API SOAP?
Una API SOAP (Simple Object Access Protocol) es un protocolo estándar para el intercambio de información estructurada entre sistemas a través de redes, especialmente usando HTTP y XML. Fue uno de los primeros métodos ampliamente adoptados para la comunicación entre aplicaciones distribuidas.

Principales características de una API SOAP:

Utiliza XML para definir el formato de los mensajes, tanto en la solicitud como en la respuesta.
Opera principalmente sobre HTTP, pero también puede funcionar sobre otros protocolos como SMTP.
Es estricto en cuanto a la estructura de los mensajes y requiere un contrato formal (WSDL - Web Services Description Language) que describe las operaciones disponibles y los tipos de datos.
Soporta extensiones como seguridad, transacciones y mensajería confiable, lo que lo hace adecuado para entornos empresariales.
Es independiente del lenguaje de programación y la plataforma.
En resumen, una API SOAP es un protocolo robusto y formal para la comunicación entre sistemas, ideal para aplicaciones empresariales que requieren seguridad, transacciones y una estructura bien definida, aunque suele ser más complejo y pesado que alternativas modernas como REST o GraphQL.

### ¿Qué es un API REST?
Una API REST (Representational State Transfer) es un estilo de arquitectura para diseñar servicios web que permiten la comunicación entre sistemas a través de HTTP. Las principales características de una API REST son:

Utiliza los métodos HTTP estándar: GET (obtener datos), POST (crear), PUT/PATCH (actualizar), DELETE (eliminar).
Los recursos (datos o servicios) se representan mediante URLs (por ejemplo, /usuarios/123).
Es stateless: cada petición contiene toda la información necesaria, el servidor no guarda estado entre peticiones.
Utiliza formatos estándar para el intercambio de datos, como JSON o XML (actualmente, JSON es el más común).
Permite operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los recursos.
En resumen, una API REST es una interfaz que permite que diferentes aplicaciones se comuniquen entre sí a través de la web, usando reglas y convenciones muy claras y sencillas.

Métodos HTTP
GET: Obtiene datos de un recurso.
POST: Crea un nuevo recurso.
PUT/PATCH: Actualiza un recurso existente.
DELETE: Elimina un recurso.

Errores HTTP
200: OK
400: Bad Request
401: Unauthorized
403: Forbidden
404: Not Found
500: Internal Server Error

### FASTAPI
FastAPI es un framework para construir APIs con Python 3.7+ basado en ASGI. 

Instalar fastapi:
```bash
pip install fastapi
```

Instalar uvicorn:
```bash
pip install uvicorn
```

Ejecutar el servidor:
```bash
uvicorn Ejercicio1:app --reload
```

Acceder a la API documentation, con swagger:
```bash
localhost:8000/docs
```

Acceder a la API documentation, con redoc:
```bash
localhost:8000/redoc
```

