from setuptools import find_packages, setup

extra = {}

try:
    import babel
    extractors = [
        ('**.py',                'python', None),
        ('**/templates/**.html', 'genshi', None),
        ('**/templates/**.js',   'javascript', None),
        ('**/templates/**.txt',  'genshi',
         {'template_class': 'genshi.template:NewTextTemplate'}),
    ]
    extra['message_extractors'] = {
        'ticketlog': extractors,
    }
except ImportError:
    pass

setup(
    name = 'TracTicketChangelogPlugin',
    version = "0.1",
    description = "Show changelogs in trac ticket",
    author = "Richard Liao",
    author_email = "richard.liao.i@gmmail.com",
    url = "http://trac-hacks.org/wiki/TracTicketChangelogPlugin",
    license = "BSD",
    packages = find_packages(exclude=['ez_setup', 'examples', 'tests*']),
    include_package_data = True,
    package_data = { 'ticketlog': [ '*.txt', 'templates/*.*', 'htdocs/*.*', 
        'tests/*.*', 'locale/*.*', 'locale/*/LC_MESSAGES/*.*' ] },
    zip_safe = False,
    keywords = "trac TracTicketChangelogPlugin",
    classifiers = [
        'Framework :: Trac',
    ],
    install_requires = [],
    entry_points = """
    [trac.plugins]
    ticketlog = ticketlog.web_ui
    """,
    **extra
    )

