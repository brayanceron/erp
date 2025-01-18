from src.database.database import  get_connection
from src.utils.messages_errors import DB_CONNECTION_ERROR, ERROR_500, ERROR_400
from uuid import uuid4

# CRUD

def get() :#{
    conn = get_connection()
    if (not conn): return DB_CONNECTION_ERROR
    
    try :#{
        cursor = conn.cursor()
        cursor.execute("select id, name, country, city, address, phone, description from sucursal")
        row_count = cursor.rowcount
        if (row_count == 0) :#{
            return {"message":"No hay sucursales registradas :("}, 404
        #}
        
        rows = cursor.fetchall()
        sucursales = []
        for row in rows :#{
            sucursales.append({
                "id":row[0],
                "name":row[1],
                "country":row[2],
                "city":row[3],
                "address":row[4],
                "phone":row[5],
                "description":row[6]
            })
        #}
        conn.close()
        return sucursales, 200
    #}
    # except :#{
    except Exception as err:#{
        # print(err)
        return ERROR_500
    #}
#}

def get_id(id) :#{
    if (not id) : return ERROR_400
    
    conn = get_connection()
    if (not conn): return DB_CONNECTION_ERROR
        
        
    try :#{
        cursor = conn.cursor()
        cursor.execute("""
        select  id, name, PaisNombre, country, CiudadNombre, city, address, phone, description
        from sucursal join pais on country = PaisCodigo join ciudad on city = CiudadID where id = %s
        """, [id])
        row_count = cursor.rowcount
        result = cursor.fetchone()
        if row_count == 0 :#{
            return {"message":"Sucursal no encontrada :("}, 404
        #}
        
        sucursal = {
            "id":result[0],
            "name":result[1],
            "country":result[2],
            "country_id":result[3],
            "city":result[4],
            "city_id":result[5],
            # "postalcode":result[4],
            "address":result[6],
            "phone":result[7],
            "description":result[8]
        }
        conn.close()
        return sucursal, 200
    #}
    except :#{
        return ERROR_500
    #} 
#}

def post(name, city, country, address, description, phone) :#{
    # Validar con regexs que los datos tengan el formato correcto
    if (not name or not city or not country or not address or not phone or not description) : return ERROR_400
    
    conn  = get_connection()
    if (not conn): return DB_CONNECTION_ERROR
    
    try :#{
        id = uuid4()
        cursor = conn.cursor()
        cursor.execute("insert into sucursal(id, name, country, city, address, phone, description)"\
            " values(%s, %s, %s, %s, %s, %s, %s)",[id, name, country, city, address, phone, description])
        conn.commit()
        conn.close()
        return {"message":"sucursal registrada exitosamente", "id" : id}, 200
    #}
    # except :#{
    except Exception as err:#{
        print(err)
        return ERROR_500
    #}
#}

def put(id, name, city, country, address, description, phone) :#{
    
    if (not id or not name or not city or not country or not address or not phone or not description) : return ERROR_400
    conn  = get_connection()
    if (not conn): return DB_CONNECTION_ERROR
    
    
    try :#{
        cursor = conn.cursor()
        cursor.execute("update sucursal set name=%s, country= %s, city= %s, phone= %s, address=%s, description= %s where id = %s",[name, country, city, phone, address, description,id])
        row_count = cursor.rowcount
        if (row_count == 0) :#{
            return {"message":"Sucursal a actualizar no encontrada :("}, 404
        #}
                
        conn.commit()
        conn.close()
        
        return {"message":"sucursal actualizada exitosamente"}, 200
    #}
    except :#{
        return ERROR_500
    #}
#}

def delete(id) :#{
    if (not id) : return ERROR_400
        
    conn = get_connection()
    if (not conn) : return DB_CONNECTION_ERROR
    
    try :#{
        cursor = conn.cursor()
        cursor.execute("delete from sucursal where id = %s",[id])
        row_count = cursor.rowcount
        if (row_count == 0) :#{
            return {"message":"La sucursal a eliminar no fue encontrada :("}, 404
        #}
        
        conn.commit()
        conn.close()
        
        return {"message": "Sucursal eliminada exitosamente"}, 200
    #}
    except :#{
        return ERROR_500
    #}
#}


# =====================================

def get_by_ubicacion(country, city = "") :#{
    conn = get_connection()
    if (not conn) : return DB_CONNECTION_ERROR
    
    try :#{
        cursor = conn.cursor()
        
        query = """select id, name, PaisNombre, country, CiudadNombre, city, address, phone, description
            from sucursal join pais on (country=PaisCodigo) join ciudad on(city=CiudadID) where country=%s """
        params = [country]
        if city : query += "and (city=%s or CiudadNombre = %s)"; params.append(city); params.append(city)
        cursor.execute(query, params)
        
        row_count = cursor.rowcount
        if (row_count == 0) :#{
            return {"message":"No se encontraron sucursales para esta region :("}, 404
        #}
        
        rows = cursor.fetchall()
        sucursales = []
        for row in rows :#{
            sucursales.append({
                "id":row[0],
                "name":row[1],
                "country":row[2],
                "country_id":row[3],
                "city":row[4],
                "city_id":row[5],
                # "postalcode":row[4],
                "address":row[6],
                "phone":row[7],
                "description":row[8]
            })
        #}
        return sucursales, 200
    #}
    except Exception as err :#{
    # except :#{
        print(err)
        return ERROR_500
    #}
#}
