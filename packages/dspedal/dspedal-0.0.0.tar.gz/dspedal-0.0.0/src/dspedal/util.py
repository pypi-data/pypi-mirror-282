import importlib.resources as pkg_resources
from . import templates
from string import Template


def load_template(template_name: str, **kwargs: dict[str, str]):
    """Load a template from the dspedal templates."""
    with pkg_resources.open_text(templates, template_name) as fp:
        t = Template(fp.read())
        return t.safe_substitute(**kwargs)
