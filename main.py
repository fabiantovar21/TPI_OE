# PROCESO: GESTIÓN DE VACACIONES MEDIANTE CHATBOT
import csv
# 1. PERSISTENCIA: LECTURA DEL NUEVO ARCHIVO usuario.csv 
def buscar_empleado_en_csv(legajo_buscado):
    try:
        # Abrimos tu nuevo archivo 'usuario.csv'
        with open("usuarios.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for fila in reader:
                # Comparamos el legajo ingresado con la columna 'legajo' del CSV
                if fila['legajo'].strip() == str(legajo_buscado).strip():
                    return {
                        "legajo": fila['legajo'].strip(),
                        "nombre": fila['nombre'].strip(),
                        "dias_disponibles": int(fila['dias'].strip()),
                        "estado_conversacion": "INICIO"
                    }
    except FileNotFoundError:
        print("\n[ERROR DE SISTEMA] No se encontró el archivo 'usuarios.csv'.")
        print("Asegurate de que esté en la misma carpeta que este script de Python.")
        return None
    
    return None


# 2. ACTUALIZACIÓN DINÁMICA (SIMULACIÓN DE ESCRITURA)
# Modificamos los días del empleado en memoria para mostrar el impacto del proceso.
def actualizar_dias_en_memoria(empleado, dias_a_descontar):
    empleado["dias_disponibles"] -= dias_a_descontar


# 3. LÓGICA PRINCIPAL: MÁQUINA DE ESTADOS Y REGLAS DE NEGOCIO
def procesar_mensaje_bot(empleado, mensaje_usuario):
    estado_actual = empleado["estado_conversacion"]
    respuesta_bot = ""

    # ESTADO A: INICIO
    if estado_actual == "INICIO":
        # Validamos si el usuario tiene la intención de sacar vacaciones
        if "vacaciones" in mensaje_usuario.lower() or "solicitar" in mensaje_usuario.lower():
            # TRANSICIÓN DE ESTADO: Cambiamos el flujo (El bot adquiere memoria)
            empleado["estado_conversacion"] = "ESPERANDO_DIAS"
            respuesta_bot = (
                f"Hola {empleado['nombre']}. Detecté tu solicitud de vacaciones.\n"
                f"Actualmente disponés de {empleado['dias_disponibles']} días.\n"
                f"¿Cuántos días te gustaría tomarte?"
            )
        else:
            respuesta_bot = (
                f"Hola {empleado['nombre']}. Soy el asistente virtual de RRHH.\n"
                f"Para iniciar tu trámite, por favor escribí la palabra 'vacaciones'."
            )

    # ESTADO B: ESPERANDO_DIAS
    elif estado_actual == "ESPERANDO_DIAS":
        # Validamos que el usuario ingrese un número
        if not mensaje_usuario.isdigit():
            respuesta_bot = (
                " Error de formato: Por favor, ingresá la cantidad usando "
                "solamente números enteros."
            )
        else:
            dias_solicitados = int(mensaje_usuario)
            dias_disponibles = empleado["dias_disponibles"]

            # COMPUERTA LÓGICA (Gateway de Decisión en tu diagrama BPMN)
            if 0 < dias_solicitados <= dias_disponibles:
                # CAMINO FELIZ: Cumple las reglas de negocio
                actualizar_dias_en_memoria(empleado, dias_solicitados)
                
                # Volvemos el estado al inicio para cerrar el ciclo de este trámite
                empleado["estado_conversacion"] = "INICIO"
                
                respuesta_bot = (
                    f"¡Solicitud Aprobada Exitosamente!\n"
                    f"Se registraron tus {dias_solicitados} días de vacaciones.\n"
                    f"Tu nuevo saldo es de {empleado['dias_disponibles']} días. ¡Que disfrutes!"
                )
            elif dias_solicitados <= 0:
                respuesta_bot = "La cantidad de días debe ser mayor a 0. Intentá de nuevo:"
            else:
                # CAMINO DE EXCEPCIÓN: Supera el límite de días disponibles
                respuesta_bot = (
                    f"No es posible procesar la solicitud.\n"
                    f"Pediste {dias_solicitados} días, pero tu saldo actual es de {dias_disponibles} días.\n"
                    f"Por favor, ingresá una cantidad menor o igual a tu saldo:"
                )
                # Al no cambiar el estado, el ciclo se repite hasta que ponga un número válido

    return respuesta_bot


# --- 4. INTERFAZ DE SIMULACIÓN EN CONSOLA (DEMOSTRACIÓN EN VIVO) ---
if __name__ == "__main__":
    print("========SISTEMA DE AUTOMATIZACIÓN DE PROCESOS - RRHH (TUP)========")
    print("Cargando base de datos desde el archivo usuario.csv...")
    
    # Volvemos a pedir el número de legajo
    legajo_ingresado = input("Por favor, ingresá tu número de legajo para iniciar: ")
    empleado_activos = buscar_empleado_en_csv(legajo_ingresado)
    
    if empleado_activos is not None:
        print(f"\n[SISTEMA] Conexión establecida. Empleado: {empleado_activos['nombre']}")
        print(" -> Escribí 'salir' en cualquier momento para apagar el bot.\n")
        print(f"Chatbot: Hola. Soy el asistente virtual de RRHH. por favor escribí la palabra 'vacaciones' para iniciar tu trámite")
        
        while True:
            print("----------------------------------------------------------------------------")
            entrada = input(f"{empleado_activos['nombre']} (Tú): ")
            
            if entrada.lower() == "salir":
                print("\nCerrando sesión de manera segura. ¡Hasta luego!")
                break
                
            respuesta = procesar_mensaje_bot(empleado_activos, entrada)
            print(f"\nChatbot:\n{respuesta}")
    else:
        print("\n[PROCESO TERMINADO] No se encontró ningún empleado con ese legajo en la base de datos.")