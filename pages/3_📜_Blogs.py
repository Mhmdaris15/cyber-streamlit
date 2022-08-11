import streamlit as st
import PIL

logo = PIL.Image.open("img/wordpress-48.png")
st.set_page_config(page_title="Blogs Page | Cybersecurity", page_icon=logo)

with st.container():
    processor, title_text, artificial = st.columns([1,3,1])

    processor.image("img/processor-64.png", width=64)
    artificial.image("img/artificial-64.png", width=70)

    title_text.markdown("""
    <div class="header-logo" style="display: flex; justify-content:space-around; align-items:center;">
            <img src="./img/processor-64.png" alt="">
            <h3><span style="color: red;">Cyber</span>-<span>Security</span></h3>
            <img src="./img/artificial-64.png" alt="">
    </div>
    """,unsafe_allow_html=True)

    st.markdown("""
        <h1 class="title" style='text-align: center;'>Welcome to Our Blog!</h1>
        <div class="des-title" style='text-align: center;'>We made several blog posts to educate People about Cybersecurity and how it's can be really vulnerable</div>
        <br><br>
    """, unsafe_allow_html=True)

    st.image("img/neon-cybersecurity.jpg")

blog1, blog2, blog3, blog4 = st.tabs(["What is Phising Attack really means? ", "How Dangerous DDoS attacks are?", "What is Carding?", "What is DOM XSS Attack?"])

with blog1:
    st.markdown("""
        <h1 class="title" style='text-align: center;'>📝 Blog 1</h1>
        <div class="des-title" style='text-align: center;'>This is a blog post about Phising Attack and how it's can be really vulnerable</div>
        <br><br>
    """, unsafe_allow_html=True)

    st.image("img/phising.jpg")

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

    st.image("img/ddos-attack.jpg")

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
        <div class="des-title" style='text-align: center;'>This is a blog post about Cardig and how it's can be really vulnerable</div>
        <br><br>
    """, unsafe_allow_html=True)

    st.image("img/carding.jpg")

    st.markdown("""
    ## What is Carding? - Carding Meaning
    Carding is also known as credit card stuffing or card verification. It is a web security threat in which attackers attempt to authorize stolen credit card credentials and use them to charge prepaid cards or gift cards. These cards are then sold or used to make purchases of goods, which can then be sold for cash.
    \n\n
    People who are involved in Carding are called carders. Carding is performed with the help of bots and hacking software, which is capable of performing automated operations over the internet. The objective is to identify card numbers or details that can be used to perform purchases.
    \n\n
    The United States is a high target for carding credit and debit cards. This is because the United States has a large market for cards that contain magnetic strips or chips and signature technology, unlike the more secure chip and PIN technology.

    ### Carding Examples
    An example of carding was when hackers built a malicious bot named GiftGhostBot. The purpose of this bot was to hack the balances of gift cards. Around 1,000 e-commerce websites became victims of this carding attack. The advanced, persistent bot checks millions of gift card numbers automatically to identify the ones with balances. This bot is still attacking websites.
    \n\n
    The validated gift card numbers are used to make purchases. This card cracking or token cracking attack is, typically, untraceable once the balance is stolen.
    
    ### Carding Attack Process\n
    A carding attack process typically involves the following steps:\n
    - Carders obtain stolen credit card numbers from criminal marketplaces, compromised websites, or payment channels.
    - Carders then deploy bots to make small purchases on several sites. In every attempt, a card number is tested against a merchant’s payment processes to determine the validity of card details.
    - The validation process is attempted thousands of times until it yields results.
    - The acquired card numbers that are successfully validated are then organized into a list and used for other criminal activities or sold to organized criminal outfits.
    - Carding is undetectable by card owners until it is too late and their money is stolen.
    """)

with blog4:
    st.markdown("""
        <h1 class="title" style='text-align: center;'>📝 Blog 4</h1>
        <div class="des-title" style='text-align: center;'>This is a blog post about XSS Attacks and how it's can be really vulnerable</div>
        <br><br>
    """, unsafe_allow_html=True)

    st.image("img/hacker-nuclear.jpg")

    st.markdown("""
    ## What is DOM XSS? - the basics
    Document Object Model (DOM) cross-site scripting (XSS) is a web application vulnerability that allows attackers to manipulate the DOM environment in a user's browser by injecting malicious client-side code. In contrast to reflected or stored XSS, where the vulnerability is caused by server-side flaws and the payload is reflected in the response, DOM XSS is purely client-side.
    \n\n
    DOM XSS vulnerabilities are mainly attributed to situations where user-controllable sources pass data to sinks, such as `eval()`, `document.write`, or `innerHTML`. These sinks allow for dynamic code execution.

    ### Quick brief on the DOM
    The DOM is an integral part of modern web applications, as it allows web applications to dynamically manipulate objects without making another trip back to the server. It works by representing data in nodes and objects for a web page in a hierarchical structure so that programming languages can interact with the page. The DOM's purpose is to allow web applications to modify their data by addressing each object on the page. Objects can be the actual content, styling or scripts, or data stored in a user’s browser that the website might need to access, such as cookies.
    \n\n


    """)