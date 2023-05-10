import os, time
from dbfunctions import createConnection
from image_recognition.functions import getReferential, createListPattern, callDocumentAI, searchPatternDocumentAI


@app.route('/status/', methods = ['GET','POST'])
def scan():
  launch = False
  list_pattern = []
  if request.method == 'POST':
    filename = request.form.get('filename')
    launch = True
    conn = createConnection()
    list_pattern = createListPattern("amf")
    result = searchPatternDocumentAI(list_pattern, filename, UPLOAD_FOLDER)
    return render_template(
      'scan_status.html',
      context=result,
      launch=launch,
      filename=filename)
    
  
