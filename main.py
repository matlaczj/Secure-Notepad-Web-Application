from website import create_app
from bleach import clean
from markupsafe import Markup

app = create_app()

def do_clean(text, **kw):
    """Perform clean and return a Markup object to mark the string as safe.
    This prevents Jinja from re-escaping the result.
    Example use in template.
    <p>{{ my_variable|clean(tags=['img', 'b', 'i', 'em', 'strong'], attributes={'img': ['src', 'alt', 'title', 'width', 'height']}) }}</p>
    """
    return Markup(clean(text, **kw))

app.jinja_env.filters['clean'] = do_clean

if __name__ == '__main__':
    app.run(debug=True)
