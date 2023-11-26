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
    # we could remove the if statements for login logout
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
loginContent = Html("""
<h1>Join Bliss Today</h1>
                    
<h2>Login Page</h2>
""")

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

with tgb.Page() as loginContent:
    with tgb.layout("3 1"):
        tgb.html("p", "Username:")
        tgb.input("{user}", label="", on_change="updateUser")
        tgb.html("p", "Password:")
        tgb.input("{password}", label="", on_change="updatePassword", password=True)
    tgb.button("Login", id="loginSubmit", on_action="nav_home")

# --------------------------------------------------------- Home Page

homeContent = tgb.Page()

homeContent = Html("""
    <div style="background-image: url('imgs/home-page.png'); background-size: cover; width: 100vw; height: 100vh;">
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
calmContent = Html("""
<h1>Welcome To the Calm Zone</h1>
No yelling allowed.""")

with tgb.Page() as calmContent:
    tgb.html("p", "Calmness. Moments of peace. Like a cold breeze in the autumn night.")
    tgb.html("p", "Choose a calm activity for today's break:")
    # i would like to add images

    tgb.button("Journaling", id="journalSubmit")
    tgb.button("Meditating", id="meditateSubmit")
    tgb.button("Ambient Noise", id="ambientSubmit")

# --------------------------------------------------------- energy Page
energyContent = Html("""""")

with tgb.Page() as energyContent:
    tgb.html("h1", "Welcome To the Energy Zone {user}")
    tgb.html("p", "Feeling devastated from work? We will get you mind back on track!")
    tgb.html("p", "Energy. It's what fuels us and what drives us forward.")
    tgb.html("p", "Choose an energetic activity for today's break:")
    # i would like to add images

    tgb.button("Exercise Routines", id="exerciseSubmit")
    tgb.button("Hiking", id="hikingSubmit")
    tgb.button("Power Nap", id="napSubmit")
# --------------------------------------------------------- relax Page
relaxContent = Html("""""")

with tgb.Page() as relaxContent:
    tgb.html("h1", "Welcome To the Relax Zone")
    tgb.html("p", "Relaxation. Unwinding into a state of trainquility.")
    tgb.html("p", "Choose a relaxing activity for today's break:")
    # i would like to add images
    tgb.button("Deep Breathing", id="breathingSubmit")
    tgb.button("Reading", id="readingSubmit")
    tgb.button("Massage", id="massageSubmit")

# --------------------------------------------------------- Analytics Page
analyticsContent = """

<|{dataframe}|chart|properties={data.property_chart}|rebuild|>

"""

with tgb.Page() as relaxContent:
    tgb.html("p", "Relaxation. Unwinding into a state of trainquility.")
    tgb.html("p", "Choose a relaxing activity for today's break:")
    # i would like to add images
    tgb.button("Deep Breathing", id="breathingSubmit")
    tgb.button("Reading", id="readingSubmit")
    tgb.button("Massage", id="massageSubmit")

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
<h1>Introducing Bliss's chatbot, Arcadia, powered by Cohere's AI!</h1>
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
