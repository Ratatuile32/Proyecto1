from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

conexion = MySQL(app)

def pagina_no_encontrada(error):
    return "<h1>ERROR 404</h1>  <h2>La página que intenta buscar no existe</h2>",404

@app.route('/empleados', methods=['GET'])
def listar_empleados():
    try:
        cursor=conexion.connection.cursor()
        sql = "SELECT Nombres, Apellidos, Codigo, Puesto FROM empleados"
        cursor.execute(sql)
        data = cursor.fetchall()
        empleados = []
        for fila in data:
            empleado={'Nombres':fila[0],'Apellidos':fila[1],'Codigo':fila[2],'Puesto':fila[3]}
            empleados.append(empleado)
        return jsonify({'empleados':empleados,'mensaje':'Empleados listados'})
        
    except Exception as ex:
        return jsonify({'mensaje':'Error'})
    
@app.route('/empleados', methods=['POST'])
def registrar_empleado():
    try: 
        n = "{0}".format(request.json['Nombres'])
        a = "{0}".format(request.json['Apellidos'])
        c = "{0}".format(request.json['Codigo'])
        p = "{0}".format(request.json['Puesto'])
        if n == "" or a == "" or c == "" or p == "":
            return jsonify({'mensaje':"Faltan Datos"}),400
        else:
            cursor=conexion.connection.cursor()
            sql = "SELECT Nombres, Apellidos, Codigo, Puesto FROM empleados WHERE codigo = '{0}'".format(request.json['Codigo'])
            cursor.execute(sql)
            if cursor.fetchone():
                return jsonify({'mensaje':'Codigo ya existente'}),409
            sql = "INSERT INTO empleados (Nombres, Apellidos, Codigo, Puesto) VALUES ('"+n+"','"+a+"',"+c+",'"+p+"')"
            cursor.execute(sql)
            conexion.connection.commit()
            return jsonify({'mensaje':'Empleado registrado'}),201
    except Exception as ex:
        return jsonify({'mensaje':'Error'}),500
    
@app.route('/empleados/<codigo>', methods=['GET'])
def leer_empleado(codigo):
    try:
        cursor=conexion.connection.cursor()
        sql = "SELECT Nombres, Apellidos, Codigo, Puesto FROM empleados WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data != None:
            empleado = {'Nombres':data[0],'Apellidos':data[1],'Codigo':data[2],'Puesto':data[3]}
            return jsonify({'empleado':empleado,'mensaje':'Empleado encontrado'}),200
        return jsonify({'mensaje':'Empleado no encontrado'}),404
    except Exception as ex:
        return jsonify({'mensaje':'Error interno'}),500
    
@app.route('/empleados/<codigo>', methods=['PUT'])
def actualizar_empleado(codigo):
    try: 
        cursor=conexion.connection.cursor()
        sql = "SELECT Nombres, Apellidos, Codigo, Puesto FROM empleados WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data != None:
            n = "{0}".format(request.json['Nombres'])
            a = "{0}".format(request.json['Apellidos'])           
            p = "{0}".format(request.json['Puesto'])
            if n == "" or a == "" or p == "":
                return jsonify({'mensaje':"Faltan Datos"}),400
            else:
                sql = "UPDATE empleados SET Nombres ='"+n+"',Apellidos='"+a+"', Puesto='"+p+"' WHERE Codigo = "+codigo
                cursor.execute(sql)
                conexion.connection.commit()
                return jsonify({'mensaje':'Datos del Empleado actualizados'}),200
        else:
            return jsonify({'mensaje':'El Empleado no existe'}),404
    except Exception as ex:
        return jsonify({'mensaje':'Error'}),500

@app.route('/empleados/<codigo>', methods=['DELETE'])
def eliminar_empleado(codigo):
    try:
        cursor=conexion.connection.cursor()
        sql = "SELECT Nombres, Apellidos, Codigo, Puesto FROM empleados WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data != None:
            sql = "DELETE FROM empleados WHERE codigo = '{0}'".format(codigo)
            cursor.execute(sql)
            conexion.connection.commit()
            return jsonify({'mensaje':'Empleado Eliminado'}),200
    except Exception as ex:
        return jsonify({'mensaje':'Empleado no encontrado'}),404


if __name__ == '__main__':
    app.config.from_object(config['develop'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()