from taipy import Gui
from taipy.gui import Html, navigate
import taipy.gui.builder as tgb
import data
import csv
import graphs
import chat
from datetime import datetime
import pandas as pd

# --------------------------------------------------------- setting up global styling
stylekit = {
  "color_primary": "#FFB6C1",
  "color_secondary": "#FFC0CB",
}
# ---------------------------------------------------------
DATE = "Date"
RELAX = "Relaxing"
CALM = "Calming"
ENERGY = "Energizing"
BREAKTYPE = "Break"

button_ids = {
    "journalSubmit": "Calming",
    "meditateSubmit": "Calming",
    "ambientSubmit": "Calming",
    "exerciseSubmit": "Energizing",
    "hikingSubmit": "Energizing",
    "napSubmit": "Energizing",
    "breathingSubmit": "Relaxing",
    "readingSubmit": "Relaxing",
    "massageSubmit": "Relaxing"
  }

data.refresh_data()

dataframe = pd.DataFrame({DATE:graphs.date_lis,
                          RELAX:graphs.relax_breaks,
                          ENERGY:graphs.energy_breaks,
                          CALM:graphs.calm_breaks})

def add_entry(activity_category):
    current_date = datetime.now().strftime("%m/%d/%y")

    data_list = [current_date, activity_category]

    with open('test.csv', 'a', newline='') as csvfile:
      csv_writer = csv.writer(csvfile)
      csv_writer.writerow(data_list)

def on_action(state, id):
    # Code to update graph
    if id == "loginSubmit":
        pages = homeContent
        pass
    elif id == "logoutSubmit":
        pages = loginContent
    elif id in button_ids:
        add_entry(button_ids.get(id))
        navigate(state, "analytics")
        data.refresh_data()
        data_dict = {
            DATE:graphs.get_date_lis(),
            RELAX:graphs.get_relax(),
            ENERGY:graphs.get_energy(),
            CALM:graphs.get_calm()
        }
        state.dataframe = pd.DataFrame(data_dict)

# --------------------------------------------------------- Login Page

loginContent = Html("""""")
# STORE USERNAME AND PASSWORD
user = "user123"
password = "password123"

# navigates to home function
def nav_home(state):
    global user
    global password
    navigate(state, "home")
    pass
def updateUser(state):
    global user
    user = state.user
    print("Current user is: ", user)
def updatePassword(state):
    global password
    password = state.password
    print("Current password is ", password)

loginContent = """
<h1>Join bliss Today</h1>
<p>Username: </p>
<|{user}|input|on_change=updateUser|>
<p>Password: </p>
<|{password}|input|on_change=updatePassword|password=True|>              
<|Login|button|id="loginSubmit"|on_action=nav_home|>
"""

# with tgb.Page() as loginContent:
#     tgb.html("h1", "Join bliss Today")
#     with tgb.layout("3 1"):
#         tgb.html("p", "Username:")
#         tgb.input("{user}", label="", on_change="updateUser")
#         tgb.html("p", "Password:")
#         tgb.input("{password}", label="", on_change="updatePassword", password=True)
#     tgb.button("Login", id="loginSubmit", on_action="nav_home")


# --------------------------------------------------------- Home Page

homeContent = tgb.Page()

def nav_calm(state):
    navigate(state, "calm")
    pass

def nav_energy(state):
    navigate(state, "energy")
    pass

def nav_relax(state):
    navigate(state, "relax")
    pass

homeContent = Html("""
    <div style="background-image: url('images/main_home.png'); background-size: cover; width: 95vw; height: 100vh;">
                   <button style="font-family: 'Trebuchet MS', sans-serif; font-size:24px; color:white; border-radius:30px; border-color:white; background-color:#80ad9b; margin-left:360px; margin-top:340px; margin-bottom:100px" type="button" onclick="nav_calm()">Calm Breaks</button>
                   <button style="font-family: 'Trebuchet MS', sans-serif; font-size:24px; color:white; border-radius:30px; border-color:white; background-color:#80ad9b; margin-left:200px; margin-bottom:100px" type="button" onclick="nav_energy()">Energetic Breaks</button>
                   <button style="font-family: 'Trebuchet MS', sans-serif; font-size:24px; color:white; border-radius:30px; border-color:white; background-color:#80ad9b; margin-left:200px; margin-bottom:100px" type="button" onclick="nav_relax()">Relaxing Breaks</button>
    </div>
""")

# navigates to home function
def nav_login(state):
    navigate(state, "login")
    pass

# must declare before page
# with tgb.Page() as homeContent:
#     tgb.html("h1", "Welcome to Bliss, {user}!")
#     tgb.html("p", "Feeling devastated from work? We will get you mind back on track!")
#     tgb.html("p", "How are you feeling today?")
#     tgb.input("Enter text here", label="Feeling Today?")
#     tgb.button("Logout", id="logoutSubmit", on_action="nav_login")

# --------------------------------------------------------- calm Page
calmContent = """
<h1>Welcome To the Calm Zone</h1>
<p>Calmness. Moments of peace. Like a cold breeze in the autumn night.</p>
<p style="margin-bottom:30px;">Choose a calm activity for today's break:</p>

<|Journaling|button|id=journalSubmit|on_action=on_action|>
<div style="display: flex; justify-center">
    <img style="margin-bottom: 20px; margin-top: 15px; width: 200px; height: auto; margin-right: 20px;" src="images/journaling.png" alt="Description of the image"></img>
    <p style="">Journalling can be a great way to destress and calm down! It means recording your thoughts, reflections, and experiences in some sort of diary.</p>
</div>
<|Meditation|button|id=meditateSubmit|on_action=on_action|>
<div style="display: flex; justify-center">
    <img style="margin-bottom: 20px; margin-top: 15px; width: 200px; height: auto; margin-right: 20px;" src="images/journaling.png" alt="Description of the image"></img>
    <p style="">Journalling can be a great way to destress and calm down! It means recording your thoughts, reflections, and experiences in some sort of diary.</p>
</div>
<|Ambient Sound|button|id=ambientSubmit|on_action=on_action|>
<div style="display: flex; justify-center">
    <img style="margin-bottom: 20px; margin-top: 15px; width: 200px; height: auto; margin-right: 20px;" src="images/journaling.png" alt="Description of the image"></img>
    <p style="">Journalling can be a great way to destress and calm down! It means recording your thoughts, reflections, and experiences in some sort of diary.</p>
</div>
"""


# --------------------------------------------------------- energy Page
energyContent = """
<h1>Welcome To the Energy Zone</h1>
<p>"Energy. It's what fuels us and what drives us forward.</p>
<p style="margin-bottom:30px;">Choose an energetic activity for today's break:</p>

<|Exercise Routines|button|id=exerciseSubmit|on_action=on_action|>
<div style="display: flex; justify-center">
    <img style="margin-bottom: 20px; width: 200px; height: auto; margin-right: 20px;" src="images/journaling.png" alt="Description of the image"></img>
    <p style="">Jounjfdksjkdsfjksfdj text goes here</p>
</div>

<|Hiking|button|id=hikingSubmit|on_action=on_action|>
<div style="display: flex; justify-center">
    <img style="margin-bottom: 20px; width: 200px; height: auto; margin-right: 20px;" src="images/journaling.png" alt="Description of the image"></img>
    <p style="">Jounjfdksjkdsfjksfdj text goes here</p>
</div>

<|Power Nap|button|id=napSubmit|on_action=on_action|>
<div style="display: flex; justify-center">
    <img style="margin-bottom: 20px; width: 200px; height: auto; margin-right: 20px;" src="images/journaling.png" alt="Description of the image"></img>
    <p style="">Jounjfdksjkdsfjksfdj text goes here</p>
</div>
"""
# --------------------------------------------------------- relax Page
relaxContent = """
<h1>Welcome To the Relax Zone</h1>
<p>Relaxation. Unwinding into a state of trainquility.</p>
<p style="margin-bottom:30px;">"Choose a relaxing activity for today's break:</p>

<|Deep Breathing|button|id=breathingSubmit|on_action=on_action|>
<div style="display: flex; justify-center">
    <img style="margin-bottom: 20px; width: 200px; height: auto; margin-right: 20px;" src="images/journaling.png" alt="Description of the image"></img>
    <p style="">Jounjfdksjkdsfjksfdj text goes here</p>
</div>

<|Reading|button|id=readingSubmit|on_action=on_action|>
<div style="display: flex; justify-center">
    <img style="margin-bottom: 20px; width: 200px; height: auto; margin-right: 20px;" src="images/journaling.png" alt="Description of the image"></img>
    <p style="">Jounjfdksjkdsfjksfdj text goes here</p>
</div>

<|Massage|button|id=massageSubmit|on_action=on_action|>
<div style="display: flex; justify-center">
    <img style="margin-bottom: 20px; width: 200px; height: auto; margin-right: 20px;" src="images/journaling.png" alt="Description of the image"></img>
    <p style="">Jounjfdksjkdsfjksfdj text goes here</p>
</div>
"""
# --------------------------------------------------------- Analytics Page
analyticsContent = """

<|{dataframe}|chart|properties={data.property_chart}|rebuild|>

"""
# --------------------------------------------------------- Chatbot Page
# chatContent = """"""
chatContent = tgb.Page()
userQuestion = "say hello"
properQuestion = False
prompt = "say hello"
answer = ""
wordCount = 40
def updateUserQuestion(state):
    global userQuestion
    userQuestion = state.userQuestion
    print("Current userQuestion is: ", userQuestion)
    pass

def submitQuestion(state):
    prompt = state.userQuestion
    state.answer = chat.genActivity(prompt + " answered in less than " + str(wordCount) +" words")
    pass


chatContent = """
<h1>Introducing bliss' chatbot, Arcadia, powered by Cohere's AI!</h1>
<br/>

<p>Hi, I am Arcadia, here to help. I can recommend any relaxing, energetic, or calming activities for you to do!</p>
<|{userQuestion}|input|label="ask here"|on_change=updateUserQuestion|>
<|Ask|button|id="questionSubmit"|on_action=submitQuestion|>
<|{answer}|input|multiline|answer|active={prompt!="" and answer!=""}|class_name=fullwidth|>
"""

# --------------------------------------------------------- Routing between pages
pages = {
    "/": "<|menu|lov={page_names}|on_action=menu_action|>",
    "login": loginContent,
    "home": homeContent,
    "calm": calmContent,
    "energy": energyContent,
    "relax": relaxContent,
    "analytics": analyticsContent,
    "chat": chatContent,
}
page_names = [page for page in pages.keys() if page != "/"]

def menu_action(state, action, payload):
    page = payload["args"][0]
    navigate(state, page)

# --------------------------------------------------------- Display the GUI


gui = Gui(pages=pages)
gui.run(run_browser=False, stylekit=stylekit)
# DO NOT ADD use_reloader=True IT DOES NOT WORK FOR MAC