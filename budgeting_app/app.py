from flask import Flask, request, render_template
import os
from utils import statement_pdf_processing

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload directory if it does not exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            table_data = statement_pdf_processing(file_path)
            if table_data:
                return render_template('table.html', table_data=table_data)
            else:
                return "Error processing the file. Please try again."
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)