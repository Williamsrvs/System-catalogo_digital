import MySQLdb
import sys

print("="*60)
print("🔐 TESTE DE CREDENCIAIS - SERVICE TOUR")
print("="*60)

# ⚠️ TESTE 1: Credenciais do projeto atual
config_atual = {
    'host': 'auth-db1937.hstgr.io',
    'user': 'u799109175_menu_prod',
    'passwd': 'Q1k2v1y5@2025',
    'db': 'u799109175_menu_prod',
    'port': 3306,
    'connect_timeout': 10
}

print("\n📋 Testando credenciais ATUAIS:")
print(f"   Host: {config_atual['host']}")
print(f"   User: {config_atual['user']}")
print(f"   DB: {config_atual['db']}")
print(f"   Password: {'*' * len(config_atual['passwd'])}")

try:
    conn = MySQLdb.connect(**config_atual)
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE(), USER()")
    db, user = cursor.fetchone()
    print(f"\n✅ SUCESSO!")
    print(f"   Database conectado: {db}")
    print(f"   User autenticado: {user}")
    cursor.close()
    conn.close()
except MySQLdb.OperationalError as e:
    print(f"\n❌ FALHOU!")
    print(f"   Erro {e.args[0]}: {e.args[1]}")
    print("\n⚠️  POSSÍVEIS CAUSAS:")
    print("   1. Senha incorreta")
    print("   2. Usuário não existe")
    print("   3. IP não autorizado no servidor")
    print("   4. Banco de dados não existe")
except Exception as e:
    print(f"\n❌ ERRO: {e}")

print("\n" + "="*60)
print("📝 AGORA TESTE COM AS CREDENCIAIS DO PROJETO QUE FUNCIONA:")
print("="*60)
print("""
Edite este arquivo e adicione:

config_funciona = {
    'host': 'SEU_HOST_QUE_FUNCIONA',
    'user': 'SEU_USER_QUE_FUNCIONA',
    'passwd': 'SUA_SENHA_QUE_FUNCIONA',
    'db': 'SEU_DB_QUE_FUNCIONA',
    'port': 3306,
    'connect_timeout': 10
}

E descomente as linhas abaixo para testar.
""")

# 🔧 DESCOMENTE AQUI E ADICIONE AS CREDENCIAIS QUE FUNCIONAM:
"""
print("\n📋 Testando credenciais do PROJETO QUE FUNCIONA:")
config_funciona = {
    'host': 'auth-db1937.hstgr.io',
    'user': 'COLOQUE_AQUI',
    'passwd': 'COLOQUE_AQUI',
    'db': 'COLOQUE_AQUI',
    'port': 3306,
    'connect_timeout': 10
}

try:
    conn = MySQLdb.connect(**config_funciona)
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE(), USER()")
    db, user = cursor.fetchone()
    print(f"✅ SUCESSO!")
    print(f"   Database: {db}")
    print(f"   User: {user}")
    cursor.close()
    conn.close()
except Exception as e:
    print(f"❌ FALHOU: {e}")
"""