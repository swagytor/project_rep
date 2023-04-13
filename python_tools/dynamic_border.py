def dynamic_border(sentence):
    """Выводит уровни сложностей в рамках"""
    width = 22

    print('+-' + '-' * width + '-+')
    print('| {0:^{1}} |'.format(sentence, width))
    print('+-' + '-' * width + '-+')