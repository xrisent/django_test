def article_validate(title, author, content):
    errors = {}
    if not title:
        errors['title'] = 'required field'
    elif len(title) < 5:
        errors['title'] = 'must be more than 5 symbols'
    if not author:
        errors['author'] = 'required field'
    elif len(author) < 5:
        errors['author'] = 'must be more than 5 symbols'
    if not content:
        errors['content'] = 'required field'
    elif len(content) < 10:
        errors['content'] = 'must be more than 10 symbols'
    return errors