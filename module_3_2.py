def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not all(['@' in recipient and
                '@' in sender,
                recipient.endswith('.ru') or
                recipient.endswith('.com') or
                recipient.endswith('.net'),
                sender.endswith('.ru') or
                sender.endswith('.com') or
                sender.endswith('.net')]):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
