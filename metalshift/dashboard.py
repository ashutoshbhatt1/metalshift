"""Synthetic operator dashboard for MetalShift validation evidence."""

import argparse
import json
from collections.abc import Sequence
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from metalshift.models.environments import all_environment_data

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>MetalShift Validation Control</title>
  <style>
    :root { color-scheme: dark; font-family: Inter, system-ui, sans-serif; }
    * { box-sizing: border-box; }
    body { margin: 0; background: #060d18; color: #eef6ff; }
    main { max-width: 1080px; margin: 0 auto; padding: 64px 28px; }
    .eyebrow { color: #54e5ad; letter-spacing: .14em; text-transform: uppercase; }
    h1 { margin: 10px 0 14px; font-size: clamp(2.5rem, 7vw, 5.3rem); line-height: .95; }
    .intro { max-width: 720px; color: #a7bad0; font-size: 1.08rem; }
    .summary { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin: 38px 0; }
    .card, table { background: #0d1a2b; border: 1px solid #1b3650; border-radius: 14px; }
    .card { padding: 20px; }
    .label { color: #7e9ab4; font-size: .78rem; text-transform: uppercase; }
    .value { display: block; margin-top: 8px; font-size: 1.75rem; }
    .ready { color: #54e5ad; }
    table { width: 100%; border-collapse: separate; border-spacing: 0; overflow: hidden; }
    th, td { padding: 15px 18px; text-align: left; border-bottom: 1px solid #1b3650; }
    th { color: #7e9ab4; font-size: .78rem; text-transform: uppercase; }
    tr:last-child td { border-bottom: 0; }
    .pill { color: #54e5ad; background: #102f2a; border-radius: 999px; padding: 5px 10px; }
    @media (max-width: 760px) { .summary { grid-template-columns: repeat(2, 1fr); } }
  </style>
</head>
<body>
  <main>
    <div class="eyebrow">Vendor-neutral synthetic lab</div>
    <h1>MetalShift<br>Validation Control</h1>
    <p class="intro">
      Bare-metal lifecycle, BMC, network readiness, and evidence status across test environments.
    </p>
    <section class="summary" aria-label="Validation summary">
      <article class="card"><span class="label">Status</span><strong id="status" class="value ready">Loading</strong></article>
      <article class="card"><span class="label">Environments</span><strong id="environments" class="value">—</strong></article>
      <article class="card"><span class="label">Hosts</span><strong id="hosts" class="value">—</strong></article>
      <article class="card"><span class="label">Networks</span><strong id="networks" class="value">—</strong></article>
    </section>
    <table aria-label="Environment readiness">
      <thead><tr><th>Environment</th><th>Datacenter</th><th>Hosts</th><th>Network state</th></tr></thead>
      <tbody id="environment-rows"></tbody>
    </table>
  </main>
  <script>
    fetch('/api/status').then(response => response.json()).then(data => {
      document.querySelector('#status').textContent = data.status;
      document.querySelector('#environments').textContent = data.summary.environments;
      document.querySelector('#hosts').textContent = data.summary.hosts;
      document.querySelector('#networks').textContent = data.summary.networks;
      document.querySelector('#environment-rows').innerHTML = data.environments.map(env => `
        <tr>
          <td>${env.name}</td><td>${env.datacenter}</td><td>${env.hosts}</td>
          <td><span class="pill">${env.network_state}</span></td>
        </tr>`).join('');
    });
  </script>
</body>
</html>
"""


def build_status_payload() -> dict[str, Any]:
    """Build a public-safe status payload from MetalShift's synthetic fixtures."""
    environments = all_environment_data()
    environment_rows = [
        {
            "name": data.environment.name,
            "datacenter": data.environment.datacenter,
            "hosts": len(data.hosts),
            "networks": len(data.networks),
            "network_state": "Ready",
        }
        for data in environments
    ]
    return {
        "status": "Ready",
        "summary": {
            "environments": len(environments),
            "hosts": sum(len(data.hosts) for data in environments),
            "networks": sum(len(data.networks) for data in environments),
        },
        "environments": environment_rows,
    }


class DashboardHandler(BaseHTTPRequestHandler):
    """Serve the dashboard and its machine-readable status endpoint."""

    def do_GET(self) -> None:
        if self.path == "/":
            self._respond(200, HTML.encode(), "text/html; charset=utf-8")
        elif self.path == "/health":
            self._json(200, {"status": "ok"})
        elif self.path == "/api/status":
            self._json(200, build_status_payload())
        else:
            self._json(404, {"error": "not found"})

    def _json(self, status: int, payload: object) -> None:
        self._respond(status, json.dumps(payload).encode(), "application/json")

    def _respond(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        """Keep automated test output free of request noise."""


def create_server(host: str = "127.0.0.1", port: int = 0) -> ThreadingHTTPServer:
    """Create a server; port zero lets tests request an available local port."""
    return ThreadingHTTPServer((host, port), DashboardHandler)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run MetalShift's synthetic status dashboard")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args(argv)
    server = create_server(args.host, args.port)
    print(f"MetalShift dashboard listening on http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
