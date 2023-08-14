from liquid import Liquid

def render_liquid_md(
    template_file_name: str,
    rendered_file_name: str,
    repo_title: str, 
    repo_summary: str, 
    repo_sections: dict) -> None:
    
    def write_rendered_content(content):
        try:
            with open(rendered_file_name, 'w') as file:
                file.write(content)
                file.close()
        except FileNotFoundError as e:
            print(repr(e))
        
    with open(template_file_name, "r") as template_file:
        template = template_file.read()
        
    liquid = Liquid(template_file_name)

    rendered_content = liquid.render(
        repo_title=repo_title,
        repo_summary=repo_summary, 
        sections=repo_sections
    )

    template_file.close()
    write_rendered_content(rendered_content)
    
render_liquid_md(   
    template_file_name="repo_template.md",
    rendered_file_name="rendered/TEST.md",
    repo_title="Test",
    repo_summary="A new test repository for liquid markdown templates",
    repo_sections=[
        {
            "section_header": "Table Of Contents",
            "section_summary": "The toc section",
            "section_image": None,
        },
        {
            "section_header": "About",
            "section_summary": "The about section",
            "section_image": None,
        },
        {
            "section_header": "Install",
            "section_summary": "The install section",
            "section_image": None,
        },
        {
            "section_header": "Usage",
            "section_summary": "The usage section",
            "section_image": None,
        },
        {
            "section_header": "Contributing",
            "section_summary": "The contributing section",
            "section_image": None,
        },
        {
            "section_header": "Security",
            "section_summary": "The security section",
            "section_image": None,
        },
        {
            "section_header": "Contacts",
            "section_summary": "The contacts section",
            "section_image": None,
        },
    ]
)
