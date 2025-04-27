import mysql.connector

class Pool:
    DATABASE = "gestion_inventario"
    USERNAME = "root"
    PASSWORD = "Root@123"
    HOST = "localhost"
    DB_PORT = 3306
    POOL_SIZE = 5
    POOL_NAME = "gestion_inventario_pool"
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    database=cls.DATABASE,
                    port=cls.DB_PORT
                )
                return cls.pool
            except mysql.connector.Error as err:
                print(f"Error: {err}")
        else:
            return cls.pool
        
    @classmethod
    def obtener_conexion(cls):
        try:
            connection = cls.obtener_pool().get_connection()
            return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        
    @classmethod
    def liberar_conexion(cls, conexion):
        if conexion:
            conexion.close()
            print("Conexión liberada.")
        else:
            print("No hay conexión para liberar")

if __name__ == "__main__":
    pool = Pool.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Pool.liberar_conexion(conexion1)
