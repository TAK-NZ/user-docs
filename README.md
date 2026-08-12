# TAK.NZ Documentation

This repository contains the source files for the [TAK.NZ](https://tak.nz) documentation, published at [docs.tak.nz](https://docs.tak.nz).

The site is built using [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

## Getting Started

To run the documentation server locally, you will need Python installed on your machine.

### Installation

It is generally a good idea to set up a virtual environment for the project dependencies, though you can install them globally if you prefer.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running the Development Server

Start the local development server with:

```bash
mkdocs serve
```

This spins up a server at `http://127.0.0.1:8000`. The server supports hot-reloading, so any changes you save to the markdown files automatically refresh the page in your browser.

## Editing Documentation

All documentation content is located in the `docs/` directory as standard Markdown files.

If you add a new page, update the `nav` section in `mkdocs.yml` so it appears in the site navigation.

### Project Structure

- `mkdocs.yml` - main configuration file for the site
- `requirements.txt` - Python dependencies for the docs site, including MkDocs plugins
- `docs/` - markdown source files
- `docs/assets/` - images, logos, and custom stylesheets
- `.github/workflows/` - CI build check and GitHub Pages deployment

## Building the Site

To generate the static HTML files for deployment:

```bash
mkdocs build
```

The output is generated in the `site/` directory.

## Deployment

Pushes to `main` automatically build and deploy the site to GitHub Pages via [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml), publishing to the custom domain configured in [`CNAME`](CNAME) (`docs.tak.nz`).

Pull requests are validated with a strict build check via [`.github/workflows/pr-preview.yml`](.github/workflows/pr-preview.yml).

## License

TAK.NZ is distributed under AGPL-3.0-only. See [LICENSE](LICENSE) for details.
