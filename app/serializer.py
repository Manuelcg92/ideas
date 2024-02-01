from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .database import *


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: User
        fields = ('id','name','lastname','username','email','is_admin','phone', 'avatar')
class CategoryShema(SQLAlchemyAutoSchema):
    class Meta:
        model : Category
        fields = ('id','name')
        load_instance = True
        
class IdeaShema(SQLAlchemyAutoSchema):
    class Meta:
        model : Idea
        fields = ('id','title','description','is_public','category_id','category','user_id','user',)
        include_relationships = True
        load_instance = True