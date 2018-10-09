# {{ name }}

![{{ name }}]({{ image }} =200 "{{ name }}")

* Temps de préparation: {{ prep_time }}
* Temps de cuisson: {{ cook_time }}

## Ingrédients
{% for ingredient in ingredients %}
- {{ ingredient }}
{%- endfor %}

## Etapes
{% for step in steps %}
- {{ step }}
{%- endfor %}

***
_([lien]({{ recipe_url }}))_
