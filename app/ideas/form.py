from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, HiddenField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length

class DeleteCategoryForm(FlaskForm):
    """Formulario para eliminar categorias. """
    submit = SubmitField("Eliminar")
    
class RegisterCategoryForm(FlaskForm):
    """Formulario para registrar categoria. """
    name = StringField("Categoría", validators = [DataRequired(), Length(min=2, max=15)])
    
    submit = SubmitField("Registrar")
    
class IdeaForm(FlaskForm):
    """Form de idea"""
    id = HiddenField()
    title = StringField("Título" , validators=[DataRequired(), Length(min=5,max=50)])
    description = StringField("Descripción" , validators=[DataRequired(), Length(min=10,max=150)])
    is_public = BooleanField("Ideas pública")
    category_id = SelectField("Categoría" , validators=[DataRequired()])
    
    submit = SubmitField("Enviar")
    
class DeleteIdeaForm(FlaskForm):
    """Form para eliminar idea"""
    submit = SubmitField("")
    
class PublicIdeaForm(FlaskForm):
    """Form para cambiar el estado de la idea"""
    submit = SubmitField("")
    