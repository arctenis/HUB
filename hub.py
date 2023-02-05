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
def init(path:str):
    typer.echo("Creating a new HUB site")
    # Create a 'content' directory
    os.mkdir(f"{path}/content")
    with open(f"{path}/content/index.md", "w") as f:
        f.write("# Welcome to HUB\n")
        f.write("This is the index page of your site.\n")
        f.close()
    # Create a 'build' directory
    os.mkdir(f"{path}/build")
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
def build():
    typer.echo("Building site")
    # Turn markdown files in 'content' directory into HTML
    # Iterate over the files in the 'content' directory
    for filename in os.listdir("content"):
        # Check if the file is a markdown file
        if filename.endswith(".md"):
            # Read the markdown file
            with open("content/" + filename, "r") as f:
                content = f.read()
                f.close()
            # Convert the markdown file to HTML
            html = markdown.markdown(content)
            # Write the HTML to a file in the 'build' directory
            with open("build/" + filename.replace(".md", ".html"), "w") as f:
                f.write(html)
                f.close()
    


if __name__ == "__main__":
    app()
