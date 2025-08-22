from recipe import create_app

app = create_app()

if __name__ == '__name__':
    app.run(host='localhost', port=5000)