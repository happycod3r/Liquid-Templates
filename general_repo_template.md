# {{ repo_title }}
{{ repo_summary }}
{% for section in sections %}
## [{{ section.section_header }}](#)
{% if section.section_header == "Table Of Contents" %}
{% if section.section_summary != None %}
{{ section.section_summary }}
{% endif %}
{% endif %}

{% if section.section_header == "About" %}
{% if section.section_summary != None %}
{{ section.section_summary }}
{% endif %}
{% endif %}

{% if section.section_header == "Install" %}
{% if section.section_summary != None %}
{{ section.section_summary }}
{% endif %}
{% endif %}

{% if section.section_header == "Usage" %}
{% if section.section_summary != None %}
{{ section.section_summary }}
{% endif %}
{% endif %}

{% if section.section_header == "Contributing" %}
{% if section.section_summary != None %}
{{ section.section_summary }}
{% endif %}
If you have any feature requests, suggestions or general questions you can reach 
me via any of the methods listed below in the [Contacts](#contacts) section.

Other than that please feel free to reach out and contribute to the project if 
your interested.
{% endif %}

{% if section.section_header == "Security" %}
### Reporting a vulnerability or bug?
Do not submit an issue or pull request: A general rule of thumb is to never publicly report bugs or vulnerabilities because you might inadvertently reveal it to unethical people who may use it for bad. Instead, you can email me directly at: [paulmccarthy676@gmail.com](mailto:paulmccarthy676@gmail.com). I will deal with the issue privately and submit a patch as soon as possible.
{% endif %}
    
{% if section.section_header == "Contacts" %}
**Author:** Paul M.
- Email: [paulmccarthy676@gmail.com](mailto:paulmccarthy676@gmail.com)
- Github: [https://github.com/happycod3r](https://github.com/happycod3r)
- Linkedin: [https://www.linkedin.com/in/paul-mccarthy-89165a269/](https://www.linkedin.com/in/paul-mccarthy-89165a269/)
- Facebook: [https://www.facebook.com/paulebeatz](https://www.facebook.com/paulebeatz)
{% endif %}

{% endfor %}
