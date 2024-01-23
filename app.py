from PIL import Image
import streamlit as st
import requests
from jsonschema._keywords import required
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# set basic configeration of the page
st.set_page_config(page_title="Sachin WebPage - Welcome!", page_icon="🐥", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        print("Error in URL")
        return None
    return r.json()


# use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# --------- LOAD ASSET ------------------------
lottie_coding = load_lottieurl(
    "https://lottie.host/bdcbcb7c-160f-4c79-b765-df31af7a72a3/CDgeDLZfK9.json"
)


# --------- HEADER SECTION ----------------------
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hi, I am Sachin Bharadwaj :wave:")
        #st.title("Systems Engineer from India!")
        st.write(
            "Passionate about signal processing, Estimation, Detection, mmWave Radars, machine learning, deep learning"
        )
        st.write("[LinkedIn > ](https://www.linkedin.com/in/sachin-bharadwaj-3518881/)")
        st.write("[Github > ](https://github.com/Sachin-Bharadwaj)")

    with right_column:
        st_lottie(
            lottie_coding,
            height=300,
            width=300,
            loop=True,
            quality="high",
            key="coding",
        )
st.write("---")

with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Projects", "Contact"],
        icons=["code-slash", "chat-left-text-fill"],
        orientation="horizontal",
    )

vit_mnsit_attnmap = Image.open("./assets/attnmaps-mnist.jpg")
vit_mnsit_preds = Image.open("./assets/predictions-mnist.jpg")
minigpt_sampletext = Image.open("./assets/sample-result-miniGPT.jpg")
babyllama_sampletext = Image.open("./assets/BabyLlama.jpg")
seogen_sample = Image.open("./assets/SEOGen.jpg")
seogen_sample = seogen_sample.resize((800,800))
pdfchat_sample = Image.open("./assets/PDF-Chat.jpg")
pdfchat_sample = pdfchat_sample.resize((800,800))
seg_sample = Image.open("./assets/sementicseg.jpg")

if selected == "Projects":
    with st.container():
        st.write("---")
        st.header("My Recent Projects")
        st.write("##")
        ## ---------- Project 1 ----------------------------------------------<<
        image_column, text_column = st.columns((1, 2))
        with image_column:
            # insert image
            st.image(vit_mnsit_attnmap)

        with text_column:
            st.subheader("Vision Transformer on MNIST")
            st.write(
                """
                Classify MNIST using VIT architecture. Analyze the attention map (shown on left) learned by VIT. We further discuss on how to design your fixed positional embeddings
                """
            )
            st.markdown("[VIT-MNIST >](https://github.com/Sachin-Bharadwaj/VIT-MNIST/tree/main)")
        # ------------------------------------------------------------------------->>

        ## ---------- Project 2 ----------------------------------------------<<
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(minigpt_sampletext)

        with text_column:
            st.subheader("mini GPT trained on Great Expectations by Charles Dickens")
            st.write(
                """
                Trained miniGPT (auto-regressive causal language model) on characters as token. Training set is Great Expectations written by Charles Dickens. Model has ~6.4M params, data is ~1M tokens, vocab size 78, context window: 256 token, 8 heads self attention.
                """
            )
            st.markdown("[miniGPT >](https://github.com/Sachin-Bharadwaj/miniGPT)")
        # ------------------------------------------------------------------------->>

        ## ---------- Project 3 ----------------------------------------------<<
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(babyllama_sampletext)

        with text_column:
            st.subheader("Baby Llama trained on Entire Work of Shakespare")
            st.write(
                """
                Trained Baby Llama for text generation. Architecture is RoFormer with Rotational positional embedding and grouped-query attention.
                Inference done using KV cache
                """
            )
            st.markdown("[BabyLlama >](https://github.com/Sachin-Bharadwaj/BabyLlama)")
        # ------------------------------------------------------------------------->>

        ## ---------- Project ChatBots ----------------------------------------------<<
        chatbot_container = st.container()
        with chatbot_container:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.image(seogen_sample)
                st.subheader("SEO Generator using GPT")
                st.write(
                    """
                    Returns SEO content for a given keyword in given style and word count
                    """
                )
                st.markdown("[SEOGen >](https://github.com/Sachin-Bharadwaj/ChatBots)")

            with col2:
                st.image(pdfchat_sample)
                st.subheader("Chat with PDF docs using GPT")
                st.write(
                    """
                    Returns the answers to the questions grounded in the uploaded pdf doc
                    """
                )
                st.markdown("[PDFChat >](https://github.com/Sachin-Bharadwaj/ChatBots)")

        ## ---------- Project SementicSeg/InvDepth using MultiTask ----------------------------------------------<<
        seg_container = st.container()
        with chatbot_container:
            col1, col2 = st.columns(2)
            with col1:
                st.image(seg_sample)
                st.subheader("Sementic Segmentation")
                st.write(
                    """
                    DeepLabv3 architecture with resenet18 backbone, mIOU>84%
                    """
                )
                st.markdown("[SEOGen >](https://github.com/Sachin-Bharadwaj/SementicSegmentation)")

            with col2:
                #st.image(pdfchat_sample)
                st.subheader("Inv Depth")
                st.write(
                    """
                    Inverse Depth on Synscapes dataset, Work in Progress
                    """
                )
                st.markdown("[PDFChat >](https://github.com/Sachin-Bharadwaj/SementicSegmentation)")





if selected == "Contact":
    # ------- CONTACT -----------
    with st.container():
        st.write("---")
        st.header("Get in Touch with Me!")
        st.write("##")

        #
        contact_form = """
        <form action = "https://formsubmit.co/sachin.bharadwaj@email.com" method = "POST" >
            <input type="hidden" name="_captcha" value="false">
            <input type ="text" name="name" placeholder="Your name" required>
            <input type ="email"  name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form >
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
