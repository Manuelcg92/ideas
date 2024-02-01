from .database import *

def create_db():
    """Método de creacion de la base de datos. """
    db.drop_all()
    db.create_all()
    
def init_db():
    """Método de inicializacion de nuestra base de datos. """
    create_db()
    #user admin
    admin = User(
        name="Manuel",
        lastname="Castro",
        username = "Manuelcg",
        email = "manuel.cg1992@gmail.com",
        is_admin = True,
        phone = "666666666"
    )
    # admin.set_password("123Admin")
    db.session.add(admin)
    db.session.commit()