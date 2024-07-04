#!/bin/sh
{% if project_layout == "src"%}
src/{{ project_slug }}/main.py $@
{% elif project_layout == "flat"%}
{{ project_slug }}/main.py $@
{% endif %}