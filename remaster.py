import telebot
import time
import os

from random import choice

token = os.getenv("KEY");
bot = telebot.TeleBot(token);

@bot.message_handler(commands=['start'])
def Start(message):
    user = message.from_user.first_name
    bot.send_message(message.chat.id, "Olá, {}!\nVamos treinar multiplicação hoje?\n/iniciar para começar\n/pare para parar".format(user))

@bot.message_handler(commands=['pare'])
def Pare(message):
    bot.send_message(message.chat.id, " Ok, parando.");
    time.sleep(1);
    #bot.send_message(message.chat.id, "Como foi sua experiencia? conte nos com o comando /exp");

@bot.message_handler(commands=['iniciar'])
def Calc(message):
    Calc.num1 = choice(range(1,10));
    Calc.num2 = choice(range(1,10));
    Calc.guess = bot.send_message(message.chat.id, "Qual o resultado de {} × {}?".format(Calc.num1, Calc.num2));
    bot.register_next_step_handler(Calc.guess, Resul);

def Resul(message):
    resul = str(Calc.num1 * Calc.num2)
    if message.text == resul:
        bot.send_message(message.chat.id,"Acertou, la vem o proximo:");
        Calc(message);
    elif message.text == "/pare":
        Pare(message);
    else:
        bot.send_message(message.chat.id, " Errou, o resultado é {}".format(resul));
        time.sleep(2)
        Calc(message)
        

def main():
    bot.polling();

if __name__ == "__main__":
    main();
    
    
    
    
    
    
    
    
    
    
    
