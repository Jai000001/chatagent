#!/bin/sh

gunicorn app.main:app \
    --bind 0.0.0.0:${APP_PORT:-5000} \
    --workers ${APP_WORKERS:-4} \
    --worker-class uvicorn.workers.UvicornWorker \
    --timeout 3600 \
    --log-level info

# gunicorn app.main:app \
#     --bind 0.0.0.0:${APP_PORT:-5000} \
#     --workers ${APP_WORKERS:-2} \
#     --worker-class uvicorn.workers.UvicornWorker \
#     --preload \
#     --timeout 3600 \
#     --log-level info    

# uvicorn cogent_app:app --host 0.0.0.0 --port ${APP_PORT:-5000} --workers ${APP_WORKERS:-4} --log-level warning