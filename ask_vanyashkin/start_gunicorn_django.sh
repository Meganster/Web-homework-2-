#!/bin/bash
gunicorn -c gunicorn.conf.py ask_vanyashkin.wsgi:application