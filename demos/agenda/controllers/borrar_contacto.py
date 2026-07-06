import web
import sqlite3

render = web.template.render('views', base='layout')

class BorrarContacto:
    # 1. Muestra la pantalla de confirmación con el nombre del contacto
    def GET(self, id_contacto):
        conn = sqlite3.connect('sql/agenda.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id_contacto, nombre, primer_apellido FROM contactos WHERE id_contacto = ?", (id_contacto,))
        row = cursor.fetchone()
        conn.close()
        
        if not row:
            return "Contacto no encontrado"
            
        contacto = web.storage({'id_contacto': row[0], 'nombre': row[1], 'primer_apellido': row[2]})
        return render.borrar_contacto(contacto)

    # 2. Elimina físicamente el registro al presionar el botón
    def POST(self, id_contacto):
        conn = sqlite3.connect('sql/agenda.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contactos WHERE id_contacto = ?", (id_contacto,))
        conn.commit()
        conn.close()
        
        # Redirecciona automáticamente a la lista de contactos
        raise web.seeother('/lista_contactos')