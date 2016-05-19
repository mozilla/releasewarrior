import os

REPO_PATH = os.path.abspath(os.path.join(os.path.realpath(__file__), '..', '..'))
TEMPLATES_PATH = os.path.join(REPO_PATH, 'templates')
RELEASES_PATH = os.path.join(REPO_PATH, 'releases')
ARCHIVED_RELEASES_PATH = os.path.join(REPO_PATH, 'releases', 'ARCHIVE')
POSTMORTEMS_PATH = os.path.join(REPO_PATH, 'releases', 'POSTMORTEMS')
LOG_PATH = os.path.join(REPO_PATH, 'logs')


WIKI_TEMPLATES = {
    'firefox': {
        'beta': os.path.join(TEMPLATES_PATH, 'firefox_beta.md.tmpl'),
        'release': os.path.join(TEMPLATES_PATH, 'firefox_release.md.tmpl'),
        'esr': os.path.join(TEMPLATES_PATH, 'firefox_esr.md.tmpl'),
    },
    'fennec': {
        'beta': os.path.join(TEMPLATES_PATH, 'fennec_beta.md.tmpl'),
        'release': os.path.join(TEMPLATES_PATH, 'fennec_release.md.tmpl'),
        'esr': os.path.join(TEMPLATES_PATH, 'fennec_esr.md.tmpl'),
    },
    'thunderbird': {
        'beta': os.path.join(TEMPLATES_PATH, 'thunderbird_beta.md.tmpl'),
        'release': os.path.join(TEMPLATES_PATH, 'thunderbird_release.md.tmpl'),
        'esr': os.path.join(TEMPLATES_PATH, 'thunderbird_esr.md.tmpl'),
    },
    "postmortem": os.path.join(TEMPLATES_PATH, 'postmortem.md.tmpl')
}

DATA_TEMPLATES = {
    'firefox': {
        'beta': os.path.join(TEMPLATES_PATH, 'firefox_beta.json.tmpl'),
        'release': os.path.join(TEMPLATES_PATH, 'firefox_release.json.tmpl'),
        'esr': os.path.join(TEMPLATES_PATH, 'firefox_esr.json.tmpl'),
    },
    'fennec': {
        'beta': os.path.join(TEMPLATES_PATH, 'fennec_beta.json.tmpl'),
        'release': os.path.join(TEMPLATES_PATH, 'fennec_release.json.tmpl'),
        'esr': os.path.join(TEMPLATES_PATH, 'fennec_esr.json.tmpl'),
    },
    'thunderbird': {
        'beta': os.path.join(TEMPLATES_PATH, 'thunderbird_beta.json.tmpl'),
        'release': os.path.join(TEMPLATES_PATH, 'thunderbird_release.json.tmpl'),
        'esr': os.path.join(TEMPLATES_PATH, 'thunderbird_esr.json.tmpl'),
    }
}

