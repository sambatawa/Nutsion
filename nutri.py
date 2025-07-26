import mysql.connector
import os
import json
import openai

openai.api_key = "OPENAI_API_KEY"

def tanyagpt(prompt, history):
    try:
        openai_messages = []
        for h in history:
            if "role" in h and "content" in h:
                openai_messages.append(h)

        openai_messages.append({"role": "user", "content": prompt})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=openai_messages,
        )
        reply = completion['choices'][0]['message']['content']

        history.append({"role": "user", "content": prompt})
        history.append({"role": "assistant", "content": reply})
        return reply, history
    except Exception as e:
        print("OpenAI error:", e)
        return "Maaf, terjadi kesalahan saat mengakses AI.", history

def kandungan(nama_makanan):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", 
            database="data_nutrisi"
        )
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM makanan WHERE LOWER(nama_makanan) LIKE %s LIMIT 1"
        cursor.execute(query, ('%' + nama_makanan.lower() + '%',))
        result = cursor.fetchone()
        
        cursor.close()
        connection.close()
        return result
    
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None

def ambilchat(session):
    os.makedirs('chat', exist_ok=True)
    filepath = os.path.join('chat', f"{session}.json")
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def simpanchat(session, userinput, botresponse):
    os.makedirs('chat', exist_ok=True)
    filepath = os.path.join('chat', f"{session}.json")
    history = ambilchat(session)
    history.append({"role": "user", "content": userinput})
    history.append({"role": "assistant", "content": botresponse})
    with open(filepath, 'w') as file:
        json.dump(history, file)
