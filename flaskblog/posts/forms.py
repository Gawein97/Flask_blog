from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField,  SelectField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=240)])
    content = TextAreaField('Content', validators=[DataRequired()])
    tags_choices = [('mindbox', 'Mindbox'), ('emails','Emails'), ('design', 'Design')]
    tags = SelectMultipleField('Tags', choices=tags_choices)
    submit = SubmitField('Post')
