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

## Contributing

`main` is protected — changes are made through pull requests, which require at least one approval and passing status checks before they can be merged. [`.github/workflows/pr-preview.yml`](.github/workflows/pr-preview.yml) runs on every PR and checks:

- **Workflow lint** — validates the GitHub Actions workflow files with [`actionlint`](https://github.com/rhysd/actionlint).
- **Strict MkDocs build** — `mkdocs build --strict` fails on broken nav references, and (via the [`htmlproofer`](https://github.com/manuzhang/mkdocs-htmlproofer-plugin) plugin) on broken internal links, anchors, or missing images in the rendered site.
- **External link check** — [`lychee`](https://github.com/lycheeverse/lychee-action) checks external links in the built site and reports broken ones in the job summary. This check is informational and does not block merging, since external sites can be flaky.

Use the PR template checklist as a guide, and update the `nav` section in `mkdocs.yml` whenever you add a new page.

## License

TAK.NZ is distributed under AGPL-3.0-only. See [LICENSE](LICENSE) for details.
