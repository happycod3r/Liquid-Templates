from liquid import Liquid


def render_liquid_md(file_name: str, repo_title: str, repo_sections: dict) -> None:
    title = repo_title
    sections = repo_sections

    with open(file_name, "r") as template_file:
        template = template_file.read()
        
    liquid = Liquid(file_name)

    rendered_content = liquid.render(
        repo_title=title, 
        sections=sections
    )

    template_file.close()
    print(rendered_content)
    
render_liquid_md(   
    "repo_template.md",
    "Test",
    [
        {"section_header": "Table Of Contents"},
        {"section_header": "About"},
        {"section_header": "Install"},
        {"section_header": "Usage"},
        {"section_header": "Contributing"},
        {"section_header": "Security"},
        {"section_header": "Contacts"}, 
    ]
)
