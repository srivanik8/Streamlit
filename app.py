import streamlit as st
import pandas as pd
import time as ts
from datetime import time

#removing streamlit hamburger and footer
st.markdown("""
<style>
.css-nqowgj.e1ewe7hr3{
visibility: hidden;
}
.css-h5rgaw.e1g8pov61{
visibility: hidden;
}
</style>
""",unsafe_allow_html=True)

table = pd.DataFrame({'column 1': [1,2,3,4,5], 'column2': [8,9,10,11,12]})
# text elements of streamlit
st.title("hii, this is sri")
st.subheader("hi, i am your subheader")
st.header("hi, i am your header")
st.text("hi, i am text function and am used in place of a paragraph")
st.markdown("# Hello world")
st.markdown("---")
#display elemts of streamlit
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json={"a":"1,2,3","b":"4,5,6"}
st.json(json)   
code="""
print("hello world)
def funct():
    return 0;"""
st.code(code, language="python")
st.write("## H2")
st.metric(label="wind speed", value="120ms⁻¹" , delta="-1.4ms⁻¹")
st.table(table)
st.dataframe(table)
#basic interactive widgets
state=st.checkbox("checkbox", value=True)
if state:
    st.write("You will be able to see me if you checked me")
else:
    pass

def change():
    print(st.session_state.checker)
state=st.checkbox("checkbox", value=True, on_change=change, key="checker") 
radio_btn=st.radio("how are you today?", options={"bad","good","amazing"})
print(radio_btn)
def btn_click():
    print("button clicked")
btn = st.button("click me", on_click= btn_click)
select = st.selectbox("what is your favourite food?", options=("biryani","mango juice","chocolates"))
print(select)
multi_select = st.multiselect("what is your favourite food?", options=("biryani","mangojuice","chocolate"))
print(multi_select)

#fileuploader
image = st.file_uploader("please upload an image", type=["png","jpeg"], accept_multiple_files=True)
if image is not None:
    for image in image:
       st.image(image)
video = st.file_uploader("please upload a video", type="mp4")
if video is not None:
    st.video(video)

#interactive widgets of streamlit
slid = st.slider("how much do you like me?", min_value=50, max_value=100, value=60)
print(slid) #prints in the terminal
point = st.select_slider("point",options=["min", "max"])
st.write(point) #used to write in the app
text =  st.text_input("enter your course title?", max_chars=60)
area = st.text_area("course description")
date = st.date_input("enter your registration date")


#progress bars
def converter(value):
    m,s,mm=value.split(":")
    t_s=int(m)*60+int(s)+int(mm)/1000
    return t_s
times = st.time_input("set timer", value=time(0,0,0))
if str(times) == "00:00:00" :
    st.write("please set timer")
else:
    sec = converter(str(times))
    print(sec)
    bar = st.progress(0)
    per = sec/100
    progress_status =st.empty()
    for i in range(100):
        bar.progress(i + 1)
        progress_status.write(str(i) + "%")
        ts.sleep(per)

#forms
st.markdown("<h1 style='text-align: center'>User Registration</h1>", unsafe_allow_html=True)
form = st.form("Form 1")
form.text_input("First name")
form.form_submit_button("Submit")


with st.form("Form 2", clear_on_submit=True):
    col1,col2 = st.columns(2)
    f_name=col1.text_input("First name")
    l_name=col2.text_input("Last name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day,month,year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_state=st.form_submit_button("Submit")
    if s_state:
        if f_name == "" and l_name == "":
            st.warning("Please fill above fields")
        else:
            st.success("submitted successfully")