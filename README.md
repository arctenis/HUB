# README

HUB - HTML Unit Builder

HUB is a static website generator based on markdown files. It turns a git
repository into a website. 

## Installation

```bash
pip install hub
```

## Usage

```bash
hub init
```

This will create a new git repository with an index.md file in a 'content'
directory and a config.yml in the project directory.

```bash
hub build
```

This will build your website into the 'build' directory.

```bash
hub serve
```

This will start a webserver on port 8000. It will automatically rebuild the
website when you change a file.
