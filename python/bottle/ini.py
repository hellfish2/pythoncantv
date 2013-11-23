from bottle import route, run, template
import requests
#from funciones_consulta import consultar_cne

def consultar_cne(cedula_a_consultar):
    r = requests.get('http://www.cne.gov.ve/web/registro_electoral/ce.php?nacionalidad=V&cedula='+cedula_a_consultar)
    return r.text

@route('/consultar.py/<cedula>.html')
def consultar_cedula(cedula="0001",nombre="fulanito"):
    return template("respuesta.tpl",cedula_template=cedula,respuesta_consultar_cne=consultar_cne(cedula)) 

run(host='localhost', port=8088)
