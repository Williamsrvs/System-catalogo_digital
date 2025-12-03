import MySQLdb

#try:
    #conn = MySQLdb.connect(
        #host="auth-db1937.hstgr.io",
        #user="u799109175_menu_prod",
        #passwd="Q1k2v1y5@2025",
        #db="u799109175_menu_prod"
    #)

try:
    conn = MySQLdb.connect(
        host="193.203.175.250",
        user="u799109175_menu_prod",
        passwd="Q1k2v1y5@2025",
        db="u799109175_menu_prod",
        port=3306
    )
    cursor = conn.cursor()

    print("✅ Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print("❌ Erro:", e)
