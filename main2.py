import telebot
from telebot import types
from googletrans import Translator

API_TOKEN = '7019669863:AAGDpWYmnYQkhPvjyCBhxeohmLurNNcGvcI'

bot = telebot.TeleBot(API_TOKEN)

translator = Translator()

translation_history = {}

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    translate_button = types.KeyboardButton('📝 Перевести текст')
    history_button = types.KeyboardButton('📚 История переводов')
    reminder_button = types.KeyboardButton('⏰ Напоминания')
    guess_number_button = types.KeyboardButton('🔢 Угадай число')
    markup.add(translate_button, history_button, reminder_button, guess_number_button)
    
    bot.reply_to(message, "Привет! Я бот-переводчик и ассистент. Выбери опцию для продолжения:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '📝 Перевести текст')
def handle_translate_prompt(message):
    bot.reply_to(message, "Отправь мне текст, который нужно перевести.")

@bot.message_handler(func=lambda message: message.text == '📚 История переводов')
def handle_history(message):
    user_id = message.chat.id
    
    if user_id in translation_history:
        history = translation_history[user_id]
        history_text = '\n'.join([f"{original} -> {translated}" for original, translated in history])
        bot.reply_to(message, f"История переводов:\n{history_text}")
    else:
        bot.reply_to(message, "У вас пока нет истории переводов.")

@bot.message_handler(func=lambda message: 'Files 1&2 A photographer' in message.text)
def handle_files_1_and_2(message):
    response_text = """This is Gonzalo. He’s a photographer. At the moment he is living and working in New York. Every day he takes photos of the city and its people. Gonzalo came to New York two years ago from Guatemala. He found a job and is now living in the east village. He has a photography studio in his apartment, and he uses lots of different equipment. Gonzalo loves his life and his work, but he wasn’t always a photographer. 'I went to school for something completely different. Uh, I went to law school. I graduated from law school. I went to UFM, I have a law degree from UFM. But when I graduated I was not happy with my choice of um career' Gonzalo was working for a newspaper when he decided to become a photographer and move to the United States. Gonzalo now works as a professional fashion photographer. He uses several different cameras and lenses, but one camera is particularly special. 'My first camera, um, actually is this one. I inherited it from my grandfather. He passed away when I was seven years old. My grandfather was German. This is a German camera. It’s a Leica M2 it’s still in mint condition. I treasure it so much. I barely use it but I mean it takes amazing quality photographs still … so it’s pretty cool.' Today Gonzalo is taking photographs of a model for a famous fashion website. But Gonzalo likes to photograph – or ‘shoot’ - lots of different things. What are his favourite? 'My favourite things to shoot, um, that’s a very tough question because I shoot a lot of things. I love to shoot portraits. I love to shoot the street, I’m a big sports fan. So, uh, I like to shoot sports a lot.' Photography isn’t always easy. Gonzalo travels a lot and at the moment he is working on three different jobs. So why does he enjoy his job? 'It entertains me. It distracts me. it stops me from worrying about my everyday troubles or my stress or anything. So I enjoy it. I enjoy it, you know.' For Gonzalo every day is different and in a city like New York there’s always something new and exciting to photograph."""
    bot.reply_to(message, response_text)

@bot.message_handler(func=lambda message: 'Files 3&4 Shopping in the UK' in message.text)
def handle_files_3_and_4(message):
    response_text = """The British high street has always been a popular place to buy and sell. Recently, however, this has changed. Fourteen per cent of town-centre shops are now empty. So, where have all the shoppers gone? This is The Oracle in Reading, England. It opened in 1999 and it cost £250m to build. Today, it has 90 shops on three different levels and covers over 80,000 square metres. Shoppers can browse their favourite labels, have a meal or a drink in one of its 22 restaurants, cafés and bars or even watch a film in its 10-screen cinema. With its glass roof and riverside location The Oracle offers a 21st century shopping experience. It is an exciting and entertaining place where you can buy all of today’s most fashionable brand names. But ‘shopping centres’ are not just a 21st century phenomenon. The Burlington Arcade, which opened in 1819, was one of the world’s first shopping centres. Lord George Cavendish, the man who built the arcade, said it was “for the sale of jewellery and fancy articles.” Today, shoppers can still buy luxurious and unique products, such as hand-made gold and silverware, precious materials and even these golden slippers. The arcade is almost 200 meters long and has been a part of London’s history for almost 200 years. However, the Burlington’s owners are going to modernise this traditional shopping arcade. Something they are very excited about is that some global modern brands, like Lulu Guiness and Jimmy Choo, are going to be based there, as well as the older specialist stores like Penhaligons and the jewellers Heming of London. The Burlington Arcade and The Oracle are two very different shopping centres but both are almost always busy. Experts predict that this is going to change as online shopping becomes more popular and people start to shop from home. However, at the moment only about 10% of retail transactions take place online while 31% take place in shopping centres. As long as places like The Burlington Arcade and The Oracle continue to offer convenience and choice they will continue to be a popular place to shop."""
    bot.reply_to(message, response_text)

@bot.message_handler(func=lambda message: 'Files 5&6 Chicago' in message.text)
def handle_files_5_and_6(message):
    response_text = """Chicago is the largest city in the U.S. state of Illinois. Some of the things it is famous for are pizza, gangsters and sports. This is Wrigley Field, home to the Chicago Cubs, Chicago’s oldest baseball team. Many American people call Chicago ‘The Second City’ because for a hundred years it had the second biggest population in the country. It was smaller than New York but, until the 1980s, it was bigger than every other American city. Today, Chicago is a very popular tourist destination. Every year over thirty million people visit the city. They go to the Millennium Park, the newest park in Chicago, they walk along the shore of Lake Michigan, the second largest of the five Great Lakes, and they admire the view from the top of The Willis Tower. The Willis Tower used to be called the Sears Tower and for 25 years it was the tallest building in the world. In 1969 Sears, Roebuck and co., the largest department store chain in the world at that time, built the tower to use as office blocks. Today the skyscraper is one of the most popular tourist attractions in the city. It is still the tallest skyscraper in the U.S but it isn’t as tall as the Burj Khalifa in Dubai or the Petronas Twin Towers in Kuala Lumpur. Chicago’s other famous nickname is ‘The Windy City.’ People say that it is windier than other major cities but weather experts disagree. In fact scientists predict that Chicago will have a very different climate in the future. They say that it won’t be as cold and as windy as it is now but will be warmer and wetter. This will mean many changes but Chicago is further ahead than most other cities in its preparations for climate change. The city is constructing new environmentally friendly buildings, planning more parks and green areas and placing big hedges alongside the city’s pathways. Chicago is also investing in new roads and car parks for electric cars. Chicago is a changing city. The Windy City’s famous climate is going to become much warmer. Chicago will be a hotter more tropical place than it is today. This will cause problems but at the moment America’s Second City is one of the first places to properly deal with pollution and climate change."""
    bot.reply_to(message, response_text)

@bot.message_handler(func=lambda message: 'Files 7&8 Learning a language' in message.text)
def handle_files_7_and_8(message):
    response_text = """This is year ten in Llantaf School in Cardiff. The students in this class are between 14 and 15 years old and there are about thirty in each class. They all speak Welsh and English but today the students are learning how to speak French. In most schools in England and Wales students have to learn a foreign language but they don’t have to choose French. In this school, for example, students can also learn German, Spanish, Italian, and even Latin. Whatever language they choose, they will have three to four forty minute classes every week and they’ll have to do an exam at the end of the year. Today these students are learning how to describe their hometown. The teacher explains the language and the students have to take notes and answer questions on worksheets. Discipline in class is quite strict. The teacher doesn’t allow chatting and the students have to obey the rules. Technology is becoming more popular in British classrooms. This teacher is using a projector to practise vocabulary and pronunciation. Most students enjoy learning a new language, but not all of them! This is an English lesson at a private language school in Oxford. The classes here are quite small. There are usually about eight students in each class. Most of the students here are adults and they come from lots of different countries. They say that if they learn English they’ll have a better chance of getting a good job. Because these students are adults discipline isn’t a big problem. The teacher and the students try to have fun and lots of the activities involve working and speaking in pairs and groups. The teacher must be active, enthusiastic, and hardworking. Caroline Reading, another English teacher in Oxford, explains what teaching English as a foreign language is like. 'Why did you decide to become an English teacher?' 'Well, I left university and didn’t know what to do and I decided I wanted to travel. So it was a good way to see the world.' 'What do you like best about the job?' 'I think the best thing for me is, um, being with people and just helping them with their learning. Helping them get on in life with their English.' 'What do you like least about the job?' 'I think the worst thing is probably the marking, correcting their homework and essays.' 'What problems do different nationalities have when learning English, and why?' 'The, the learners from the Far East and the Middle East have problems with writing and reading in English and this is because their languages have a different alphabet and so before they can start learning English they have to learn our alphabet. And they also read from right to left, which makes it very difficult for them. Italian, Spanish, and I think French students also have problems with pronunciation, that’s probably their biggest problem. And then if you speak German, so if you come from Switzerland or Germany, they also have pronunciation problems, but it’s more to do with the intonation, as they can sound a little bit rude in English.' 'What do you think is the most useful thing(s) students can do outside class to improve their language learning?' 'I think that outside the classroom students should first of all do their homework and go back over what they’ve learnt in the classroom during the class. But I also think that they need to do more than that. They need to go on the internet, watch films in English, if they can read a book in English and socialize with people and also travel, because when you travel you often end up speaking in English to people.' Teaching English in a language school is quite different to teaching French in a secondary school. But both involve working hard, and having fun."""
    bot.reply_to(message, response_text)

@bot.message_handler(func=lambda message: True)
def handle_default_message(message):
    bot.reply_to(message, "Простите, я не понимаю вашу команду. Пожалуйста, попробуйте другую.")

bot.polling()
