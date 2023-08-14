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
    
PROJECT_TITLE = "Test Template"
RENDERED_FILE = "rendered/TEST.md"
TEMPLATE_FILE = "general_repo_template.md"
REPO_SUMMARY = "A new test repository for liquid markdown templates"
SECTIONS = [
        {
            "section_header": "Table Of Contents",
            "section_summary": None,
            "section_image": None,
        },
        {
            "section_header": "About",
            "section_summary": None,
            "section_image": None,
        },
        {
            "section_header": "Install",
            "section_summary": None,
            "section_image": None,
        },
        {
            "section_header": "Usage",
            "section_summary": None,
            "section_image": None,
        },
        {
            "section_header": "Contributing",
            "section_summary": None,
            "section_image": None,
        },
        {
            "section_header": "Security",
            "section_summary": None,
            "section_image": None,
        },
        {
            "section_header": "Contacts",
            "section_summary": None,
            "section_image": None,
        },
    ]

render_liquid_md(   
    template_file_name=TEMPLATE_FILE,
    rendered_file_name=RENDERED_FILE,
    repo_title=PROJECT_TITLE,
    repo_summary=REPO_SUMMARY,
    repo_sections=SECTIONS
)
