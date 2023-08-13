from liquid import Liquid


def render_liquid_md(repo_title: str, repo_sections: list) -> None:
    repo_title = repo_title
    sections = repo_sections
    posts = [
        {"title": "Post 1", "excerpt": "Excerpt 1"},
        {"title": "Post 2", "excerpt": "Excerpt 2"}
    ]

    with open("test_template.md", "r") as template_file:
        template = template_file.read()
        
    liquid = Liquid("test_template.md")

    rendered_content = liquid.render(
        site_name=site_name, 
        posts=posts
    )

    template_file.close()
    print(rendered_content)
    
render_liquid_md(
    
)
