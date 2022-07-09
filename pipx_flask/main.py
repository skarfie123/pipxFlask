import math
import webbrowser
from threading import Timer

from flask import Flask, cli

cli.show_server_banner = lambda *_: None

app = Flask(__name__)


@app.route("/")
def index():
    return f'<a href="/gAYL5H46QnQ">Hello</a> <a href="/{int(math.pi*10e9)}">world</a>!'


@app.route("/<int:work_id>")
def work(work_id):
    diagram = f"graph TD\nA[{work_id}] -->|x2| B[{work_id*2}]"
    return f"""<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
    mermaid.initialize({{ startOnLoad: true }});
</script>
<div class="mermaid">{diagram}</div>"""


@app.route("/<life_id>")
def life(life_id):
    return f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{life_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'


def main():
    host = "127.0.0.1"
    port = 12345
    Timer(1, lambda: webbrowser.open_new(f"http://{host}:{port}/")).start()
    app.run(host=host, port=port)


if __name__ == "__main__":
    main()
