import os


def get_templates_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception("File path is invalid %s" % (file_path))
    return file_path


def get_templates(path):
    file_path = get_templates_path(path)
    return open(file_path).read()


def render_context(templates_string, context):
    return templates_string.format(**context)


file_ = "templates/email_templates.txt"
templates = get_templates(file_)
print templates
context = {
    "name": "divya",
    "date": None,
    "amount": None
}

print render_context(templates, context)
