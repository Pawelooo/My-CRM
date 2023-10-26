from datetime import datetime

from flask import jsonify, abort, request

from back.resume.models import generate_uuid, Category, Author, \
    Book, Item, Course, Question, Roadmap, Status, SubItem, User, Video
from back.resume.models import db, app
from base.src.model.config import UPLOAD, LOCATION_FILES, CREATE, \
    FILE_BOOK_NAME, FILE_AUTHOR_NAME, FILE_ITEM, FILE_COURSE_NAME, \
    FILE_CATEGORY_NAME, FILE_QUESTION, FILE_ROADMAP, FILE_STATUS_NAME, \
    FILE_SUBITEM, FILE_USER_NAME, FILE_VIDEO_NAME, UPLOAD_OBJ, \
    FOLDER_IMAGES_FLASK, DELETE
from base.src.service.jfs import JsonFromService
from base.src.service.validators.author_validator import AuthorValidator

from base.src.service.validators.book_validator import BookValidator
from base.src.service.validators.category_validator import CategoryValidator
from base.src.service.validators.course_validator import CourseValidator
from base.src.service.validators.item_validator import ItemValidator
from base.src.service.validators.question_validator import QuestionValidator
from base.src.service.validators.roadmap_validator import RoadmapValidator
from base.src.service.validators.status_validator import StatusValidator
from base.src.service.validators.subitem_validator import SubItemValidator
from base.src.service.validators.user_validator import UserValidator
from base.src.service.validators.video_validator import VideoValidator

book_validator = BookValidator()

jfs = JsonFromService()


@app.route('/images/', methods=['POST'])
def upload_images():
    image = request.files['files']
    jfs.save_image(image)
    jfs.compress(FOLDER_IMAGES_FLASK)
    return f'Image was save {image.filename}'


@app.route('/books/gets/', methods=['GET'])
def get_file_to_book():
    return jfs.get_object(FILE_BOOK_NAME)


@app.route('/books/', methods=['GET'])
def read_all_books():
    books = Book.query.all()
    return jsonify(books)


@app.route('/book/upload/<name_file>/', methods=['POST'])
def send_files_to_book(name_file: str):
    res = jfs.add_file(name_file, UPLOAD, LOCATION_FILES)
    if isinstance(res, int):
        return {'status code': res}
    return res


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
    id_obj = generate_uuid()
    book_validator = BookValidator().validate({'name': name, 'author': author,
                                               'category': category,
                                               'link': link,
                                               'page_count': page_count,
                                               'version': version,
                                               'date_publish': date_publish,
                                               'id': id_obj}, CREATE)
    if not book_validator:
        abort(404, f'Cannot create book without name and author and category')

    book = Book(id=id_obj, name=name, author=author,
                category=category, link=link, page_count=int(page_count),
                version=version,
                date_publish=date_publish)
    db.session.add(book)
    db.session.commit()
    return jsonify(book)


# TODO Metoda pakowanie do mniesjzego foramtowania plików(obrazów po przez funkcje wczesniejszą)


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
            'date_publish': date_publish, 'id': id_obj}
    book_validator = BookValidator().validate(data, UPLOAD_OBJ)
    if not book_validator:
        abort(404, f'Cannot update book without name and author and category')
    book = Book.query.filter(Book.id == id_obj).one_or_none()
    if book:
        for key, value in data.items():
            if value:
                setattr(book, key, value)
        db.session.commit()
        return jsonify(book)
    else:
        abort(404, f'Not found object of this ID{id_obj}')


@app.route('/book/delete/<id_obj>/', methods=['DELETE'])
def delete_book(id_obj):
    book = Book.query.filter(Book.id == id_obj).one_or_none()
    if book:
        db.session.delete(book)
        db.session.commit()
    else:
        abort(404, 'Not found Book object of this ID')
    return f'You success delete a book with ID:{id_obj}'


@app.route('/authors/gets/', methods=['GET'])
def get_file_to_authors():
    return jfs.get_object(FILE_AUTHOR_NAME)


@app.route('/authors/upload/', methods=['POST'])
def send_files_to_author():
    res = jfs.add_file(FILE_AUTHOR_NAME, UPLOAD, LOCATION_FILES)
    if isinstance(res, int):
        return {'status code': res}
    return res


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
    id_obj = generate_uuid()
    author_validator = AuthorValidator().validate(
        {'name': name, 'surname': surname,
         'topic': topic, 'website': website,
         'country': country, 'id': id_obj},
        CREATE)
    if not author_validator:
        abort(404, f'Cannot create author without name and surname !')
    author = Author(id=id_obj, name=name, surname=surname,
                    topic=topic, website=website, country=country)
    db.session.add(author)
    db.session.commit()
    return jsonify(author)


@app.route('/author/update/<id_obj>/', methods=['PUT'])
def update_author(id_obj):
    name = request.args.get("name")
    surname = request.args.get("surname")
    topic = request.args.get("topic") or None
    website = request.args.get('website') or None
    country = request.args.get('country') or None
    data = {'name': name, 'surname': surname, 'topic': topic,
            'website': website, 'country': country, 'id': id_obj}
    author_validator = AuthorValidator().validate(data, UPLOAD_OBJ)
    if not author_validator:
        abort(404, f'Cannot update author without name and surname')
    author = Author.query.filter(Author.id == id_obj).one_or_none()
    if author:
        for key, value in data.items():
            if value:
                setattr(author, key, value)
        db.session.commit()
        return jsonify(author)
    else:
        abort(404, f'Not found object  of this ID:{id_obj}')


@app.route('/author/delete/<id_obj>/', methods=['DELETE'])
def delete_author(id_obj):
    author = Author.query.filter(Author.id == id_obj).one_or_none()
    author_validation = AuthorValidator().validate(author.__repr__(), DELETE)
    if author_validation:
        db.session.delete(author)
        db.session.commit()
        return f'You success delete a author with ID:{id_obj}'
    return abort(404, 'You cannot delete this author')


@app.route('/items/gets/', methods=['GET'])
def get_file_to_items():
    return jfs.get_object(FILE_ITEM)


@app.route('/items/upload/<name_file>/', methods=['POST'])
def send_files_to_items(name_file: str):
    res = jfs.add_file(name_file, UPLOAD, LOCATION_FILES)
    if isinstance(res, int):
        return {'status code': res}
    return res


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
    id_obj = generate_uuid()
    item_validator = ItemValidator().validate({'name': name, 'title': title,
                                               'description': description,
                                               'deadline': deadline,
                                               'category': category,
                                               'assignee': assignee,
                                               'status': status,
                                               'name_file': name_file,
                                               'attachments': attachments,
                                               "tag": tag,
                                               'id': id_obj}, CREATE)
    if not item_validator:
        abort(404,
              f'Cannot create item without name, title, description, deadline, assignee and id !')
    item = Item(id=id_obj, name=name, title=title,
                description=description, deadline=deadline,
                category=category, assignee=assignee, status=status,
                name_file=name_file, attachments=attachments, tag=tag)
    db.session.add(item)
    db.session.commit()
    return jsonify(item)


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
    item_validator = ItemValidator().validate(data, UPLOAD_OBJ)
    if not item_validator:
        abort(404, f'Cannot update item without name, title, description, '
                   f'deadline, assignee and id ')
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
    item_validation = AuthorValidator().validate(item.__repr__(), DELETE)
    if item_validation:
        db.session.delete(item)
        db.session.commit()
        return f'You success delete a item with ID:{id_obj}'
    return 'You cannot delete this item'


@app.route('/courses/gets/', methods=['GET'])
def get_file_to_courses():
    return jfs.get_object(FILE_COURSE_NAME)


@app.route('/courses/upload/<name_file>/', methods=['POST'])
def send_file_to_courses(name_file: str):
    res = jfs.add_file(name_file, UPLOAD, LOCATION_FILES)
    if isinstance(res, int):
        return {'status code': res}
    return res


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
    id_obj = generate_uuid()
    data = {'name': name, 'category': category, 'author': author,
            'link': link, 'topic': topic, 'id': id_obj}
    course_validator = CourseValidator().validate(data, CREATE)
    if not course_validator:
        abort(404, f'Cannot create Course without name and category and author !')
    course = Course(id=id_obj, name=name, category=category,
                    link=link, author=author, topic=topic)
    db.session.add(course)
    db.session.commit()
    return jsonify(course)


@app.route('/course/update/<id_obj>/', methods=['PUT'])
def update_course(id_obj):
    name = request.args.get("name")
    category = request.args.get('category')
    author = request.args.get('author')
    link = request.args.get('link') or None
    topic = request.args.get('topic') or None
    data = {'name': name, 'category': category, 'author': author,
            'link': link, 'topic': topic}
    course_validator = CourseValidator().validate(data, UPLOAD_OBJ)
    if not course_validator:
        abort(404, f'Cannot update course without name and category and author ')
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
    course_validation = AuthorValidator().validate(course.__repr__(), DELETE)
    if course_validation:
        db.session.delete(course)
        db.session.commit()
        return f'You success delete a course with ID:{id_obj}'
    return abort(404, 'You cannot delete this course')


@app.route('/category/gets/', methods=['GET'])
def get_file_to_category():
    return jfs.get_object(FILE_CATEGORY_NAME)


@app.route('/category/upload/<name_file>/', methods=['POST'])
def send_files_to_category(name_file: str):
    res = jfs.add_file(name_file, UPLOAD, LOCATION_FILES)
    if isinstance(res, int):
        return {'status code': res}
    return res


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
    id_obj = generate_uuid()
    category_validator = CategoryValidator().validate({'name': name, 'id': id_obj}, CREATE)
    if not category_validator:
        abort(404, f'Cannot create category without name!')
    category = Category(id=generate_uuid(), name=name)
    db.session.add(category)
    db.session.commit()
    return jsonify(category)


@app.route('/category/update/<id_obj>/', methods=['PUT'])
def update_category(id_obj):
    name = request.args.get("name")
    data = {'name': name, 'id': id_obj}
    category_validator = CategoryValidator().validate(data, UPLOAD_OBJ)
    if not category_validator:
        abort(404, f'Cannot update author without name and surname')
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
    category_validation = CategoryValidator().validate(category.__repr__(), DELETE)
    if category_validation:
        db.session.delete(category)
        db.session.commit()
        return f'You success delete a category with ID:{id_obj}'
    return abort(404, 'You cannot delete this category')


@app.route('/questions/gets/', methods=['GET'])
def get_file_to_questions():
    return jfs.get_object(FILE_QUESTION)


@app.route('/questions/upload/<name_file>/', methods=['POST'])
def send_files_to_questions(name_file: str):
    res = jfs.add_file(name_file, UPLOAD, LOCATION_FILES)
    if isinstance(res, int):
        return {'status code': res}
    return res


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
    number_of_fails = request.args.get('number_of_fails') or None
    number_of_usages = request.args.get("number_of_usages") or None
    id_obj = generate_uuid()
    data = {'name': name, 'tag': tag, 'number_of_fails': number_of_fails,
            'number_of_usage': number_of_usages, 'id': id_obj}
    question_validator = QuestionValidator().validate(data, CREATE)
    if not question_validator:
        abort(404, f'Cannot create question without name!')
    question = Question(id=generate_uuid(), name=name, tag=tag,
                        number_of_fails=number_of_fails,
                        number_of_usages=number_of_usages)
    db.session.add(question)
    db.session.commit()
    return jsonify(question)


@app.route('/question/update/<id_obj>/', methods=['PUT'])
def update_question(id_obj):
    name = request.args.get("name")
    tag = request.args.get('tag') or None
    number_of_fails = request.args.get('number_of_fails') or 0
    number_of_usages = request.args.get("number_of_usages") or 0
    data = {'name': name, 'tag': tag, 'number_of_fails': number_of_fails,
            'number_of_usage': number_of_usages, 'id': id_obj}
    question_validator = QuestionValidator().validate(data, UPLOAD_OBJ)
    if not question_validator:
        abort(404, f'Cannot update author without name and surname')
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
    question_validation = AuthorValidator().validate(question.__repr__(), DELETE)
    if question_validation:
        db.session.delete(question)
        db.session.commit()
        return f'You success delete a author with ID:{id_obj}'
    return abort(404, 'You cannot delete this question')


@app.route('/roadmap/gets/', methods=['GET'])
def get_file_to_roadmap():
    return jfs.get_object(FILE_ROADMAP)


@app.route('/roadmap/upload/<name_file>/', methods=['POST'])
def send_files_to_roadmap(name_file: str):
    res = jfs.add_file(name_file, UPLOAD, LOCATION_FILES)
    if isinstance(res, int):
        return {'status code': res}
    return res


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
    id_obj = generate_uuid()
    data = {'type_item': type_item, 'title': title, 'priority': priority,
            'complexity': complexity, 'goal_completion': goal_completion,
            'added': added, 'user_id': user_id, 'deadline': deadline, 'id': id_obj}
    roadmap_validator = RoadmapValidator().validate(data, CREATE)
    if not roadmap_validator:
        abort(404, f'Cannot create roadmap without type_item, title, priority'
                   f'complexity, goal_completion, added, user_id')


    roadmap = Roadmap(id=generate_uuid(), type_item=type_item, title=title,
                      priority=priority, complexity=complexity,
                      goal_completion=datetime.strptime(goal_completion,
                                                        '%d.%m.%Y'),
                      added=added,
                      user_id=user_id, deadline=deadline)
    db.session.add(roadmap)
    db.session.commit()
    return jsonify(roadmap)


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
            'added': added, 'user_id': user_id, 'deadline': deadline, 'id': id_obj}
    roadmap_validator = BookValidator().validate(data, UPLOAD_OBJ)
    if not roadmap_validator:
        abort(404, f'Cannot upadte roadmap without type_item, title, priority'
                   f'complexity, goal_completion, added, user_id')
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
    roadmap_validation = AuthorValidator().validate(roadmap.__repr__(), DELETE)
    if roadmap_validation:
        db.session.delete(roadmap)
        db.session.commit()
        return f'You success delete a author with ID:{id_obj}'
    return abort(404, 'You cannot delete this roadmap ')


@app.route('/status/gets/', methods=['GET'])
def get_file_to_status():
    return jfs.get_object(FILE_STATUS_NAME)


@app.route('/status/upload/<name_file>/', methods=['POST'])
def send_files_to_status(name_file: str):
    res = jfs.add_file(name_file, UPLOAD, LOCATION_FILES)
    if isinstance(res, int):
        return {'status code': res}
    return res


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
    id_obj = generate_uuid()
    data = {'name': name, 'id': id_obj}
    status_validator = StatusValidator().validate(data, CREATE)
    if not status_validator:
        abort(404, f'Cannot create status without name!')
    status = Status(id=generate_uuid(), name=name)
    db.session.add(status)
    db.session.commit()
    return jsonify(status)



@app.route('/status/update/<id_obj>/', methods=['PUT'])
def update_status(id_obj):
    name = request.args.get("name")
    data = {'name': name, 'id': id_obj}
    status_validator = StatusValidator().validate(data, UPLOAD_OBJ)
    if not status_validator:
        abort(404, f'Cannot update status without name!')
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
    status_validation = StatusValidator().validate(status.__repr__(), DELETE)
    if status_validation:
        db.session.delete(status)
        db.session.commit()
        return f'You success delete a status with ID:{id_obj}'
    return abort(404, 'You cannot delete this status ')


@app.route('/subitems/gets/', methods=['GET'])
def get_file_to_subitems():
    return jfs.get_object(FILE_SUBITEM)


@app.route('/subitems/upload/<name_file>/', methods=['POST'])
def send_files_to_subitems(name_file: str):
    res = jfs.add_file(name_file, UPLOAD, LOCATION_FILES)
    if isinstance(res, int):
        return {'status code': res}
    return res


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
    id_obj = generate_uuid()
    data = {'name': name, 'title': title, 'description': description,
            'id_item': id_item,
            'deadline': deadline, 'opened_by': opened_by, 'status': status,
            'name_file': name_file, 'attachments': attachments, 'tag': tag, 'id': id_obj}
    subitem_validator = QuestionValidator().validate(data, CREATE)
    if not subitem_validator:
        abort(404, f'Cannot create subitem without name!')
    subitem = SubItem(id=id_obj, name=name, title=title,
                      description=description, id_item=id_item,
                      deadline=deadline, opened_by=opened_by,
                      status=status,
                      name_file=name_file, attachments=attachments,
                      tag=tag)
    db.session.add(subitem)
    db.session.commit()
    return jsonify(subitem)



@app.route('/subitem/update/<id_obj>/', methods=['PUT'])
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
    data = {'name': name, 'title': title, 'description': description,
            'id_item': id_item,
            'deadline': deadline, 'opened_by': opened_by, 'status': status,
            'name_file': name_file, 'attachments': attachments, 'tag': tag,
            'id': id_obj}
    subitem_validator = SubItemValidator().validate(data, UPLOAD_OBJ)
    if not subitem_validator:
        abort(404, f'Cannot update subitem !')
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
    subitem_validation = StatusValidator().validate(subitem.__repr__(), DELETE)
    if subitem_validation:
        db.session.delete(subitem)
        db.session.commit()
        return f'You success delete a author with ID:{id_obj}'
    return abort(404, 'You cannot delete this roadmap ')


@app.route('/users/gets/', methods=['GET'])
def get_file_to_users():
    return jfs.get_object(FILE_USER_NAME)


@app.route('/users/upload/<name_file>/', methods=['POST'])
def send_files_to_users(name_file: str):
    res = jfs.add_file(name_file, UPLOAD, LOCATION_FILES)
    if isinstance(res, int):
        return {'status code': res}
    return res


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
    full_name = request.args.get("full_name") or None
    id_obj = generate_uuid()
    data = {'name': name, 'password': password, 'email': email,
            'full_name': full_name, 'id': id_obj}
    user_validator = UserValidator().validate(data, CREATE)
    if not user_validator:
        abort(404, f'Cannot create user without name, password and email!')
    user = User(id=id_obj, name=name, password=password,
                      email=email, full_name=full_name)
    db.session.add(user)
    db.session.commit()
    return jsonify(user)


@app.route('/users/update/<id_obj>/', methods=['PUT'])
def update_user(id_obj):
    name = request.args.get("name")
    password = request.args.get("password")
    email = request.args.get("email") or None
    full_name = request.args.get("full_name") or None
    data = {'name': name, 'password': password, 'email': email,
            'full_name': full_name, 'id': id_obj}
    user_validator = UserValidator().validate(data, UPLOAD_OBJ)
    if not user_validator:
        abort(404, f'Cannot update user without name or password or email!')
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
    user_validation = StatusValidator().validate(user.__repr__(), DELETE)
    if user_validation:
        db.session.delete(user)
        db.session.commit()
        return f'You success delete a user with ID:{id_obj}'
    return abort(404, 'You cannot delete this user ')


@app.route('/video/gets/', methods=['GET'])
def get_file_to_video():
    return jfs.get_object(FILE_VIDEO_NAME)


@app.route('/video/upload/<name_file>/', methods=['POST'])
def send_files_to_video(name_file: str):
    res = jfs.add_file(name_file, UPLOAD, LOCATION_FILES)
    if isinstance(res, int):
        return {'status code': res}
    return res


@app.route('/video/gets/', methods=['POST'])
def get_all_files_to_video(name_file: str):
    res = jfs.add_file(name_file, UPLOAD, LOCATION_FILES)
    if isinstance(res, int):
        return {'status code': res}
    return res


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
    link = request.args.get("link") or None
    topic = request.args.get("topic") or None
    version = request.args.get("version") or None
    date_publication = request.args.get("date_publication") or None
    id_obj = generate_uuid()
    data = {'name': name, 'category': category, 'author': author, 'link': link,
            'topic': topic, 'version': version,
            'date_publication': date_publication, 'id': id_obj}
    video_validator = VideoValidator().validate(data, CREATE)
    if not video_validator:
        abort(404, f'Cannot create user without name, password and email!')
    video = Video(id=id_obj, name=name, category=category,
                  author=author, link=link, topic=topic, version=version,
                  date_publication=date_publication)
    db.session.add(video)
    db.session.commit()
    return jsonify(video)



@app.route('/video/update/<id_obj>/', methods=['PUT'])
def update_video(id_obj):
    name = request.args.get("name")
    category = request.args.get("category")
    author = request.args.get('author')
    link = request.args.get("link")
    topic = request.args.get("topic")
    version = request.args.get("version")
    date_publication = request.args.get("date_publication")
    data = {'name': name, 'category': category, 'author': author, 'link': link,
            'topic': topic, 'version': version,
            'date_publication': date_publication}
    video_validator = VideoValidator().validate(data, UPLOAD_OBJ)
    if not video_validator:
        abort(404, f'Cannot update user without name, password and email!')
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
    video_validation = StatusValidator().validate(video.__repr__(), DELETE)
    if video_validation:
        db.session.delete(video)
        db.session.commit()
        return f'You success delete a video with ID:{id_obj}'
    return abort(404, 'You cannot delete this video ')

