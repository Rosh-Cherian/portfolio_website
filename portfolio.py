import streamlit as st
import google.generativeai as genai
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1,col2=st.columns(2)
with col1:
    st.subheader('Hello :wave:')
    st.title('I am Rosh Cherian')
with col2:
    st.image("images/my_picture.png")

persona = """
        You are Rosh AI bot. You help people answer questions about your self (i.e Rosh)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Rosh: 
         
        Rosh Cherian is a 4th year B.Tech student in Computer Science at Sree Chitra Thirunal College of Engineering
        concurrently specialising in Machine Learning through an Honours program and Mechatronics as a Minor degree.
        Rosh completed his schooling at St.Marys's Central School with a score 95.4 in Computer Science.
        Rosh has been volunteering several student clubs including IEEE,GDSC,CSI,IEDC,etc. Rosh is currently the content lead of IEEE SCT SB.

 
        Rosh's Email: roshcherian03@gmail.com 
        Rosh's Linkdin: https://www.linkedin.com/in/rosh-cherian/
        Rosh's Github :https://github.com/Rosh-Cherian
        """
st.title("Rosh's AI Bot")
userquestion=st.text_input("Ask anything about me")
if st.button("ASK",use_container_width=400):
    prompt = persona +"Here is the question that the user asked: " +  userquestion
    response=model.generate_content(prompt)
    st.write(response.text)

#col1,col2=st.columns(2)
#with col1:
#    st.subheader("LinkedIn")
#    st.write("- world class kidilam")

st.title("My Skills")
st.slider("Programming",0,100,70)
st.slider("Problem Solving",0,100,95)
st.file_uploader("Upload a file(may be a letter which you think i should read)")
st.write("Contact")
st.subheader("roshcherian03@gmail.com")