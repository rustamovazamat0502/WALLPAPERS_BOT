from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def generate_categories(categories):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    buttons = []

    for category in categories:
        btn = KeyboardButton(text=category[0])
        buttons.append(btn)


    markup.add(*buttons)
    return markup


def download_buttons(image_id):
    markup = InlineKeyboardMarkup()
    download_d = InlineKeyboardButton(text='Download Desktop',
                                    callback_data=f'downloadd_{image_id}')
    download_m = InlineKeyboardButton(text='Download Mobile',
                                      callback_data=f'downloadm_{image_id}')
    markup.add(download_d, download_m)
    return markup