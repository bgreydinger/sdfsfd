"""App entry point."""
from main import create_app

app = create_app()

server = app.server()

if __name__ == "__main__":
    app.run_server(debug=True)
