import requests  # Importa la biblioteca requests para realizar solicitudes HTTP

# URL base de la API
BASE_URL = "http://127.0.0.1:8000/api/"

def mostrar_menu():
    # Muestra el menú CRUD
    print("\n--- Menú CRUD ---")
    print("1. Crear Cliente")
    print("2. Listar Clientes")
    print("3. Actualizar Cliente")
    print("4. Eliminar Cliente")
    print("5. Salir")

def crear_cliente():
    # Función para crear un nuevo cliente
    print("\n--- Crear Cliente ---")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    telefono = input("Teléfono: ")

    # Datos del nuevo cliente
    data = {"nombre": nombre, "correo": correo, "telefono": telefono}
    # Realiza una solicitud POST para crear el cliente
    response = requests.post(BASE_URL + "clientes/", json=data)

    # Verifica si la creación fue exitosa
    if response.status_code == 201:
        print("Cliente creado con éxito.")
    else:
        print("Error al crear cliente:", response.json())

def listar_clientes():
    # Función para listar todos los clientes
    print("\n--- Lista de Clientes ---")
    # Realiza una solicitud GET para obtener la lista de clientes
    response = requests.get(BASE_URL + "clientes/")
    
    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        clientes = response.json()
        # Imprime la información de cada cliente
        for cliente in clientes:
            print(f"ID: {cliente['id']} | Nombre: {cliente['nombre']} | Correo: {cliente['correo']} | Teléfono: {cliente['telefono']}")
    else:
        print("Error al listar clientes:", response.json())

def actualizar_cliente():
    # Función para actualizar la información de un cliente
    print("\n--- Actualizar Cliente ---")
    cliente_id = input("ID del cliente a actualizar: ")
    nombre = input("Nuevo Nombre: ")
    correo = input("Nuevo Correo: ")
    telefono = input("Nuevo Teléfono: ")

    # Datos actualizados del cliente
    data = {"nombre": nombre, "correo": correo, "telefono": telefono}
    # Realiza una solicitud PUT para actualizar el cliente
    response = requests.put(BASE_URL + f"clientes/{cliente_id}/", json=data)

    # Verifica si la actualización fue exitosa
    if response.status_code == 200:
        print("Cliente actualizado con éxito.")
    else:
        print("Error al actualizar cliente:", response.json())

def eliminar_cliente():
    # Función para eliminar un cliente
    print("\n--- Eliminar Cliente ---")
    cliente_id = input("ID del cliente a eliminar: ")
    # Realiza una solicitud DELETE para eliminar el cliente
    response = requests.delete(BASE_URL + f"clientes/{cliente_id}/")

    # Verifica si la eliminación fue exitosa
    if response.status_code == 204:
        print("Cliente eliminado con éxito.")
    else:
        print("Error al eliminar cliente:", response.json())

def main():
    # Función principal que muestra el menú y maneja las opciones del usuario
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            actualizar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()  # Ejecuta la función principal
