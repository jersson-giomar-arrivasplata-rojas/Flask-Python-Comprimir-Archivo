import os
from flask import Flask, flash, request, redirect, url_for,render_template,send_from_directory
from werkzeug.utils import secure_filename
import zipfile

UPLOAD_FOLDER = 'templates/file'
UPLOAD_FOLDER_COMPRESOR='comprimido'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','zip','rar'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_COMPRESOR'] = UPLOAD_FOLDER_COMPRESOR



def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            nombreArchivo=file.filename.rsplit('.', 1)[0].lower().strip() 
            jungle_zip = zipfile.ZipFile('comprimido'+'/'+nombreArchivo+'.zip', 'w')
            jungle_zip.write('templates/file/'+file.filename, compress_type=zipfile.ZIP_DEFLATED)
            jungle_zip.close()

            return send_from_directory(app.config['UPLOAD_FOLDER_COMPRESOR'],  nombreArchivo+'.zip') # '<a href="comprimido/'+nombreArchivo+'.zip" download>Descargar</a>' #"redirect(url_for('uploaded_file',  filename=filename))"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
    </form>
    '''
@app.route('/<filename>')
def uploaded_file(filename):
        
    return send_from_directory(app.config['UPLOAD_FOLDER'],  filename)

@app.route("/", methods = [ 'GET'])
def main():
    return render_template('index.html')

#Recomendacion crear el insertar aqui

if __name__ == "__main__":
    app.run()