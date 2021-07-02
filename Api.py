from flask import Flask, request, Response
from flask_cors import CORS
app=Flask(__name__)
cors=CORS(app, resources={r"/*":{"origin":"*"}})


@app.route('/xml', methods=['GET'])
def getxml():
    archivoxml=open('archivoxml.xml','r+')
    texto=str(archivoxml.read())
    print(texto)
    return Response(status=200,response=texto, content_type='text/xml')

@app.route('/xml', methods=['POST'])

def postxml():
    strXml=request.data.decode('utf-8')
    print(strXml)
    archivoxml=open('archivoxml.xml','w+')
    archivoxml.write(strXml)
    archivoxml.close()
    return Response(status=204)
if __name__=='__main__':
    app.run(debug=True)

