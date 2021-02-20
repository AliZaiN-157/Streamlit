import time
import datetime
from PIL import Image
import streamlit as st

# Text/Title
st.title('Streamlit Tutorial')

# Header/SubHeader
st.header('Header')
st.subheader('SubHeader')

# Text/
st.text('Hello World')

st.markdown('yeee')

# Error
st.success("Sucessful")
st.info("Info")
st.warning("Warning")
st.error("Error")
st.exception("NameError('name error')")

# Get Help
st.help(tuple)

# Writing Text
st.write("Text with write")
st.write(range(10))

# Images
img = Image.open("demo.gif")
st.image(img, width=300)  # width height

# Videos
# vid_file = open('video.mp4', 'rb').read()
# vid_bytes = vid_file.read()
# st.video(vid_file)

# Audio
# audio_file = open('audio.mp3', 'rb').read()
# st.audio(audio_file, format="audio/mp3")

# Widget

# CheckBox

if st.checkbox("Show/Hide"):
    st.text("Show/Hide")

# Radio
status = st.radio("What is your favourite theme", ("Dark", "Light"))

if status == "Dark":
    st.header("Dark Theme")
elif status == "Light":
    st.header("Light Theme")

# Select Box
occupation = st.selectbox("Your Occupation is ", [
                          "Programmer", "Data Scientist", "Software Engineer", "Doctor"])
st.write("Your Occupation is ", occupation)


# MultiSelect

location = st.multiselect("Where do you work?",
                          ("London", "New York", "California", "Pakistan"))

# Slider

level = st.slider("What is your level", 1, 5)

# Button

st.button("Simple Button")

# if st.button("Home"):
#     st.text("Home")

# Text Input

firstname = st.text_input("Enter your First name", "Type Here ..")
if st.button("Sumbit"):

    if len(firstname) > 2:
        st.success(firstname)

# Text Area

message = st.text_area("Enter Your Message")


# Date Input

today = st.date_input("Today is", datetime.datetime.now())


# Time
the_time = st.time_input("The time is", datetime.time())


# Displaying Json data

st.text("Display Json data")
st.json({'name': "Ali", 'gender': 'male', 'age': 18})

# Display Raw Code

st.text("Display Raw Code")
st.code('import streamlit as st')

# Display Raw Code with comment
with st.echo():
    # this will show comment also
    import pandas as pd
    df = pd.DataFrame()

# Progress bar

my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p+1)

# Spinner
with st.spinner("Loading"):
    time.sleep(3)
st.success("Sucessful")

# Balloons

# st.balloons()

# SideBar

st.sidebar.header("About")
st.sidebar.text("Welcome")

# Functions


@st.cache
def run_function():
    return range(100)


st.write(run_function())

# Plot
st.pyplot()

# DataFrames

st.dataframe(df)

# Tables

st.Tables(df)
