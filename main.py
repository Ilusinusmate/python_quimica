from flask import Flask, render_template, request
from flask.wrappers import Response
app = Flask(__name__)

@app.get("/")
def home():
    return("<h1> Home </h1>")

@app.get("/elements/")
def elements():
    args = request.args.to_dict("query")

    # Implementar lógica de input/output stream
    if args:
        args["mensage"] = "Querry recebida com sucesso!"
        print(args)
        return Response(args,status='200')
    else:
        return Response("Nenhuma query recebida", status=400)

if __name__ == "__main__":
    app.run(port='8000', debug=True)