import web
import sqlite3

render = web.template.render('views', base='layout')

class VerContacto:

    def GET(self, id_contacto):
        print(f"ID_contacto: {id_contacto}")

        return render.ver_contacto()