import web
import sqlite3

render = web.template.render('views', base='layout')

class InsertarContacto:
    # 1. Muestra el formulario vacío para escribir el nuevo contacto
    def GET(self):
        return render.insertar_contacto()

    # 2. Recibe los datos del formulario y los guarda en la base de datos
    def POST(self):
        try:
            # Lee los datos que el usuario escribió en las cajas de texto del HTML
            formulario = web.input()
            
            # Conecta a la base de datos
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            
            # Consulta SQL para insertar (el id_contacto no se pone si es autoincrementable)
            query = """
                INSERT INTO contactos (nombre, primer_apellido, segundo_apellido, email, telefono)
                VALUES (?, ?, ?, ?, ?)
            """
            
            # Ejecuta la inserción con los datos del formulario
            cursor.execute(query, (
                formulario['nombre'], 
                formulario['primer_apellido'], 
                formulario['segundo_apellido'], 
                formulario['email'], 
                formulario['telefono']
            ))
            
            # Guarda los cambios permanentemente en el archivo .db
            conn.commit()
            conn.close()
            
            # Si todo sale bien, te regresa automáticamente a la lista de contactos
            return "Contacto guardado"
            
        except sqlite3.Error as error:
            print(f"ERROR al insertar: {error.args}")
            return "Error al guardar el contacto"