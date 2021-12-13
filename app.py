from flask import Flask, render_template, Request, request,redirect, url_for, send_from_directory, flash
from os import remove
import math

import funciones 


#parte del archivo
import os
UPLOAD_FOLDER = os.path.abspath("uploads/")


app = Flask(__name__)
#donde se quiere que se suban los archivos
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/jair')
def jair():
    return '<h1>jair</h1>'


rutas = ['base.py']
i=0
filas = []
nombreMatriz = ''



@app.route("/similitud")
def Similitud():
    global filas 
    global rutas
    global nombreMatriz
    #filas = funciones.calcularMatrizSimlitud(rutas,'uploads/',3)
    fila1 = funciones.crearEncabezadoMatriz(filas)
    fila2 = fila1[1:]
     
    
    return render_template('similitud.html', matriz = filas, encabezado = fila1, nombre = nombreMatriz, nombresArchivos = rutas[1:], encabezado2 = fila2)

@app.route('/calcular', methods=['POST'])
def calcular():
    if request.method == 'POST':
        tipo = request.form['options']  
        tipo = int(tipo)
        

        global rutas
        global filas
        global nombreMatriz
        nombreMatriz = funciones.nombreMatriz(tipo)
        filas = funciones.calcularMatrizSimlitud(rutas,'uploads/',tipo)       
        return redirect(url_for('Similitud'))


#ruta para mostrar formulario de subir imagen
@app.route("/upload", methods=["GET","POST"])
def upload():
    if request.method == "POST":
        f = request.files["ourfile"] #ourfile es el name del formulario
        filename = f.filename #se escoge el nombre del archivo
        #print(filename)
        global rutas
        filename = funciones.agregarArchivoLista(rutas,filename)
        rutas.append(filename)
        print(rutas)
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename)) 
        #return "Your file has been uploaded " + filename
        flash('El código se subio correctamente')
        #return redirect(url_for("get_file", filename=filename))
    

    return render_template('formularioArchivo.html')


@app.route("/delete/<nombre_archivo>")
def delete(nombre_archivo):
  global rutas
  rutas.remove(nombre_archivo)
  remove("uploads/"+nombre_archivo)
  flash('Documento Eliminado')
  return redirect(url_for('eliminar'))




@app.route("/eliminar")
def eliminar():
  global rutas

  return render_template('eliminar.html', ubicaciones = rutas[1:])




#parte de subir codigo
@app.route("/uploadCodigo",methods=['GET','POST'])
def uploadCodigo():
    if request.method == "POST":
        textCodigo = request.form["codigo"]
        #print(textCodigo)
        mns = escribirArchivo(textCodigo)   
        flash(mns)      
        return render_template('formularioCodigo.html')
        
       
    return render_template('formularioCodigo.html')


#metodo para escribir archivo
def escribirArchivo(texto):      
    global rutas
    ruta = "uploads/"
    nombreA = 'archivo'+'.txt'
    nombreA = funciones.agregarArchivoLista(rutas,nombreA)
    nombreArchivo = ruta + nombreA     
    escritura = open(nombreArchivo,'w')
    escritura.write(texto)
    escritura.close()     
    rutas.append(nombreA)
    return "Archivo: "+str(nombreA)+" escrito"


if __name__ == '__main__':
    app.run(port = 5000, debug = True)