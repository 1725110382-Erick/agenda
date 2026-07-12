import web
import sqlite3

render = web.template.render('views', base='layout')

class BorrarCliente:

    def buscarCliente(self, id_cliente:int):
        try:
            # Conecta a la base de datos
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            # Consulta los registros de la tabla contactos
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_cliente,))
            # Almacena cada registro en un diccionario
            row = cursor.fetchone()
            cliente = {
                'id_cliente': row[0],
                'nombre': row[1],
                'primer_apellido': row[2],
                'segundo_apellido': row[3],
                'email': row[4],
                'telefono': row[5]
            }
            # Cierra la conexión a la base de datos
            conn.close()
            return cliente
        except sqlite3.Error as error:
            print(f"ERROR verClientes 100: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR verClientes 101: {error.args}")
            return {}
        finally:
            conn.close()

    def GET(self,id_cliente):
        print(f"ID_CLIENTE: {id_cliente}")
        cliente =  self.buscarCliente(id_cliente)
        print(cliente)

        return render.borrar_cliente(cliente)

    # --- LO QUE ME PEDISTE AGREGAR ---
    def POST(self, id_cliente):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = "DELETE FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_cliente,))
            conn.commit()
            
            # Si el contador de filas afectadas es mayor a 0, significa que sí lo borró
            exito = cursor.rowcount > 0
            conn.close()
            
            return True if exito else False
        except:
            return False