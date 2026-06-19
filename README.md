# Chatbot para Gestión de Vacaciones

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue)
![BPMN](https://img.shields.io/badge/BPMN-2.0-green)
![CSV](https://img.shields.io/badge/Persistencia-CSV-orange)
![GitHub](https://img.shields.io/badge/GitHub-Repositorio-black)

</p>

---

# Descripción

Este proyecto fue desarrollado como **Trabajo Práctico Integrador** de la materia **Organización Empresarial** de la **Tecnicatura Universitaria en Programación (TUP)**.

El objetivo es automatizar el proceso administrativo de **solicitud de vacaciones** mediante un chatbot, modelando previamente el proceso utilizando la metodología **BPMN 2.0**.

La solución implementada simula la interacción entre un empleado y un asistente virtual de Recursos Humanos, permitiendo consultar y solicitar días de vacaciones de manera automática.

---

# Integrantes

- **Fabian Tovar**
- **Darwing Lohn**

---

# Empresa Simulada

**TechSolutions SRL**

| Área | Proceso Automatizado |
|------|----------------------|
| Recursos Humanos | Gestión de Vacaciones |

---

# Tecnologías Utilizadas

| Herramienta | Uso |
|------------|-----|
| Python 3 | Desarrollo del chatbot |
| csv | Persistencia de datos |
| BPMN 2.0 | Modelado de procesos |
| GitHub | Control de versiones |
| ChatGPT y Gemini | Asistencia en diseño y documentación |

---

# Estructura del Proyecto

```text
TPI_OE/

├── main.py
├── usuarios.csv
├── README.md

├── bpmn/
│   ├── as_is.png
│   └── to_be.png

├── capturas_ia/
│   ├── consulta_chatgpt.png
│   └── consulta_gemini.png
```

---

# Base de Datos Simulada

El sistema utiliza un archivo denominado **usuarios.csv** para almacenar información de los empleados.

### Ejemplo

```csv
legajo,nombre,dias
1042,Juan Perez,15
1043,Ana Gomez,8
1044,Pedro Rodriguez,20
1045,Lucas Martinez,10
```

---

# Funcionalidades

El chatbot permite:

 Validar la existencia del empleado mediante número de legajo.

 Consultar el saldo disponible de vacaciones.

 Solicitar una cantidad determinada de días.

 Aprobar o rechazar solicitudes según reglas de negocio.

 Mantener el estado de la conversación mediante una máquina de estados.

 Detectar errores de entrada del usuario.

---

# Ejecución del Programa

Abrir una terminal dentro de la carpeta del proyecto y ejecutar:

```bash
python main.py
```

---

# Máquina de Estados

Estados implementados:

| Estado | Descripción |
|--------|-------------|
| INICIO | Espera que el usuario solicite vacaciones |
| ESPERANDO_DIAS | Solicita la cantidad de días deseados |

Estos estados permiten que el chatbot recuerde en qué etapa del proceso se encuentra cada usuario.

---

# Caminos de Excepción

El sistema contempla diferentes escenarios de error:

- Legajo inexistente.
- Ingreso de texto en lugar de números.
- Solicitud de una cantidad mayor a los días disponibles.
- Solicitud de cero o menos días.

---

# Diagramas BPMN

Se incluyen dos modelos BPMN desarrollados para representar el proceso administrativo.

### AS-IS
Representa el procedimiento manual realizado por Recursos Humanos.

### TO-BE
Representa el proceso automatizado mediante chatbot.

---

# Herramientas de Inteligencia Artificial Utilizadas

Se utilizaron herramientas de IA como apoyo para:

- Diseño de diagramas BPMN.
- Revisión de la lógica de programación.
- Elaboración de documentación técnica.
- Validación de escenarios de prueba.

Se adjuntan capturas de las consultas realizadas como evidencia del proceso de desarrollo.

---

# Asignatura

**Organización Empresarial**

**Tecnicatura Universitaria en Programación**

**Universidad Tecnológica Nacional**