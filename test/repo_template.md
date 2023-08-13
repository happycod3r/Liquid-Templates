# Welcome to {{ site_name }}
{% for post in posts %}
  ## {{ post.title }}
  {{ post.excerpt }}
{% endfor %}
