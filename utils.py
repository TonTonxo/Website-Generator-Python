# utils.py

from flask import render_template_string

def generate_user_template(link):
    template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ link.title }}'s Website</title>
    </head>
    <body>
        <h1>Welcome to {{ link.title }}'s Website!</h1>
        <p>{{ link.name }}: {{ link.bio }}</p>
        <a href="{{ link.url }}" target="_blank">Visit My Link</a>
    </body>
    </html>
    '''
    rendered_template = render_template_string(template, link=link)

    # Save the generated HTML template to a file (optional)
    with open(f'static/{link.title}_website.html', 'w') as file:
        file.write(rendered_template)
