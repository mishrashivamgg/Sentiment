import streamlit as st
from textblob import TextBlob
st.sidebar.title("about us")
st.sidebar.text("we are student at Ducat ")


st.sidebar.title("Contact us")
st.sidebar.text("""monu @1111
sonu @2222
monu @3333""")

st.title("Sentiment Analysis")

text=st.text_input("**enter text**")
btn=st.button("predict")

if btn:
    blob=TextBlob(text)
    sent=blob.sentiment[0]
    if sent<0:
        st.error("Negative Sentiment")
        st.image("Neg.jpg")
    elif sent>0:
        st.success("Possitive Sentiment")
        st.image("pos.jpg")
    else:
        st.warning("Neutral Sentiment")
        st.image("neu.jpg")









    
