import telegram.ext
from telegram.ext import CallbackQueryHandler
from ytmusic import YTMusicapp
import database
from telegram import *
from youtube_dll import song_conversion
import os









# useful code
# update.message.reply_text(update.message.text)
# #context.bot.send_message(chat_id=update.effective_chat.id,text="Whatsapp")



reply = ""
searched_songs_results = {}
searched_albums_results = {}
music = YTMusicapp

#music.YTmusicappclass.song_search("eminem")




def start(update, context):

    update.message.reply_text("Hello "+update.effective_chat.first_name+"!"+". My name is Morris, How can i help you today")


def song(update, context):
        global reply
        reply = "song"



        update.message.reply_text("Enter name of the song")



def album(update, context):
    global reply
    reply="album"
    
    update.message.reply_text("Enter name of the Album")
    


def help(update,context):
    update.message.reply_text("""
    The following commands are avilable:
    
    /start -> Welcome to the channel
    /help -> This message
    /content -> Simplilearn offers various courses free of course through Skillup by Simplilearn
    /Python  -> The first video from Python Playlist
    /SQL -> The first video from SQL Playlist
    /Java -> The first video from Java Playlist
    /Skillup -> Free platform for certification by Simplilearn
    /contact -> contact information 
     """)
    


def handle_message(update, context):
    global reply
    global searched_songs_results
    
    if reply == "song":
        mhinduro = ""
        music.YTmusicappclass.song_search(update.message.text)
        reply = "song_search_results"
        searched_songs_results = database.song_searched_results


        for x in searched_songs_results:
            mhinduro += str(x+1) +'. ' + searched_songs_results[x][2] + " - " + searched_songs_results[x][0] + "\n"

        buttons = [[InlineKeyboardButton("1", callback_data="first_song",)],
                   [InlineKeyboardButton("2", callback_data="second_song")],
                   [InlineKeyboardButton("3", callback_data="third_song")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                                 text=mhinduro)

        
        
        

    elif reply=="album":

        mhinduro = ""
        music.YTmusicappclass.album_search(update.message.text)
        reply = "album_search_results"
        searched_album_results = database.album_searched_results



        for x in searched_album_results:
            mhinduro += searched_album_results[x][0] + " - " + searched_album_results[x][1] + "\n"

        buttons = [[InlineKeyboardButton("1", callback_data="first_album")],
                   [InlineKeyboardButton("2", callback_data="second_album")],
                   [InlineKeyboardButton("3", callback_data="third_album")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                                 text=mhinduro)

        



    else:
        update.message.reply_text("Invalid Command")

    
    
def song_callback(update, context):
    print("Sending...")
    chat_id = update.effective_chat.id
    query = update.callback_query


    if query.data =="first_song":


        path = song_conversion.conversion().getsong(searched_songs_results,os.path.join(os.path.dirname(os.path.abspath(__file__))),0)

        song = open(path,"rb")
        context.bot.send_document(chat_id, song)

    elif query.data =="second_song":
        path = song_conversion.conversion().getsong(searched_songs_results,
                                                    os.path.join(os.path.dirname(os.path.abspath(__file__))), 1)

        song = open(path, "rb")
        context.bot.send_document(chat_id, song)
    elif query.data == "third_song":
        path = song_conversion.conversion().getsong(searched_songs_results,
                                                    os.path.join(os.path.dirname(os.path.abspath(__file__))), 2)

        song = open(path, "rb")
        context.bot.send_document(chat_id, song)


   # document = open(song_conversion(//link), 'rb')

    #context.bot.send_document(chat_id,document)






    # Code to handle when the song button is pressed



def album_callback(update, context):
    # Code to handle when the album button is pressed
    print("Album downloading...")



    



Token = ("Paste your Telegram bot token here")
#print(bot.get_me())
updater = telegram.ext.Updater("5865766343:AAECVqR7cMD2HNoJPGuOwQW4kXWtN45v1EE", use_context=True)
disp = updater.dispatcher





disp.add_handler(telegram.ext.CommandHandler('album', album))
disp.add_handler(telegram.ext.CommandHandler('song', song))
disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('heyo', start))
disp.add_handler(telegram.ext.CommandHandler('help', help))


disp.add_handler(CallbackQueryHandler(song_callback, pattern='first_song'))
disp.add_handler(CallbackQueryHandler(song_callback, pattern='second_song'))
disp.add_handler(CallbackQueryHandler(song_callback, pattern='third_song'))
disp.add_handler(CallbackQueryHandler(album_callback, pattern='first_album'))
disp.add_handler(CallbackQueryHandler(album_callback, pattern='second_album'))
disp.add_handler(CallbackQueryHandler(album_callback, pattern='third_album'))



disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()


#song-Search for a song
#album-Search for an album