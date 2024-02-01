
class Config:
    """Clase de configuracion de flask."""
    SECRET_KEY = 'ideas secretas'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../ideas'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


