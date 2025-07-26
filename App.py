from flask import Flask, request, render_template, jsonify
from nutri import ambilchat, kandungan, simpanchat, tanyagpt
from datetime import datetime

app = Flask(__name__)

def current_date():
    return datetime.now().strftime("%Y-%m-%d")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    userinput = request.json.get('message', '')
    session = request.remote_addr + "_" + current_date()
    history = ambilchat(session)

    if any(x in userinput.lower() for x in ['kandungan', 'nutrisi', 'gizi']):
        nama = userinput.lower()
        for prefix in ['kandungan', 'nutrisi', 'gizi', 'di', 'dari', 'mengenai']:
            nama = nama.replace(prefix, '')
        nama = nama.strip()
        data = kandungan(nama)
        if data:
            response = (
                f"{data.get('nama_makanan', nama).capitalize()} merupakan makanan yang mengandung sekitar "
                f"{data.get('kalori', '?')} kCal energi. Dalam 100 gramnya, makanan ini mengandung "
                f"{data.get('protein', '?')} mg protein, {data.get('lemak', '?')} mg lemak, dan "
                f"{data.get('karbohidrat', '?')} mg karbohidrat. Kandungan seratnya mencapai "
                f"{data.get('serat', '?')} mg, dengan kadar air sekitar {data.get('air', '?')} l. "
                f"Selain itu, makanan ini juga mengandung {data.get('kalsium', '?')} mg kalsium "
                f"dan {data.get('zatbesi', '?')} mg zat besi."
            )
        else:
            response = "Maaf, saya tidak menemukan informasi tentang makanan tersebut."
        simpanchat(session, userinput, response)
        return jsonify({'response': response})

    jawaban, updatehistory = tanyagpt(userinput, history)
    simpanchat(session, userinput, jawaban)
    return jsonify({'response': jawaban})

if __name__ == '__main__':
    app.run(debug=True)
