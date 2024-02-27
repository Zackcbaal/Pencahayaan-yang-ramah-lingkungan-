from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size, lights, device):
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# Variabel untuk menyimpan data formulir
form_data = {
    'name': '',
    'email': '',
    'address': '',
    'date': ''
}

# Halaman pertama
@app.route('/')
def index():
    return render_template('index.html')

# Halaman kedua
@app.route('/<size>')
def lights(size):
    return render_template('lights.html', size=size)

# Halaman ketiga
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

# Perhitungan
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    try:
        result = result_calculate(int(size), int(lights), int(device))
        return render_template('end.html', result=result)
    except ValueError:
        # Handle invalid input, for example, redirect to an error page or show a message
        return render_template('error.html', message='Invalid input. Please enter valid numeric values.')

# Formulir
@app.route('/form')
def form():
    return render_template('form.html')

# Hasil formulir
@app.route('/submit', methods=['POST'])
def submit_form():
    # Mendeklarasikan variabel untuk pengumpulan data
    form_data['name'] = request.form['name']
    form_data['email'] = request.form['email']
    form_data['address'] = request.form['address']
    form_data['date'] = request.form['date']

    # Menyimpan data ke dalam file .txt
    with open('form.txt', 'a') as f:
        f.write(f"Name: {form_data['name']}, Email: {form_data['email']}, Address: {form_data['address']}, Date: {form_data['date']}\n")

    # Anda dapat menyimpan data Anda atau mengirimkannya melalui email
    return render_template('form_result.html', data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
