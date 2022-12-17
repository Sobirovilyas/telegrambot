import telebot
import sqlite3
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
TOKEN = "5780017391:AAGLwwKWCqW3-RTxXrggk3Wq_sV8hk_s3gk"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=["start"])
def greetings(message):
    reply = 'привет. я бот который собирает информацию'
    bot.reply_to(message, reply, reply_markup=keyboard())






is_taking_name= False
is_taking_surname = False
name=None
surname=None
@bot.message_handler(content_types=["text"])
def message_handler(message):
    chat_id = message.chat.id
    global is_taking_name
    global is_taking_surname
    global name
    global surname





    if is_taking_surname == True:
        surname = message.text
        print(surname)
        print("thank you")
        is_taking_surname = False
        save_data_to_db(name, surname)



    if is_taking_name:
        name = message.text
        print(name)
        is_taking_name = False
        is_taking_surname = True
        bot.send_message(chat_id, "Input ur surname:")




    if message.text == 'save name':
        is_taking_name = True
        bot.send_message(chat_id, "input ur name:")



    if message.text == '/show_data':

            data = read_date_from_db()
            for datum in data:
                bot.reply_to(message, str(datum))


def save_data_to_db(name, surname):
#название нашего файла из база данных

    connection = None

    try:

#название нашего файла из база данных
        connection = sqlite3.Connection("date base")
        cursor = connection.cursor()
        insert_sql = f"""INSERT INTO
                       user (name,surname)
                       VALUES ('{name}', '{surname}')"""

        cursor.execute(insert_sql)
        connection.commit()
    except Exception as e:
        print("There was an error in the db")
        print(e)



def read_date_from_db():
    try:
        connection = sqlite3.connect("date base")
        cursor = connection.cursor()

        select_sql = """
        SELECT * FROM user
        """
        cursor.execute(select_sql)
        connection.commit()
        data = cursor.fetchall()
        connection.close()
        return data
    except Exception as e:
        print('There was an error with db!')
        print(e)
def keyboard():
    markup = ReplyKeyboardMarkup(row_width=2)

    button1 = KeyboardButton('save name')
    button2 = KeyboardButton("save surname")
    markup.add(button1, button2)

    return markup
bot.infinity_polling()














