from flask import Blueprint, render_template, url_for

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    image_file = url_for('static', filename=f'errors/404.jpg')
    return render_template('errors/404.html', image_file=image_file, sidebar_off=True), 404


@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html', sidebar_off=True), 403


@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html', sidebar_off=True), 500
