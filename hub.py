""" 
HUB is a CLI tool that can be used to generate a static site from the
command line. It uses a simple directory structure to generate a static site.
It is designed to be used with a git repository to make it easy to deploy to a
web server. Write markdown files in the content directory and HUB will generate
a static site in the 'build' directory. 
"""

import typer
import markdown
import os

app = typer.Typer()


@app.command()
def init(path: str):
    typer.echo("Creating a new HUB site")
    # Check if path exists
    if os.path.exists(path):
        typer.echo("Directory already exists")
        return
    os.mkdir(path)
    # Create a 'content' directory
    os.mkdir(f"{path}/content")
    with open(f"{path}/content/index.md", "w") as f:
        f.write("# Welcome to HUB\n")
        f.write("This is the index page of your site.\n")
        f.close()
    # Create a 'build' directory
    os.mkdir(f"{path}/build")
    # Create a 'css' directory
    os.mkdir(f"{path}/build/css")
    # Create a 'default.css' file
    with open(f"{path}/build/css/default.css", "w") as f:
        f.write("body {\n")
        f.write("    font-family: sans-serif;\n")
        f.write("    background-color: black;\n")
        f.write("    color: white;\n")
        f.write("}\n")
        f.close()
    # Create a 'config.yaml' file
    with open(f"{path}/config.yaml", "w") as f:
        f.write("title: My new HUB Site\n")
        f.write("author: Your Name\n")
        f.write("description: A description of your site\n")
        f.write("url: https://example.com\n")
        f.write("theme: default\n")
        f.write("language: en\n")
        f.write("index: index.md\n")
        f.close()


@app.command()
def build(project_path: str):
    """
    Create static html files from the markdown files in the 'content' directory.
    """
    typer.echo("Building site")
    for filename in os.listdir(f"{project_path}/content"):
        # Check if the file is a markdown file
        if filename.endswith(".md"):
            # Read the markdown file
            with open(f"{project_path}/content/" + filename, "r") as f:
                content = f.read()
                f.close()
            # Convert the markdown file to HTML
            html = markdown.markdown(content)
            # Add css link based on the theme in the config file
            theme = "default"
            with open(f"{project_path}/config.yaml", "r") as f:
                # Read theme parameter from YAML file
                for line in f:
                    if line.startswith("theme"):
                        theme = line.split(":")[1].strip()
                        break
                f.close()
            # Add the css link to the HTML
            html = f'<link rel="stylesheet" href="css/{theme}.css">\n' + html
            # Write the HTML to a file in the 'build' directory
            with open(
                f"{project_path}/build/" + filename.replace(".md", ".html"), "w"
            ) as f:
                f.write(html)
                f.close()


if __name__ == "__main__":
    app()
