from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler,filters, ContextTypes

Token: Final='6870935675:AAEL8ra9Aabw5uIuWhtPd56yQihNePyOJWs'
Bot_username: Final='@logistic_supportBot'

async def start_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello thanks for chatting with me!")
    
async def help_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("We are a logistic support Bot.Please leave your question so i can respond!")
    
async def custom_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")\
        
#Responses

def handle_responses(text: str) ->str:
    processed: str= text.lower()
    if 'hello' in processed:
        return 'Hey there!'
    if 'how are you' in processed:
        return 'I am good'
    if 'I love python' in processed:
        return 'We too!'
    
    return "I do not understant, so i can't help you"

async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message_type: str= update.message.chat.type
    text: str=update.message.text
    
    print(f'User({update.message.chat.id})in {message_type}:"{text}"')
    
    if message_type== 'group':
        if Bot_username in text:
            new_text:str = text.replace(Bot_username,'').strip()
            response: str = handle_responses(new_text)
        else:
            return 
        
    else:
        response: str =handle_responses(text)
        
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    
if __name__ == '__main__':
    print('Starting bot...')
    app= Application.builder().token(Token).build()
    # Commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))
    
    #Messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    
    # Errors
    app.add_error_handler(error)
    
    #polls the bot 
    print('Polling...')
    app.run_polling(poll_interval=3)  #3 seconds