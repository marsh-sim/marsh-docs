# Documentation

Documentation for all projects under MARSH-Sim.

All sources for these pages are in a [GitHub repository](https://github.com/marsh-sim/marsh-sim.github.io). It is set up to automatically build the documentation on every commit on GitHub servers. The public version at [marsh-sim.github.io](https://marsh-sim.github.io/) is updated every time the `main` branch is changed, the actual files served are from `gh-pages`.

## Local installation

The pages can be built into HTML and other formats using Python. A virtual environment is recommended to avoid mixing this documentation with system packages.

Unlike many Sphinx tutorials online, **the files are not in the `docs/` folder**. The following commands can be used for Linux:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sphinx-build source build
```

For users on Windows, only the line to activate the virtual environment changes to:

```
./venv/Scripts/activate
```

## Usage

Once a local installation is complete, the pages can be re-built with:

```
sphinx-build source build
```

### Optional: preview on save

This setup for Linux is only included because it is convenient, but running the command by hand will give the same results.

Using the [entr program](https://github.com/eradman/entr), the following command can be used to automatically rebuild the documents on every change. You may need to press `Ctrl+C` twice in quick succession to exit both the running program and the loop.

```bash
while sleep 0.1; do ls **/*.md **/*.rst | entr -s 'sphinx-build source build'; done
```

The page can be hosted locally with [Live Server extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer), which will reload the page when the HTML files change.

## Contributing

Content is written in Markdown, only using reStructured Text when special Sphinx directives are necessary. Markdown files should preferably be formatted with [Prettier](https://prettier.io/), conveniently available as an [extension for VS Code](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode).

### Recommended resources

- [Make a Readme](https://www.makeareadme.com/)
- [Readme Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html)
- [More Software Projects need Defenses of Design](https://buttondown.email/hillelwayne/archive/more-software-projects-need-defenses-of-design/)

### Defense of Design

The goal for this setup of the documentation was to make it simple to update to users who come from aerospace engineering background and may not be familiar with the web technologies at large. A single documentation for all related projects was chosen to simplify navigation, allow easier cross linking between different concepts, and make it easier to search.

The web pages are generated with Sphinx, because it is the most popular option for Python which most colleagues already know. The alternatives used by related projects like GitBook (for MAVLink Dev Guide) are not free anymore, and VuePress (for PX4) requires NodeJS. Even though Sphinx was chosen, Markdown should be used for content, since we already use it for a README.md file in every repository, is much more popular, and has simpler syntax.

Hosting the page through GitHub Pages and building through GitHub Actions mean there are no dedicated servers needed to be maintained by users. A fully open-source solution independent of a specific for-profit company would be preferred, but at least this can serve as introduction to contributing to other software outside of the University.

## License

Content in this documentation is licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)
