from fasthtml.common import *
from codecs import decode


app, rt = fast_app(
    hdrs=(
        Link(rel="stylesheet", href="/static/css/main.css", type="text/css"),
        Script(src="/static/scripts/main.js", nonce="kdljfadle"),)
)

def encrypt(text, s):
    result = ""

    for i in text:
        if ord(i) == 32:
            result += ' '
            continue

        if (ord(i)+s) >= 1515:
            result += (chr(ord(i)+s-27))
        else:
            result += chr((ord(i)+s))

    return result

def div_char(str):
    if str != ' ':
    #     # return Div(
    #     #     Div(' ', cls="char_space"),
    #     #     Div(' ', cls="char_space")
    #     # )
    # else:
        return Div(
            Div(str, cls="char_message"),
            Div('_', name=f"char_{ord(str)}", 
                id=f"char_{ord(str)}", cls="char_message_in", 
                onclick="select_char(this)")
        )

def div_word(str):
    return Div(
        *[div_char(char) for char in str],
        cls="message_word"
    )
def div_message():
    message = " צפע חזק נשך דג מת באוסטרליה צפע חזק נשך דג מת באוסטרליה"
    encrypt_message = encrypt(message, 1)
    print(encrypt_message)
    output = ""
    # לחלק למילים ואז להדפיס
    return Div(
        *[div_word(word) for word in encrypt_message.split(' ')],
        
        cls="message_container"
    )
def main_container():
    return Div(
        
        div_message(),

        cls="main_container"
    )
@rt("/")
def get():
    return Titled("מפענח צפנים", 
        main_container()              
    )


serve()