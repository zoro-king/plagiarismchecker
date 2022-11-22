import requests
import streamlit as st
from streamlit_lottie import st_lottie


def checker(file1,file2):
    f1=str(file1.read(),"utf-8")
    f2=str(file2.read(),"utf-8")

    str1=''.join(f1)
    str2=''.join(f2)

    sent_text1=str1.split('.')
    sent_text2=str2.split('.')

    
    final_list=[]
    for z in sent_text1:
        for y in sent_text2:
            if z == y:
                final_list.append(z)



    return final_list

st.set_page_config(page_title="Plagiarism Checker",page_icon=":mag:",layout="wide")

st.subheader("plagirism Checker in python :mag:")
st.title("comparing two files to get the plagiarised line")
st.write("user can able to compare the two files and get the output of the plagiarised line")

def load_lottie(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

lottie_coding=load_lottie("https://assets1.lottiefiles.com/packages/lf20_axrujg5c.json")
with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        file1=st.file_uploader('File1',type=["pdf","txt","docx"])
        file2=st.file_uploader('File2',type=["pdf","txt","docx"])
        
        if st.button("process"):
            lis=checker(file1,file2)
            s=''
            for i in lis:
                s += "- " + i + "\n"
            st.markdown(s)

    with right_column:
          st_lottie(lottie_coding,height=300,key="coding")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/svetri2611@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
        