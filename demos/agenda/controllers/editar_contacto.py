import web
import sqlite3

render = web.template.render('views', base='layout')

class EditarContacto:
    # 1. Obtener los datos actuales del contacto para rellenar el formulario
    def GET(self, id_contacto):
        conn = sqlite3.connect('sql/agenda.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contactos WHERE id_contacto = ?", (id_contacto,))
        row = cursor.fetchone()
        conn.close()
        
        if not row: 
            return "Contacto no encontrado"
            
        # Creamos el diccionario compacto mapeando los datos de la fila
        contacto = web.storage({
            'id_contacto': row[0], 'nombre': row[1], 'primer_apellido': row[2],
            'segundo_apellido': row[3], 'email': row[4], 'telefono': row[5]
        })
        return render.editar_contacto(contacto)

    # 2. Procesar los datos enviados por el usuario y guardarlos en la BD
    def POST(self, id_contacto):
        form = web.input() # Captura todas las cajas de texto del HTML
        
        conn = sqlite3.connect('sql/agenda.db')
        cursor = conn.cursor()
        query = """
            UPDATE contactos 
            SET nombre = ?, primer_apellido = ?, segundo_apellido = ?, email = ?, telefono = ?
            WHERE id_contacto = ?
        """
        cursor.execute(query, (form.nombre, form.primer_apellido, form.segundo_apellido, 
                               form.email, form.telefono, id_contacto))
        conn.commit()
        conn.close()
        
        # Redirección inmediata a la lista principal
        raise web.seeother('/lista_contactos')