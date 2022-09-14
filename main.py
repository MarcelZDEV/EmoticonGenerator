import secrets

eyes = [';', ':', '=']
nose = ['-', '¬']
mouth = [')', '(', '|', '\\', '/', '}', '{', ']', '[']


def create_emoticon(list_eyes, list_nose, list_mouth):
    choice_eyes = secrets.choice(list_eyes)
    choice_nose = secrets.choice(list_nose)
    choice_mouth = secrets.choice(list_mouth)
    print(choice_eyes + choice_nose + choice_mouth)
    return 0


if __name__ == '__main__':
    create_emoticon(eyes, nose, mouth)
