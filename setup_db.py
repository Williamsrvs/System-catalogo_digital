#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configurador Interativo de Banco de Dados
Ajuda você a configurar as credenciais corretas
"""

import os
import subprocess
import sys
from dotenv import load_dotenv
import mysql.connector

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def test_connection(host, user, password, database, port):
    """Testa se a conexão funciona"""
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
            autocommit=False,
            connection_timeout=5
        )
        conn.close()
        return True, None
    except mysql.connector.Error as e:
        return False, str(e)

def configure_local_mysql():
    """Guia para configurar MySQL local"""
    print("\n" + "="*70)
    print("⚙️  CONFIGURAÇÃO DO MYSQL LOCAL")
    print("="*70)
    
    print("\nVocê tem 3 opções:\n")
    
    print("1️⃣  WINDOWS - MySQL/MariaDB Instalado")
    print("   Verifique se o serviço está rodando:")
    print("   • Serviços > MySQL80 ou MariaDB > Iniciar")
    print("   • Ou: Get-Service MySQL80")
    
    print("\n2️⃣  DOCKER (Recomendado)")
    print("   Execute este comando:")
    print("   docker run --name mysql-local \\")
    print("     -e MYSQL_ROOT_PASSWORD=root \\")
    print("     -e MYSQL_DATABASE=catalogo_digital \\")
    print("     -p 3306:3306 -d mysql:8.0")
    
    print("\n3️⃣  XAMPP/WAMP/MAMP")
    print("   Inicie o painel de controle e ative o MySQL")
    
    print("\n" + "="*70)

def main():
    print("\n" + "="*70)
    print("🔧 CONFIGURADOR INTERATIVO - CATÁLOGO DIGITAL")
    print("="*70)
    
    # Carregar .env existente
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path=env_path)
    
    host = os.getenv('MYSQL_HOST', 'localhost')
    user = os.getenv('MYSQL_USER', 'root')
    password = os.getenv('MYSQL_PASSWORD', '')
    database = os.getenv('MYSQL_DB', 'catalogo_digital')
    port = int(os.getenv('MYSQL_PORT', 3306))
    
    print("\n📝 CONFIGURAÇÃO ATUAL:")
    print(f"  Host: {host}")
    print(f"  Usuário: {user}")
    print(f"  Banco: {database}")
    print(f"  Porta: {port}")
    print(f"  Senha: {'***' if password else '(vazia)'}")
    
    # Testar conexão atual
    print("\n🔗 Testando conexão com credenciais atuais...")
    success, error = test_connection(host, user, password, database, port)
    
    if success:
        print("✅ CONEXÃO BEM-SUCEDIDA!")
        print("\n✨ Você pode iniciar a aplicação com: python app.py")
        return
    else:
        print(f"❌ FALHA: {error}")
    
    # Menu de opções
    print("\n" + "="*70)
    print("PRÓXIMAS ETAPAS:")
    print("="*70)
    print("\n1. Verifique se o MySQL está instalado e rodando")
    print("2. Ajuste as credenciais no arquivo .env")
    print("3. Execute este script novamente para testar")
    
    configure_local_mysql()
    
    print("\n📝 EDITAR CREDENCIAIS:")
    print("\nAbra o arquivo '.env' e atualize:")
    print("""
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=root       # 👈 Ajuste conforme seu MySQL
MYSQL_DB=catalogo_digital
MYSQL_PORT=3306
""")
    
    print("\n💡 DICAS COMUNS:")
    print("  • Se acabou de instalar: senha pode estar vazia ou 'root'")
    print("  • Docker: use a senha que configurou no comando (ex: root)")
    print("  • XAMPP: geralmente password vazia ou 'password'")
    print("  • MySQL Community: você configurou durante instalação")
    
    # Perguntar se deseja tentar novamente
    while True:
        print("\n" + "="*70)
        resp = input("Atualizou as credenciais? [S/n] ").strip().lower()
        
        if resp in ['s', 'yes', '']:
            # Recarregar .env
            load_dotenv(dotenv_path=env_path, override=True)
            
            host = os.getenv('MYSQL_HOST', 'localhost')
            user = os.getenv('MYSQL_USER', 'root')
            password = os.getenv('MYSQL_PASSWORD', '')
            database = os.getenv('MYSQL_DB', 'catalogo_digital')
            port = int(os.getenv('MYSQL_PORT', 3306))
            
            print(f"\n🔗 Testando nova conexão em {host}...")
            success, error = test_connection(host, user, password, database, port)
            
            if success:
                print("✅ SUCESSO! Conexão estabelecida!")
                print("\n✨ Agora você pode iniciar: python app.py")
                print("="*70 + "\n")
                return
            else:
                print(f"❌ Ainda não funciona: {error}")
                continue
        else:
            print("OK, ajuste o .env e execute novamente!")
            return

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação cancelada pelo usuário")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        sys.exit(1)
