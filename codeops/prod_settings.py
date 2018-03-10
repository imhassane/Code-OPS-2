from .settings import *

# Les hotes permis.
ALLOWED_HOSTS = ['code-ops.herokuapp.com']

# Debug à true
DEBUG = False

# Configuration de postgresql.
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Changement de la clé secrete.
SECRET_KEY = os.environ['SECRET_KEY']

# Ajout du middleware pour servir les fichiers en producton
MIDDLEWARE += [
'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Mise en cache des fichiers avec white noise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'