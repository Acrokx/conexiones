#include <mysql/mysql.h>
#include <iostream>

int main() {
    MYSQL *conn;
    conn = mysql_init(0);
    if (conn) {
        conn = mysql_real_connect(conn, "localhost", "root", "password", "mi_base_de_datos", 0, NULL, 0);
        if (conn) {
            if (mysql_query(conn, "SELECT * FROM tabla")) {
                std::cout << "Error en la consulta: " << mysql_error(conn) << std::endl;
            } else {
                MYSQL_RES *res = mysql_store_result(conn);
                MYSQL_ROW row;
                while ((row = mysql_fetch_row(res))) {
                    std::cout << row[0] << " " << row[1] << std::endl;
                }
            }
            mysql_close(conn);
        } else {
            std::cout << "No se pudo conectar a la base de datos: " << mysql_error(conn) << std::endl;
        }
    }
    return 0;
}
