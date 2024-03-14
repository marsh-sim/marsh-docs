# Documentation

Documentation for all projects under MARSH-Sim.

All sources for these pages are in a [GitHub repository](https://github.com/marsh-sim/marsh-sim.github.io). It is set up to automatically build the documentation on every commit on GitHub servers. The public version at [marsh-sim.github.io](https://marsh-sim.github.io/) is updated every time the `main` branch is changed, the actual files served are from `gh-pages`.

## Local installation

The pages can be built into HTML and other formats using Python. A virtual environment is recommended to avoid mixing this documentation with system packages.

The following commands can be used for Linux:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

For users on Windows, only the line to activate the virtual environment changes to:

```ps1
./venv/Scripts/activate
```

## Usage

Once a local installation is complete, the pages can be re-built live with:

```bash
mkdocs serve
```

## Contributing

Content is written in Markdown and built to HTML with [MkDocs](https://www.mkdocs.org/). Markdown files should preferably be formatted with [markdownlint extension for VS Code](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint).

### Recommended resources

- [Make a Readme](https://www.makeareadme.com/)
- [Readme Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html)
- [More Software Projects need Defenses of Design](https://buttondown.email/hillelwayne/archive/more-software-projects-need-defenses-of-design/)

### Defense of Design

The goal for this setup of the documentation was to make it simple to update to users who come from aerospace engineering background and may not be familiar with the web technologies at large. A single documentation for all related projects was chosen to simplify navigation, allow easier cross linking between different concepts, and make it easier to search.

The web pages are generated with MkDocs, because it uses Python which most colleagues already know. The alternatives used by related projects like GitBook (for MAVLink Dev Guide) are not free anymore, and VuePress (for PX4) requires NodeJS. Initially the more popular Sphinx was chosen, but didn't play nicely with Markdown files. This was deemed more important, since we already use it for a README.md file in every repository, is much more popular than reStructured Text, and has simpler syntax.

Hosting the page through GitHub Pages and building through GitHub Actions mean there are no dedicated servers needed to be maintained by users. A fully open-source solution independent of a specific for-profit company would be preferred, but at least this can serve as introduction to contributing to other software outside of the University.

## License

Content in this documentation is licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)
