"""MkDocs build hook that fills in the current year in the copyright notice.

Keep the `{year}` placeholder in the `copyright` setting in mkdocs.yml
(e.g. "Copyright &copy; {year} TAK.NZ") and this hook will substitute it
with the current year on every build, so the footer never goes stale.
"""

from datetime import datetime, timezone


def on_config(config, **kwargs):
    if config.copyright:
        config.copyright = config.copyright.format(year=datetime.now(timezone.utc).year)
    return config
