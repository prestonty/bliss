from taipy import Gui
from taipy.gui import Html, navigate
import taipy.gui.builder as tgb
import data
import csv
from datetime import datetime

# --------------------------------------------------------- setting up global styling
stylekit = {
  "color_primary": "#FFB6C1",
  "color_secondary": "#FFC0CB",
}
# ---------------------------------------------------------

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

def add_entry(activity_category):
    current_date = datetime.now().strftime("%m/%d/%y")

    data_list = [current_date, activity_category]

    with open('test.csv', 'a', newline='') as csvfile:
      csv_writer = csv.writer(csvfile)
      csv_writer.writerow(data_list)


def on_action(state, id):
    if id == "loginSubmit":
        pages = homeContent
        pass
    elif id == "logoutSubmit":
        pages = loginContent
    elif id in button_ids:
        # pages = analyticsContent
        add_entry(button_ids.get(id))
        navigate(state, "analytics") # is there a better way to do this?

# --------------------------------------------------------- Login Page
loginContent = Html("""
<h1>Join Bliss Today</h1>
                    
<h2>Login Page</h2>
""")

# navigates to home function
def nav_home(state):
    navigate(state, "home")
    pass

with tgb.Page() as loginContent:

    with tgb.layout("3 1"):
        tgb.html("p", "Username:")
        tgb.input("", label="")
        tgb.html("p", "Password:")
        tgb.input("******", label="")
    tgb.button("Submit", id="loginSubmit", on_action="nav_home")

# --------------------------------------------------------- Home Page

homeContent = Html("""
<h1>Welcome to Bliss</h1>

Feeling devastated from work? We will get you mind back on track!
""")
# must declare before page
with tgb.Page() as homeContent:
    tgb.html("p", "How are you feeling today?")
    tgb.input("Enter text here", label="Feeling Today?")

# --------------------------------------------------------- calm Page
calmContent = Html("""
<h1>Welcome To the Calm Zone</h1>
No yelling allowed.""")

with tgb.Page() as calmContent:
    tgb.html("p", "Choose a calm activity for today's break:")
    # i would like to add images

    tgb.button("Journaling", id="journalSubmit")
    tgb.button("Meditating", id="meditateSubmit")
    tgb.button("Ambient Noise", id="ambientSubmit")

# --------------------------------------------------------- energy Page
energyContent = Html("""
<h1>Welcome To the Energy Zone</h1>
BE AS LOUD AS YOU WANT!!!""")

with tgb.Page() as energyContent:
    tgb.html("p", "Choose an energetic activity for today's break:")
    # i would like to add images

    tgb.button("Exercise Routines", id="exerciseSubmit")
    tgb.button("Hiking", id="hikingSubmit")
    tgb.button("Power Nap", id="napSubmit")
# --------------------------------------------------------- relax Page
relaxContent = Html("""
<h1>Welcome To the Relax Zone</h1>
""")

with tgb.Page() as relaxContent:
    tgb.html("p", "Choose a relaxing activity for today's break:")
    # i would like to add images

    tgb.button("Deep Breathing", id="breathingSubmit")
    tgb.button("Reading", id="readingSubmit")
    tgb.button("Massage", id="massageSubmit")

# --------------------------------------------------------- Analytics Page
analyticsContent = """

<|{data.dataframe}|chart|properties={data.property_chart}|>

"""

with tgb.Page() as relaxContent:
    tgb.html("p", "Choose a relaxing activity for today's break:")
    # i would like to add images

    tgb.button("Deep Breathing", id="breathingSubmit")
    tgb.button("Reading", id="readingSubmit")
    tgb.button("Massage", id="massageSubmit")
# --------------------------------------------------------- Routing between pages
pages = {
    "/": "<|menu|lov={page_names}|on_action=menu_action|>",
    "login": loginContent,
    "home": homeContent,
    "calm": calmContent,
    "energy": energyContent,
    "relax": relaxContent,
    "analytics": analyticsContent,
}
page_names = [page for page in pages.keys() if page != "/"]

def menu_action(state, action, payload):
    page = payload["args"][0]
    navigate(state, page)

# --------------------------------------------------------- Display the GUI


gui = Gui(pages=pages)
gui.run(run_browser=False, stylekit=stylekit)
# DO NOT ADD use_reloader=True IT DOES NOT WORK FOR MAC
