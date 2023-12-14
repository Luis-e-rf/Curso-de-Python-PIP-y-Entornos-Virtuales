import store

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
    <html>
        <head>
            <title>Yurak Web</title>
        </head>
        <body>
            <h1>Mi primer servidor web!</h1>
            <p>Yurak aparece en la web :)</p>
        </body>
    </html>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()