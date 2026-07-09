import web
import sqlite3

render = web.template.render('views', base='layout')

class BorrarContacto:

    def buscarContacto(self, id_contacto:int):
        try:
            # Conecta a la base de datos
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            # Consulta los registros de la tabla contactos
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            # Almacena cada registro en un diccionario
            row = cursor.fetchone()
            contacto = {
                'id_contacto': row[0],
                'nombre': row[1],
                'primer_apellido': row[2],
                'segundo_apellido': row[3],
                'email': row[4],
                'telefono': row[5]
            }
            # Cierra la conexión a la base de datos
            conn.close()
            return contacto
        except sqlite3.Error as error:
            print(f"ERROR verContactos 100: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR verContactos 101: {error.args}")
            return {}
        finally:
            conn.close()

    def GET(self,id_contacto):
        print(f"ID_CONTACTO: {id_contacto}")
        contacto =  self.buscarContacto(id_contacto)
        print(contacto)

        return render.borrar_contacto(contacto)

    # --- LO QUE ME PEDISTE AGREGAR ---
    def POST(self, id_contacto):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = "DELETE FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            conn.commit()
            
            # Si el contador de filas afectadas es mayor a 0, significa que sí lo borró
            exito = cursor.rowcount > 0
            conn.close()
            
            return True if exito else False
        except:
            return False