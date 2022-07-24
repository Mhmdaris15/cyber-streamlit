import streamlit as st

st.sidebar.markdown("# Home page 🎈")

processor, nevtik_text, nevtik = st.columns([1,3,1])

processor.image("images/processor-64.png", width=64)
nevtik.image("images/logo-nevtik.png", width=70)

nevtik_text.markdown("""
<div class="header-logo" style="display: flex; justify-content:space-around; align-items:center;">
        <img src="./images/processor-64.png" alt="">
        <h3><span style="color: red;">NEV</span>-<span>TIK</span></h3>
        <img src="./images/logo-nevtik.png" alt="">
   </div>
""",unsafe_allow_html=True)

st.markdown("""
    <h1 class="title" style='text-align: center;'>Todays, Cybersecurity is absolutely Crucial!</h1>
    <div class="des-title" style='text-align: center;'>Finance, IT, Business, Education, and many more... NEED to be protected!</div>
    <br><br>
""", unsafe_allow_html=True)

st.image("images/sunset-nature-landscape.jpg")

# ! IMAGE AND DESCRIPTION AREA ###########################################################################################

phising_text, phising_img = st.columns(2)

with phising_img:
    st.image("images/phising.jpg", caption="Phising Attactk", use_column_width=True)
    

with phising_text:
    st.markdown(f"""
        <div class="phising-text" style="text-align:center; margin-top:20%;">Phishing is a type of social engineering where an attacker sends a fraudulent message designed to trick a person into revealing sensitive information to the attacker or to deploy malicious software on the victim's infrastructure like ransomware.</div>
    </div>
    """, unsafe_allow_html=True)

carding_text, carding_img = st.columns(2)


with carding_img:
    st.image("images/carding.jpg",  caption="Carding Attactk", use_column_width=True)

with carding_text:
    st.markdown(f"""
        <div class="carding-text" style="text-align:center; margin-top:20%;">Carding (also known as credit card stuffing and card verification) is a web security threat in which attackers use multiple, parallel attempts to authorize stolen credit card credentials</div>
    </div>
    """, unsafe_allow_html=True)

# ! SMALL IMAGE AND DESCRIPTION AREA ###########################################################################################

hacker1, hacker2, hacker3 = st.columns(3)
text_hacker1, text_hacker2, text_hacker3 = st.columns(3)

with hacker1:
    st.write("### Hacker 1")
    st.image("images/hacker-1.jpg", width=200, caption='First Hacker')

with hacker2:
    st.write("### Hacker 2")
    st.image("images/hacker-2.jpg", width=200, caption='Second Hacker')

with hacker3:
    st.write("### Hacker 3")
    st.image("images/hacker-nuclear.jpg", width=200, caption='Third Hacker')

with text_hacker1:
    st.markdown("lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem, quisquam. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem, quisquam.")

with text_hacker2:
    st.markdown("lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem, quisquam. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem, quisquam.")

with text_hacker3:
    st.markdown("lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem, quisquam. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem, quisquam.")

# ! EXPANDER ##############################################################################################################
with st.expander("How to Surfing on Internet safely?"):
    st.image('images/server-48.png')
    st.markdown("""
    1. Use strong passwords. ...
    2. Be careful with phishing emails. ...
    3. Be careful opening email attachments. ...
    4. Don't click on pop-ups. ...
    5. Don't use your browser to store your passwords. ...
    6. Don't give out your personal information. ...
    7. Use Two-Factor-Authentication every time you can.
    """)


with st.expander("Is it easy to be craced by Hacker?"):
    st.image('images/nas-48.png')
    st.write("They have advanced knowledge of programming languages and computer OS. Hackers are very skilled and intelligent people. These people may be skilled. But most of the time, they don't even need extensive skills. Some crackers only have a knowledge of a few illegal tricks that help them in stealing data.")

with st.expander("How can my Data be stolen?"):
    st.image('images/c-drive-48.png')
    st.write("Many online services require users to fill in personal details such as full name, home address and credit card number. Criminals steal this data from online accounts to commit identity theft, such as using the victim's credit card or taking loans in their name.")
