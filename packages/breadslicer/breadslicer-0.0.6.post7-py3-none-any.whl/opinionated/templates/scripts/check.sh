#!/bin/sh

poetry check
{% if project_type == "django" %}
./manage.py check
{% endif %}