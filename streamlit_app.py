from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to MY first APP!


"""

st.title("this is demo2.py")

st.header("this is header")
st.subheader("this is subheader")

st.text("this is text")
st.markdown("### this is markdown")

st.success("successful")
st.info("information")
st.warning("this is warning")
st.error("this is error danger")
st.exception("NameError('name three not definded')")

st.help(range)

st.write("Text with write")
st.write(range(10))

# from PIL import Image
# img = Image.open("HMI.png")
# st.image(img, width=300,caption="HMI")

# vid_file = open("example.mp4", "rb")
# # vid_bytes = vid_file.read()
# st.video(vid_file)

# audio_file = open("example.mp4","rb").read()
# st.audio(audio_file,format='audio/mp3')
# cheakbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

# radio
status = st.radio("what is your status", ("Active", "Inactive"))
if status == "Active":
    st.success("You are Active")
else:
    st.warning("Inacive, Activate")

# selectbox
occcupation = st.selectbox("Your Occupation",["Programmer","DataScientlist","Doctor","Busnessman"])
st.write("You selected this option ", occcupation)

# multselect
location = st.multiselect("Where do you work?",("London", "Newyork","Accre","China"))
st.write("You selected", len(location), "locations")

# Slider
level = st.slider("What is your level", 1, 5)
st.write("Your level is ", level)

# button
st.button("Simple Button")
if st.button("Aboat"):
    st.text("Streamlit is so cool")

# text input
message = st.text_area("Enter your message", "Type Here ...")
if st.button("Submit"):
    result = message.title()
    st.success(result)

# dateinput
import datetime
today = st.date_input("Today is", datetime.datetime.now())
# time
the_time = st.time_input("The time is",datetime.time())
# display json
st.text("Display JSON")
st.json({"name":"Jesse",'gender':'male'})

# display row code
st.text("Display Raw Code")
st.code("import numpy as np")

with st.echo():
    # this will also show a comment
    import pandas as pd
    df = pd.DataFrame()

# progressbar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

# spinner
# with st.spinner("Waiting.."):
#     time.sleep(5)
# st.success("Finished")

# ballons
# st.balloons()

# uploader
uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#      # To read file as bytes:
#      bytes_data = uploaded_file.getvalue()
#      st.write(bytes_data)
#
#      # To convert to a string based IO:
#      stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#      st.write(stringio)
#
#      # To read file as string:
#      string_data = stringio.read()
#      st.write(string_data)
#
#      # Can be used wherever a "file-like" object is accepted:
#      dataframe = pd.read_csv(uploaded_file)
#      st.write(dataframe)

# siderbars

# download
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

import numpy as np
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tut")
st.sidebar.button("Click me")
st.sidebar.form("myfirstform")
with st.sidebar.container():
    st.write("This is inside the container")
    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

# fuction
@st.cache
def run_fxn():
    return range(100)
st.write(run_fxn())

# # plot
# st.pyplot()
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

#
# # datetime
# st.dataframe(df)
#
# # table
# st.table(df)
if st.checkbox("Show/Hide1"):
    st.text("Showing or Hiding Widget")
    df = pd.DataFrame(
        np.random.randn(10, 5),
        columns=('col %d' % i for i in range(5)))

    st.table(df)

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

form = st.form("my_form1")
form.slider("Inside the form1")
st.slider("Outside the form")

# Now add a submit button to the form:
form.form_submit_button("Submit")

# st.form_submit_button(label="Submit", help=None, on_click=run_fxn)
# 查看pdf
with st.expander('点我查看资料'):
    import base64
    upload_file = st.file_uploader("上传pdf", type=['pdf'])
    if upload_file is not None:
        base64_pdf = base64.b64encode(upload_file.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)


for i in range(1, 3):
    print(i)


st.text('This will appear first')
# Appends some text to the app.

my_slot1 = st.empty()
# Appends an empty slot to the app. We'll use this later.

my_slot2 = st.empty()
# Appends another empty slot.

st.text('This will appear last')
# Appends some more text to the app.

my_slot1.text('This will appear second')
# Replaces the first empty slot with a text string.

my_slot2.line_chart(np.random.randn(20, 2))
# Replaces the second empty slot with a chart.
