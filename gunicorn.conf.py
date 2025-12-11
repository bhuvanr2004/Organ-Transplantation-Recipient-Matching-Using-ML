import multiprocessing
import os

workers = int(os.environ.get('GUNICORN_WORKERS', multiprocessing.cpu_count() * 2 + 1))
threads = int(os.environ.get('GUNICORN_THREADS', 2))

bind = os.environ.get('BIND', '0.0.0.0:5000')

worker_class = 'sync'
worker_connections = 1000
timeout = 120
keepalive = 5

max_requests = 1000
max_requests_jitter = 100

accesslog = '-'
errorlog = '-'
loglevel = os.environ.get('LOG_LEVEL', 'info')

capture_output = True
enable_stdio_inheritance = True

preload_app = False

def on_starting(server):
    print(f"Starting Gunicorn server with {workers} workers and {threads} threads per worker")

def worker_int(worker):
    print(f"Worker {worker.pid} received SIGINT, shutting down gracefully")

def worker_abort(worker):
    print(f"Worker {worker.pid} aborted")
