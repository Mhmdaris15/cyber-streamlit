from turtle import width
import streamlit as st

with st.container():
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
        <h1 class="title" style='text-align: center;'>Welcome to Our Blog!</h1>
        <div class="des-title" style='text-align: center;'>We made several blog posts to educate People about Cybersecurity and how it's can be really vulnerable</div>
        <br><br>
    """, unsafe_allow_html=True)

    st.image("images/neon-cybersecurity.jpg")

blog1, blog2, blog3 = st.tabs(["What is Phising Attack really means? ", "How Dangerous DDoS attacks are?", "What is Carding?"])

with blog1:
    st.markdown("""
        <h1 class="title" style='text-align: center;'>📝 Blog 1</h1>
        <div class="des-title" style='text-align: center;'>This is a blog post about Carding and how it's can be really vulnerable</div>
        <br><br>
    """, unsafe_allow_html=True)

    st.image("images/phising.jpg")

    st.markdown("""
    ### What is Phising?
    Phishing attacks are counterfeit communications that appear to come from a trustworthy source but which can compromise all types of data sources. Attacks can facilitate access to your online accounts and personal data, obtain permissions to modify and compromise connected systems--such as point of sale terminals and order processing systems--and in some cases hijack entire computer networks until a ransom fee is delivered.
    \n\n
    Sometimes hackers are satisfied with getting your personal data and credit card information for financial gain. In other cases, phishing emails are sent to gather employee login information or other details for use in more malicious attacks against a few individuals or a specific company. Phishing is a type of cyber attack that everyone should learn about in order to protect themselves and ensure email security throughout an organization.
    
    ### How does phishing work?
    Phishing starts with a fraudulent email or other communication designed to lure a victim. The message is made to look as though it comes from a trusted sender. If it fools the victim, he or she is coaxed into providing confidential information--often on a scam website. Sometimes malware is also downloaded onto the target's computer.
    \n\n
    Cybercriminals start by identifying a group of individuals they want to target. Then they create email and text messages that appear to be legitimate but actually contain dangerous links, attachments, or lures that trick their targets into taking an unknown, risky action. In brief:
    \n\n
    - Phishers frequently use emotions like fear, curiosity, urgency, and greed to compel recipients to open attachments or click on links.
    - Phishing attacks are designed to appear to come from legitimate companies and individuals.
    - Cybercriminals are continuously innovating and becoming more and more sophisticated.
    - It only takes one successful phishing attack to compromise your network and steal your data, which is why it is always important to Think Before You Click.

    """)

with blog2:
    st.markdown("""
        <h1 class="title" style='text-align: center;'>📝 Blog 2</h1>
        <div class="des-title" style='text-align: center;'>This is a blog post about DDos Attacks and how it's can be really vulnerable</div>
        <br><br>
    """, unsafe_allow_html=True)

    st.image("images/ddos-attack.jpg")

    st.markdown("""
    ## What is a DDoS Attack? - DDoS Meaning
    Distributed Network Attacks are often referred to as Distributed Denial of Service (DDoS) attacks. This type of attack takes advantage of the specific capacity limits that apply to any network resources – such as the infrastructure that enables a company’s website. The DDoS attack will send multiple requests to the attacked web resource – with the aim of exceeding the website’s capacity to handle multiple requests… and prevent the website from functioning correctly.
    \n\n
    Typical targets for DDoS attacks include:
    \n\n
    - Internet shopping sites
    - Online casinos
    - Any business or organisation that depends on providing online services

    ### How a DDoS attack works?
    Network resources – such as web servers – have a finite limit to the number of requests that they can service simultaneously. In addition to the capacity limit of the server, the channel that connects the server to the Internet will also have a finite bandwidth / capacity. Whenever the number of requests exceeds the capacity limits of any component of the infrastructure, the level of service is likely to suffer in one of the following ways:
    \n\n
    - The response to requests will be much slower than normal.
    - Some – or all – users’ requests may be totally ignored.

    """)
with blog3:
    st.markdown("""
        <h1 class="title" style='text-align: center;'>📝 Blog 2</h1>
        <div class="des-title" style='text-align: center;'>This is a blog post about DDos Attacks and how it's can be really vulnerable</div>
        <br><br>
    """, unsafe_allow_html=True)

    st.image("images/hacker-nuclear.jpg")

    st.markdown("""
    ## What is a DDoS Attack? - DDoS Meaning
    Distributed Network Attacks are often referred to as Distributed Denial of Service (DDoS) attacks. This type of attack takes advantage of the specific capacity limits that apply to any network resources – such as the infrastructure that enables a company’s website. The DDoS attack will send multiple requests to the attacked web resource – with the aim of exceeding the website’s capacity to handle multiple requests… and prevent the website from functioning correctly.
    \n\n
    Typical targets for DDoS attacks include:
    \n\n
    - Internet shopping sites
    - Online casinos
    - Any business or organisation that depends on providing online services

    ### How a DDoS attack works?
    Network resources – such as web servers – have a finite limit to the number of requests that they can service simultaneously. In addition to the capacity limit of the server, the channel that connects the server to the Internet will also have a finite bandwidth / capacity. Whenever the number of requests exceeds the capacity limits of any component of the infrastructure, the level of service is likely to suffer in one of the following ways:
    \n\n
    - The response to requests will be much slower than normal.
    - Some – or all – users’ requests may be totally ignored.

    """)
