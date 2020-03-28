from flask import Blueprint, render_template, url_for, flash, redirect, request, abort, current_app
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post, Tag
from flaskblog.posts.forms import PostForm


posts = Blueprint('posts', __name__)


def create_tags(tags:list):
    result = []
    for tag_name in tags:
        existing_check = Tag.query.filter_by(name=tag_name).first()
        if not existing_check:
            create_tag = Tag(name=tag_name)
            db.session.add(create_tag)
            db.session.commit()
            select_tag = Tag.query.filter_by(name=tag_name).first()
            result.append(select_tag)
        else:
            result.append(existing_check)
    return result

@posts.route('/post/new', methods=['POST', 'GET'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        current_app.logger.info(f'{form.tags.data}')
        tags = create_tags(form.tags.data)
        post = Post(title=form.title.data, content=form.content.data, author=current_user, tags=tags)
        db.session.add(post)
        db.session.commit()
        flash('Post has been created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route('/post/<int:post_id>/update', methods=['POST', 'GET'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted!', 'success')
    return redirect(url_for('main.home'))
