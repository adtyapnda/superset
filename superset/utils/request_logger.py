import time
from flask import request, g
from flask_login import current_user

def before_request():
    g.start_time = time.time()

def after_request(response):
    if not hasattr(g, "start_time"):
        return response

    duration = round((time.time() - g.start_time) * 1000, 2)

    log = {
        "method": request.method,
        "path": request.path,
        "status": response.status_code,
        "duration_ms": duration,
        "user": current_user.username if current_user.is_authenticated else "anonymous",
        "ip": request.remote_addr,
    }

    print("[REQUEST LOG]", log)

    return response