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

    if message.text == "next":
        bot.reply_to(message, " выберите пункт меню",reply_markup=next_keyboard())


    if message.text == "Back":
        bot.reply_to(message, "введите данные:", reply_markup=keyboard())
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
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    button1 = KeyboardButton('save name')
    button2 = KeyboardButton("save surname")
    button3 = KeyboardButton("next")

    markup.add(button1, button2)
    markup.add(button3)

    return markup

def next_keyboard():
    markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

    button1 = KeyboardButton("Text1")
    button2 = KeyboardButton("Text2")
    button3 = KeyboardButton("Text3")
    button4 = KeyboardButton("Back")
    markup.add(button1,button2,button3)
    markup.add(button4)
    return markup
bot.infinity_polling()














