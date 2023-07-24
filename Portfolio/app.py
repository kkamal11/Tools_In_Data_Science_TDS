import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

#set page config
st.set_page_config(
    page_title="Kamal",
    page_icon=":tada:",
    layout="wide" #use entire screen
)

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ----USE LOCAL CSS -----
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css("./style/style.css")

# ----LOAD ASSETS -------
lottie_anim_url = "https://assets5.lottiefiles.com/packages/lf20_q5qeoo3q.json"
lottie_anim_json = load_lottie_url(lottie_anim_url)
# img_contact_form = Image.open("images/filen")

# ---HEADER SECTION -----
with st.container(): #to organize the code use container
    st.subheader("Hi, I am Kamal :wave:")
    st.title("A Web Developer and Data Analyst From India")
    st.write("I am passionate about developing web apps and helping bussinesses take data-driven decisions.")
    st.markdown(
        """
            <a href="#" class="button button2">LinkedIn</a>
            <a href="https://github.com/kkamal11" class="button button2">Github</a>
        """,
        unsafe_allow_html=True
    )


# ---WHAT I DO ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do :computer:")
        st.write("##")
        st.write(
            """
            Describe what you do here.
            """
        )
    with right_column:
        st_lottie(lottie_anim_json, height=300, key="coding")

# ------PROJECTS-------
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2)) #second col is twice of first
    with image_column:
        # st.image(img_contact_form)
        pass
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use lottie files in Streamlit
            - Markdown supported
            - List 2
            """
        )
        st.markdown("[Watch Videos]()")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        # st.image(img_contact_form)
        pass
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use lottie files in Streamlit
            - Markdown supported
            - List 2
            """
        )
        st.markdown("[Watch Videos]()")


# ----CONTACT FORM ---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me")

    contact_form = """
        <form action="https://formsubmit.co/01937c08c49936bd5a35d4f3f81da0ef" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Enter your name" required>
            <input type="email" name="email" placeholder="Enter your email" required>
            <textarea name="message" placeholder="Your message here..." required></textarea>
            <button type="submit" class="button button2">Send</button>
        </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.write("""
            Dropping a line to say hi:wave:, ask for my resume or see if we can build something together? I'd :sparkling_heart: to hear from you!
        """)
        st.write("##")
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
