class script(object):
    START_TXT = """ð·ðīðŧðū {},
ðžð ð―ð°ðžðī ðļð <a href=https://t.me/{}>{}</a>, ðļ ðēð°ð― ðŋððūððļðģðī ðžðūððļðīð, ðđððð ð°ðģðģ ðžðī ððū ððūðð ðķððūððŋ ð°ð―ðģ ðžð°ðšðī ðžðī ð°ðģðžðļð―.. ðð·ðīð― ððīðī ðžð ðŋðūððīðð âĨïļâĨïļðĨ"""
    HELP_TXT = """ð·ðīð {}
ð·ðīððī ðļð ðð·ðī ð·ðīðŧðŋ ðĩðūð ðžð ðēðūðžðžð°ð―ðģð."""
    ABOUT_TXT = """âŪ ðžð ð―ð°ðžðī: {}
âŪ ðēððīð°ððūð: <a href=https://t.me/itz_mrshyam>âMĖķRĖķ SĖķHĖķYĖķAĖķMĖķ</a>
âŪ ðŧðļðąðð°ðð: ðŋðððūðķðð°ðž
âŪ ðŧð°ð―ðķðð°ðķðī: ðŋððð·ðūð― ðđ
âŪ ðģð°ðð° ðąð°ððī: ðžðūð―ðķðū ðģðą
âŪ ðąðūð ððīðððīð: ð·ðīððūðšð
âŪ ðąððļðŧðģ ððð°ððð: v1.0.2 [ ðąðīðð° ]"""
    SOURCE_TXT = """<b>Donation</b>

âŠž <b>ððĻðŪ ððð§ ððĻð§ðð­ð ðð§ðē ððĶðĻðŪð§ð­ ððĻðŪ ðððŊð ðģ. 

<b>âââââââââá Payment Methods áâââââââââ

âŪ ððžðžðīðđðēðĢðŪð
âŪ ðĢðŪðððš
âŪ ðĢðĩðžðŧðēðĢðē
âŪ ðĢðŪððĢðŪðđ

_ððĻð§ð­ððð­ ðð ððĻðŦ ðð§ðĻð° ðððĻðŪð­ ððĄð ðððēðĶðð§ð­ ðð§ððĻ_
ââââââââââââá <a href=https://t.me/itz_mrshyam><b>âMĖķRĖķ SĖķHĖķYĖķAĖķMĖķ</b></a> áââââââââââââ"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>  

- Filter is the feature were users can set automated replies for a particular keyword and áĐááĐá­ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. áĐááĐá­ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âū /filter - <code>add a filter in chat</code>
âū /filters - <code>list all the filters of a chat</code>
âū /del - <code>delete a specific filter in chat</code>
âū /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- áĐááĐá­ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. áĐááĐá­ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://telegram.me/m_s_p_o_123)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âū /connect  - <code>connect a particular chat to your PM</code>
âū /disconnect  - <code>disconnect from a chat</code>
âū /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of áĐááĐá­

<b>Commands and Usage:</b>
âū /id - <code>get id of a specifed user.</code>
âū /info  - <code>get information about a user.</code>
âū /imdb  - <code>get the film information from IMDb source.</code>
âū /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my OáŊáEáâĄ

<b>Commands and Usage:</b>
âū /logs - <code>to get the rescent errors</code>
âū /stats - <code>to get status of files in db.</code>
âū /delete - <code>to delete a specific file from db.</code>
âū /users - <code>to get list of my users and ids.</code>
âū /chats - <code>to get list of the my chats and ids </code>
âū /leave  - <code>to leave from a chat.</code>
âū /disable  -  <code>do disable a chat.</code>
âū /ban  - <code>to ban a user.</code>
âū /unban  - <code>to unban a user.</code>
âū /channel - <code>to get list of total connected channels</code>
âū /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """âŪ ððūðð°ðŧ ðĩðļðŧðīð: <code>{}</code>
âŪ ððūðð°ðŧ ðððīðð: <code>{}</code>
âŪ ððūðð°ðŧ ðēð·ð°ðð: <code>{}</code>
âŪ ðððīðģ ðððūðð°ðķðī: <code>{}</code> ðžððą
âŪ ðĩððīðī ðððūðð°ðķðī: <code>{}</code> ðžððą"""
    LOG_TEXT_G = """#ððð°ððŦðĻðŪðĐ
âŪ ððŦðĻðŪðĐ âšâš {}(<code>{}</code>)
âŪ ððĻð­ððĨ ðððĶðððŦðŽ âšâš <code>{}</code>
âŪ ððððð ððē âšâš {}
"""
    LOG_TEXT_P = """#ððð°ððŽððŦ
âŪ ðð âšâš <code>{}</code>
âŪ ðððĶð âšâš {}
"""
