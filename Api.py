from flask import Flask, request, Response

app=Flask(__name__)

@app.route('/xml', method=['POST'])
def xml():
    strXml=request.data.decode('utf-8')
    print(strXml)
if __name__=='__main__':
    app.run(debug=True)

