import web

urls = (
    '/', 'index_contactos',
    '/lista_contactos', 'lista_contactos',
    '/ver_contacto', 'ver_contacto',
    '/insertar_contacto', 'insertar_contacto',
    '/editar_contacto', 'editar_contacto',
    '/borrar_contacto', 'borrar_contacto'
)

app = web.application(urls, globals())
render = web.template.render('views') 
class index_contactos:
    def GET(self):
        return render.index()

class lista_contactos:
    def GET(self):
        return render.lista_contactos()

class ver_contacto:
    def GET(self):
        return render.ver_contacto()


class insertar_contacto:
    def GET(self):
        return render.insertar_contacto()

class editar_contacto:
    def GET(self):
        return render.editar_contacto()


class borrar_contacto:
    def GET(self):
        return render.borrar_contacto()

if __name__ == "__main__":
    app.run()