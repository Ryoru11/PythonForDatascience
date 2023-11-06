import dash
from layout import get_layout
from callbacks import register_callbacks
import dashboard

app = dash.Dash(__name__)
app.layout = get_layout()
register_callbacks(app)

def main():
    dashboard.dashboard


if __name__ == '__main__':
    app.run_server(debug=True)
