"""404 page, served by Vercel for any unknown URL."""
from components import asset, link, rule
from pages import Page


def render():
    body = f'''<section class="sec"><div class="wrap not-found">
  <img src="{asset('img/crest-160.png')}" width="96" height="92" alt="">
  <span class="eyebrow">Page not found</span><h1>This page could not be found</h1>{rule(center=True)}
  <p class="lead">The link may be old or mistyped. Use the menu above, or go back to the home page.</p>
  <div class="btn-row"><a class="btn btn-primary" href="{link('home')}">Go to Home</a><a class="btn btn-ghost" href="{link('contact')}">Contact the school</a></div>
</div></section>'''
    return Page(
        key='home', file='404.html',
        title='Page Not Found | Al-Khair Academy',
        description='The page you are looking for could not be found.',
        body=body, nav='none', noindex=True,
    )
