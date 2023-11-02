from datetime import datetime

from flask import jsonify, abort, request, render_template

from back.resume.models import generate_uuid, Category, Author, \
    Book, Item, Course, Question, Roadmap, Status, SubItem, User, Video, Test

from back.app import db, app



@app.route('/v1/', methods=['GET'])
def health():
    obj = ["new", "old"]
    return render_template('index.html', objects=obj)


@app.route('/books/', methods=['GET'])
def read_all_books():
    books = Book.query.all()
    return jsonify(books)


@app.route('/book/<id_book>/', methods=['GET'])
def read_book(id_book):
    book = Book.query.filter(Book.id == id_book).one_or_none()
    if book:
        return jsonify(book)
    else:
        abort(404, f'Author with ID {id_book} not found')


@app.route('/book/create/', methods=['POST'])
def create_book():
    name = request.args.get("name")
    author = request.args.get("author")
    category = request.args.get("category")
    link = request.args.get('link') or None
    page_count = request.args.get('page_count') or 0
    version = request.args.get('version') or None
    date_publish = request.args.get('date_publish') or None
    if all([value is not None for value in [name, author, category]]):
        book = Book(id=generate_uuid(), name=name, author=author,
                    category=category, link=link, page_count=int(page_count),
                    version=version,
                    date_publish=date_publish)
        db.session.add(book)
        db.session.commit()
        return jsonify(book)
    else:
        abort(404, f'Cannot create book without name and author and category')


@app.route('/book/update/<id_obj>/', methods=['PUT'])
def update_book(id_obj):
    name = request.args.get('name')
    author = request.args.get("author")
    category = request.args.get("category")
    link = request.args.get("link")
    page_count = request.args.get("page_count")
    version = request.args.get("version")
    date_publish = request.args.get("date_publish")
    data = {'name': name, 'author': author, 'category': category, 'link': link,
            'page_count': page_count, 'version': version,
            'date_publish': date_publish}
    book = Book.query.filter(Book.id == id_obj).one_or_none()
    if book:
        for key, value in data.items():
            if value:
                setattr(book, key, value)
        db.session.commit()
        return jsonify(book)
    else:
        abort(404, 'Not found object')


@app.route('/book/delete/<id_obj>/', methods=['DELETE'])
def delete_book(id_obj):
    book = Book.query.filter(Book.id == id_obj).one_or_none()
    db.session.delete(book)
    db.session.commit()
    return f'You success delete a book with ID:{id_obj}'


@app.route('/authors/', methods=['GET'])
def read_all_authors():
    authors = Author.query.all()
    return jsonify(authors)


@app.route('/author/<id_author>/', methods=['GET'])
def read_author(id_author):
    author = Author.query.filter(Author.id == id_author).one_or_none()
    if author:
        return jsonify(author)
    else:
        abort(404, f'Author with ID {id_author} not found')


@app.route('/author/create/', methods=['POST'])
def create_author():
    name = request.args.get("name")
    surname = request.args.get("surname")
    topic = request.args.get("topic") or None
    website = request.args.get('website') or None
    country = request.args.get('country') or None
    if all([value is not None for value in [name, surname]]):
        author = Author(id=generate_uuid(), name=name, surname=surname,
                        topic=topic, website=website, country=country)
        db.session.add(author)
        db.session.commit()
        return jsonify(author)
    else:
        abort(404,
              f'Cannot create Author without name and surname and category')


@app.route('/author/update/<id_obj>/', methods=['PUT'])
def update_author(id_obj):
    name = request.args.get("name")
    surname = request.args.get("surname")
    topic = request.args.get("topic") or None
    website = request.args.get('website') or None
    country = request.args.get('country') or None
    data = {'name': name, 'surname': surname, 'topic': topic,
            'website': website,
            'country': country}
    author = Author.query.filter(Author.id == id_obj).one_or_none()
    if author:
        for key, value in data.items():
            if value:
                setattr(author, key, value)
        db.session.commit()
        return jsonify(author)
    else:
        abort(404, 'Not found object')


@app.route('/author/delete/<id_obj>/', methods=['DELETE'])
def delete_author(id_obj):
    author = Author.query.filter(Author.id == id_obj).one_or_none()
    db.session.delete(author)
    db.session.commit()
    return f'You success delete a author with ID:{id_obj}'


@app.route('/items/', methods=['GET'])
def get_all_items():
    items = Item.query.all()
    return jsonify(items)


@app.route('/item/<id_item>/', methods=['GET'])
def get_item(id_item):
    item = Item.query.filter(Item.id == id_item).one_or_none()
    if item:
        return jsonify(item)
    else:
        abort(404, f'Author with ID {id_item} not found')


@app.route('/item/create/', methods=['POST'])
def create_item():
    name = request.args.get("name")
    title = request.args.get("title")
    description = request.args.get("description")
    deadline = request.args.get('deadline')
    category = request.args.get('category')
    assignee = request.args.get('assignee')
    status = request.args.get('status')
    name_file = request.args.get('name_file') or None
    attachments = request.args.get('attachments') or None
    tag = request.args.get('tag') or None
    if all([value is not None for value in [name, title, description,
                                            deadline, category, assignee]]):
        item = Item(id=generate_uuid(), name=name, title=title,
                    description=description, deadline=deadline,
                    category=category, assignee=assignee, status=status,
                    name_file=name_file, attachments=attachments, tag=tag)
        db.session.add(item)
        db.session.commit()
        return jsonify(item)
    else:
        abort(404,
              f'Cannot create Author without name and surname and category')


@app.route('/item/update/<id_obj>/', methods=['PUT'])
def update_item(id_obj):
    name = request.args.get("name")
    title = request.args.get("title")
    description = request.args.get("description")
    deadline = request.args.get('deadline')
    category = request.args.get('category')
    assignee = request.args.get('assignee')
    status = request.args.get('status')
    name_file = request.args.get('name_file') or None
    attachments = request.args.get('attachments') or None
    tag = request.args.get('tag') or None
    data = {'name': name, 'title': title, 'description': description,
            'deadline': deadline, 'category': category, 'assignee': assignee,
            'status': status, 'name_file': name_file,
            'attachments': attachments, 'tag': tag}
    item = Item.query.filter(Item.id == id_obj).one_or_none()
    if item:
        for key, value in data.items():
            if value:
                setattr(item, key, value)
        db.session.commit()
        return jsonify(item)
    else:
        abort(404, f'Not found object of this ID:{id_obj}')


@app.route('/item/delete/<id_obj>/', methods=['DELETE'])
def delete_item(id_obj):
    item = Item.query.filter(Item.id == id_obj).one_or_none()
    db.session.delete(item)
    db.session.commit()
    return f'You success delete a item with ID:{id_obj}'


@app.route('/courses/', methods=['GET'])
def get_all_course():
    course = Course.query.all()
    return jsonify(course)


@app.route('/course/<id_item>/', methods=['GET'])
def get_course(id_item):
    course = Course.query.filter(Course.id == id_item).one_or_none()
    if course:
        return jsonify(course)
    else:
        abort(404, f'Course with ID {id_item} not found')


@app.route('/course/create/', methods=['POST'])
def create_course():
    name = request.args.get("name")
    category = request.args.get('category')
    author = request.args.get('author')
    link = request.args.get('link') or None
    topic = request.args.get('topic') or None
    if all([value is not None for value in [name, category, author]]):
        course = Course(id=generate_uuid(), name=name, category=category,
                        link=link, author=author, topic=topic)
        db.session.add(course)
        db.session.commit()
        return jsonify(course)
    else:
        abort(404,
              f'Cannot create Course without name and category and author')


@app.route('/course/update/<id_obj>/', methods=['PUT'])
def update_course(id_obj):
    name = request.args.get("name")
    category = request.args.get('category')
    author = request.args.get('author')
    link = request.args.get('link') or None
    topic = request.args.get('topic') or None
    data = {'name': name, 'category': category, 'author': author,
            'link': link, 'topic': topic}
    course = Course.query.filter(Course.id == id_obj).one_or_none()
    if course:
        for key, value in data.items():
            if value:
                setattr(course, key, value)
        db.session.commit()
        return jsonify(course)
    else:
        abort(404, f'Not found object of this ID:{id_obj}')


@app.route('/course/delete/<id_obj>/', methods=['DELETE'])
def delete_course(id_obj):
    course = Course.query.filter(Course.id == id_obj).one_or_none()
    if course:
        db.session.delete(course)
        db.session.commit()
        return 'You success delete course'
    return abort(404, 'NOt find a course')


@app.route('/category/', methods=['GET'])
def get_all_category():
    category = Category.query.all()
    return jsonify(category)


@app.route('/category/<id_item>/', methods=['GET'])
def get_category(id_item):
    category = Category.query.filter(Category.id == id_item).one_or_none()
    if category:
        return jsonify(category)
    else:
        abort(404, f'Category with ID {id_item} not found')


@app.route('/category/create/', methods=['POST'])
def create_category():
    name = request.args.get("name")
    if name is not None:
        category = Category(id=generate_uuid(), name=name)
        db.session.add(category)
        db.session.commit()
        return jsonify(category)
    else:
        abort(404,
              f'Cannot create Category without name and category and author')


@app.route('/category/update/<id_obj>/', methods=['PUT'])
def update_category(id_obj):
    name = request.args.get("name")
    data = {'name': name}
    category = Category.query.filter(Category.id == id_obj).one_or_none()
    if category:
        for key, value in data.items():
            if value:
                setattr(category, key, value)
        db.session.commit()
        return jsonify(category)
    else:
        abort(404, f'Not found object of this ID:{id_obj}')


@app.route('/category/delete/<id_obj>/', methods=['DELETE'])
def delete_category(id_obj):
    category = Category.query.filter(Category.id == id_obj).one_or_none()
    db.session.delete(category)
    db.session.commit()
    return f'You success delete a category with ID:{id_obj}'


@app.route('/questions/', methods=['GET'])
def get_all_questions():
    question = Question.query.all()
    return jsonify(question)


@app.route('/question/<id_item>/', methods=['GET'])
def get_question(id_item):
    question = Question.query.filter(Question.id == id_item).one_or_none()
    if question:
        return jsonify(question)
    else:
        abort(404, f'Question with ID {id_item} not found')


@app.route('/question/create/', methods=['POST'])
def create_question():
    name = request.args.get("name")
    tag = request.args.get('tag')
    number_of_fails = request.args.get('number_of_fails')
    number_of_usages = request.args.get("number_of_usages")
    if all([value is not None for value in [name, tag]]):
        question = Question(id=generate_uuid(), name=name, tag=tag,
                            number_of_fails=number_of_fails,
                            number_of_usages=number_of_usages)
        db.session.add(question)
        db.session.commit()
        return jsonify(question)
    else:
        abort(404,
              f'Cannot create Question without name and category and author')


@app.route('/question/update/<id_obj>/', methods=['PUT'])
def update_question(id_obj):
    name = request.args.get("name")
    tag = request.args.get('tag')
    number_of_fails = request.args.get('number_of_fails')
    number_of_usages = request.args.get("number_of_usages")
    data = {'name': name, 'tag': tag, 'number_of_fails': number_of_fails,
            'number_of_usage': number_of_usages}
    question = Question.query.filter(Question.id == id_obj).one_or_none()
    if question:
        for key, value in data.items():
            if value:
                setattr(question, key, value)
        db.session.commit()
        return jsonify(question)
    else:
        abort(404, f'Not found Question object of this ID:{id_obj}')


@app.route('/question/delete/<id_obj>/', methods=['DELETE'])
def delete_question(id_obj):
    question = Question.query.filter(Question.id == id_obj).one_or_none()
    db.session.delete(question)
    db.session.commit()
    return None


@app.route('/roadmap/', methods=['GET'])
def get_all_roadmap():
    roadmap = Roadmap.query.all()
    return jsonify(roadmap)


@app.route('/roadmap/<id_item>/', methods=['GET'])
def get_roadmap(id_item):
    roadmap = Roadmap.query.filter(Roadmap.id == id_item).one_or_none()
    if roadmap:
        return jsonify(roadmap)
    else:
        abort(404, f'Roadmap with ID {id_item} not found')


@app.route('/roadmap/create/', methods=['POST'])
def create_roadmap():
    type_item = request.args.get("type_item")
    title = request.args.get("title")
    priority = request.args.get("priority")
    complexity = request.args.get("complexity")
    goal_completion = request.args.get("goal_completion")
    added = request.args.get("added")
    user_id = request.args.get("user_id")
    deadline = request.args.get("deadline") or None
    if all([value is not None for value in
            [type_item, title, priority, complexity,
             goal_completion, added, user_id]]):
        roadmap = Roadmap(id=generate_uuid(), type_item=type_item, title=title,
                          priority=priority, complexity=complexity,
                          goal_completion=datetime.strptime(goal_completion,
                                                            '%d.%m.%Y'),
                          added=added,
                          user_id=user_id, deadline=deadline)
        db.session.add(roadmap)
        db.session.commit()
        return jsonify(roadmap)
    else:
        abort(404,
              f'Cannot create Roadmap without name and category and author')


@app.route('/roadmap/update/<id_obj>/', methods=['PUT'])
def update_roadmap(id_obj):
    type_item = request.args.get("type_item")
    title = request.args.get("title")
    priority = request.args.get("priority")
    complexity = request.args.get("complexity")
    goal_completion = request.args.get("goal_completion")
    added = request.args.get("added")
    user_id = request.args.get("user_id")
    deadline = request.args.get("deadline") or None
    data = {'type_item': type_item, 'title': title, 'priority': priority,
            'complexity': complexity, 'goal_completion': goal_completion,
            'added': added, 'user_id': user_id, 'deadline': deadline}
    roadmap = Roadmap.query.filter(Roadmap.id == id_obj).one_or_none()
    if roadmap:
        for key, value in data.items():
            if value:
                setattr(roadmap, key, value)
        db.session.commit()
        return jsonify(roadmap)
    else:
        abort(404, f'Not found Roadmap object of this ID:{id_obj}')


@app.route('/roadmap/delete/<id_obj>/', methods=['DELETE'])
def delete_roadmap(id_obj):
    roadmap = Roadmap.query.filter(Roadmap.id == id_obj).one_or_none()
    db.session.delete(roadmap)
    db.session.commit()
    return None


@app.route('/status/', methods=['GET'])
def get_all_status():
    status = Status.query.all()
    return jsonify(status)


@app.route('/status/<id_item>/', methods=['GET'])
def get_status(id_item):
    status = Status.query.filter(Status.id == id_item).one_or_none()
    if status:
        return jsonify(status)
    else:
        abort(404, f'Status with ID {id_item} not found')


@app.route('/status/create/', methods=['POST'])
def create_status():
    name = request.args.get("name")
    if name is not None:
        status = Status(id=generate_uuid(), name=name)
        db.session.add(status)
        db.session.commit()
        return jsonify(status)
    else:
        abort(404,
              f'Cannot create Status without name')


@app.route('/status/update/<id_obj>/', methods=['PUT'])
def update_status(id_obj):
    name = request.args.get("name")
    data = {'name': name}
    status = Status.query.filter(Status.id == id_obj).one_or_none()
    if status:
        for key, value in data.items():
            if value:
                setattr(status, key, value)
        db.session.commit()
        return jsonify(status)
    else:
        abort(404, f'Not found Status object of this ID:{id_obj}')


@app.route('/status/delete/<id_obj>/', methods=['DELETE'])
def delete_status(id_obj):
    status = Status.query.filter(Status.id == id_obj).one_or_none()
    db.session.delete(status)
    db.session.commit()
    return None


@app.route('/subitems/', methods=['GET'])
def get_all_subitems():
    subitems = SubItem.query.all()
    return jsonify(subitems)


@app.route('/subitem/<id_item>/', methods=['GET'])
def get_subitem(id_item):
    subitem = SubItem.query.filter(SubItem.id == id_item).one_or_none()
    if subitem:
        return jsonify(subitem)
    else:
        abort(404, f'SubItem with ID {id_item} not found')


@app.route('/subitem/create/', methods=['POST'])
def create_subitem():
    name = request.args.get("name")
    title = request.args.get("title")
    description = request.args.get("description")
    id_item = request.args.get('id_item')
    deadline = request.args.get('deadline') or None
    opened_by = request.args.get('opened_by ') or None
    status = request.args.get('status') or None
    name_file = request.args.get('name_file') or None
    attachments = request.args.get('attachments') or None
    tag = request.args.get('tag') or None
    if all([value is not None for value in
            [name, title, description, id_item, name_file]]):
        subitem = SubItem(id=generate_uuid(), name=name, title=title,
                         description=description, id_item=id_item,
                         deadline=deadline, opened_by=opened_by, status=status,
                         name_file=name_file, attachments=attachments, tag=tag)
        db.session.add(subitem)
        db.session.commit()
        return jsonify(subitem)
    else:
        abort(404,
              f'Cannot create Subitem without name anhd title and description, id_item,'
              f'name_file')


@app.route('/status/update/<id_obj>/', methods=['PUT'])
def update_subitem(id_obj):
    name = request.args.get("name")
    title = request.args.get("title")
    description = request.args.get("description")
    id_item = request.args.get('id_item')
    deadline = request.args.get('deadline')
    opened_by = request.args.get('opened_by ')
    status = request.args.get('status')
    name_file = request.args.get('name_file') or None
    attachments = request.args.get('attachments') or None
    tag = request.args.get('tag') or None
    data = {'name': name, 'title': title, 'description': description, 'id_item':id_item,
            'deadline': deadline, 'opened_by': opened_by, 'status': status,
            'name_file': name_file, 'attachments': attachments, 'tag': tag}
    subitem = SubItem.query.filter(SubItem.id == id_obj).one_or_none()
    if subitem:
        for key, value in data.items():
            if value:
                setattr(subitem, key, value)
        db.session.commit()
        return jsonify(subitem)
    else:
        abort(404, f'Not found SubItem object of this ID:{id_obj}')


@app.route('/status/delete/<id_obj>/', methods=['DELETE'])
def delete_subitem(id_obj):
    subitem = SubItem.query.filter(SubItem.id == id_obj).one_or_none()
    db.session.delete(subitem)
    db.session.commit()
    return None


@app.route('/users/', methods=['GET'])
def get_all_user():
    users = User.query.all()
    return jsonify(users)


@app.route('/users/<id_obj>/', methods=['GET'])
def get_user(id_obj):
    user = User.query.filter(User.id == id_obj).one_or_none()
    if user:
        return jsonify(user)
    else:
        abort(404, f'User with ID {id_obj} not found')


@app.route('/users/create/', methods=['POST'])
def create_user():
    name = request.args.get("name")
    password = request.args.get("password")
    email = request.args.get("email")
    full_name = request.args.get("full_name")
    if all([value is not None for value in [name, password, email]]):
        user = User(id=generate_uuid(), name=name, password=password,
                    email=email, full_name=full_name)
        db.session.add(user)
        db.session.commit()
        return jsonify(user)
    else:
        abort(404,
              f'Cannot create User without name or password or email')


@app.route('/users/update/<id_obj>/', methods=['PUT'])
def update_user(id_obj):
    name = request.args.get("name")
    password = request.args.get("password")
    email = request.args.get("email")
    full_name = request.args.get("full_name")
    data = {'name': name, 'password': password, 'email': email,
            'full_name': full_name}
    user = User.query.filter(User.id == id_obj).one_or_none()
    if user:
        for key, value in data.items():
            if value:
                setattr(user, key, value)
        db.session.commit()
        return jsonify(user)
    else:
        abort(404, f'Not found User object of this ID:{id_obj}')


@app.route('/users/delete/<id_obj>/', methods=['DELETE'])
def delete_user(id_obj):
    user = User.query.filter(User.id == id_obj).one_or_none()
    db.session.delete(user)
    db.session.commit()
    return None


@app.route('/videos/', methods=['GET'])
def get_all_video():
    video = Video.query.all()
    return jsonify(video)


@app.route('/video/<id_obj>/', methods=['GET'])
def get_video(id_obj):
    video = User.query.filter(Video.id == id_obj).one_or_none()
    if video:
        return jsonify(video)
    else:
        abort(404, f'Video with ID {id_obj} not found')


@app.route('/video/create/', methods=['POST'])
def create_video():
    name = request.args.get("name")
    category = request.args.get("category")
    author = request.args.get('author')
    link = request.args.get("link")
    topic = request.args.get("topic")
    version = request.args.get("version")
    date_publication = request.args.get("date_publication")
    if all([value is not None for value in [name, category, author]]):
        video = Video(id=generate_uuid(), name=name, category=category,
                    author=author, link=link, topic=topic, version=version,
                      date_publication=date_publication)
        db.session.add(video)
        db.session.commit()
        return jsonify(video)
    else:
        abort(404,
              f'Cannot create video without name or password or email')


@app.route('/video/update/<id_obj>/', methods=['PUT'])
def update_video(id_obj):
    name = request.args.get("name")
    category = request.args.get("category")
    author = request.args.get('author')
    link = request.args.get("link")
    topic = request.args.get("topic")
    version = request.args.get("version")
    date_publication = request.args.get("date_publication")
    data = {'name': name, 'category': category, 'author': author,'link': link,
            'topic': topic, 'version': version, 'date_publication': date_publication}
    video = Video.query.filter(Video.id == id_obj).one_or_none()
    if video:
        for key, value in data.items():
            if value:
                setattr(video, key, value)
        db.session.commit()
        return jsonify(video)
    else:
        abort(404, f'Not found Video object of this ID:{id_obj}')


@app.route('/video/delete/<id_obj>/', methods=['DELETE'])
def delete_video(id_obj):
    video = Video.query.filter(Video.id == id_obj).one_or_none()
    db.session.delete(video)
    db.session.commit()
    return None
