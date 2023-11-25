from taipy import Gui
from taipy.gui import Html, navigate
import taipy.gui.builder as tgb


def on_action(state, id):
    if id == "loginSubmit":
        pages = homeContent
        pass
    elif id == "logoutSubmit":
        pages = loginContent

# --------------------------------------------------------- Login Page
loginContent = Html("""

<h1>Login Page</h1>

""")

# must declare before page
with tgb.Page() as loginContent:

    with tgb.layout("3 1"):
        tgb.html("p", "Username:")
        tgb.input("", label="")
        tgb.html("p", "Password:")
        tgb.input("******", label="")
    tgb.button("Submit", id="loginSubmit")

# ---------------------------------------------------------


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

    tgb.button("Exercise Routines", id="journalSubmit")
    tgb.button("idk", id="meditateSubmit")
    tgb.button("still done know", id="ambientSubmit")
# --------------------------------------------------------- relax Page
relaxContent = Html("""
<h1>Welcome To the Relax Zone</h1>
""")

with tgb.Page() as relaxContent:
    tgb.html("p", "Choose a relaxing activity for today's break:")
    # i would like to add images

    tgb.button("Breathing", id="journalSubmit")
    tgb.button("idk", id="meditateSubmit")
    tgb.button("idk man", id="ambientSubmit")
# --------------------------------------------------------- relax Page


root_md="<|menu|label=Menu|lov={[('calmContent', 'Calming'), ('energyContent', 'Energizing'), ('relaxContent', 'Relaxation')]}|on_action=on_menu|>"
loginPage="## This is page 1"
home="## This is page 2"

#trying to navigate between pages using the buttons (it aint working)
def on_menu(state, var_name, function_name, info):
    page = info['args'][0]
    navigate(state, to=page)

#trying to navigate to home (it aint working)
def go_home(state):
    navigate(state, "home")

pages = {
    "/": root_md,
    "login": loginContent,
    "home": homeContent,
    "calm": calmContent,
    "energy": energyContent,
    "relax": relaxContent,
}
Gui(pages=pages).run()