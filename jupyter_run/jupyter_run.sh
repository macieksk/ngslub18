#!/bin/bash
set -e
#ipython notebook
echo "Usage: $(basename "$0") <port_number> [-p]" >&2
echo "    -p set new password" >&2
PORT="$1"
if [ -z "$PORT" ]; then exit 1; fi
if [ x"$2" = "x-p" ]; then
    jupyter notebook password
elif [ -n "$2" ]; then exit 1; fi

xvfb-run -a jupyter notebook --no-browser --ip=127.0.0.1 --port="$PORT" # --certfile=/home/msykulski/workspace/certbot/genxone_cert.pem

