#!/bin/bash
# Sets up or updates passCBAP on PythonAnywhere.
# Run from a PythonAnywhere Bash console:
#   git clone https://github.com/HulkOfKnowledge/passCBAP && cd passCBAP && bash deploy_pythonanywhere.sh
set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$HOME/.virtualenvs/passcbap-env"
cd "$PROJECT_DIR"

if [ ! -d "$VENV" ]; then
    python3.11 -m venv "$VENV"
fi
"$VENV/bin/pip" install --upgrade pip
"$VENV/bin/pip" install -r requirements.txt

"$VENV/bin/python" manage.py migrate --noinput
"$VENV/bin/python" manage.py collectstatic --noinput

WSGI_FILE="/var/www/${USER}_pythonanywhere_com_wsgi.py"

cat <<EOF

Done. Finish on the PythonAnywhere "Web" tab:
  1. Add a new web app -> Manual configuration -> Python 3.11 (first time only)
  2. Virtualenv:     $VENV
  3. Source code:    $PROJECT_DIR
  4. WSGI file ($WSGI_FILE), replace its contents with:

import os, sys
path = '$PROJECT_DIR'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'passCBAP.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

  5. Static files:   URL /static/  ->  $PROJECT_DIR/staticfiles
  6. Click Reload, then open https://${USER}.pythonanywhere.com
EOF
