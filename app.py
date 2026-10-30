import sqlite3

def login(username, password):
    conn = sqlite3.connect('banco_laboratorio.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM usuarios WHERE user = ? AND pass = ?"
    
    try:
        cursor.execute(query, (username, password))
        resultado = cursor.fetchone()
        if resultado:
            return "Acesso Permitido"
        return "Acesso Negado"
    except Exception as e:
        return f"Erro no banco: {e}"

print(login("admin' --", "senha_ignorada"))