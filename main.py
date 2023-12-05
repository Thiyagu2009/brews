import time

import streamlit as st

from chatgpt import generate_blog
from send_email_brevo_cli import send_transactional_email, email_events
from supaops import insert_user, construct_df


def main():
   render_input_page()


def render_input_page():
    st.title("Brewsy Email Campaign Dashboard")

    # Text input
    recepient_email = st.text_input("Enter Email")

    # Select box
    options = ["Podcast", "Wine"]
    interest = st.selectbox("Select your area of interest:", options)
    btn_result = st.button("Send Email")
    if btn_result:
        insert_user(recepient_email)
        send_brevo_email(recepient_email, interest, generate_blog(interest))

    st.subheader("User & Stats")
    st.dataframe(construct_df())

    st.subheader("Email Stats last 90 days")

    col1, col2, col3, col4 = st.columns(4)
    while(True):
        construct_email_events_metrics(col1, col2, col3, col4)
        time.sleep(600)


def construct_email_events_metrics(col1, col2, col3, col4):
    email_events_response = email_events()

    col1.metric("Requested", email_events_response.requests)
    col2.metric("Delivered", email_events_response.delivered)
    col3.metric("Opened", email_events_response.opens)
    col4.metric("Unique Opens", email_events_response.unique_opens)


def send_brevo_email(recipient_email, interest, selected_option):
    sender_name = "Brewsy"
    sender_email = "thiyagu.nataraj@gmail.com"
    recipient_name = "John Doe"
    subject = "Dear {0} enthisiast!".format(interest)

    status_code, response_json = send_transactional_email(sender_name, sender_email, recipient_name,
                                                          recipient_email, subject, generate_blog(selected_option))

    print("Status Code:", status_code)
    print("Response:")
    print(response_json)


if __name__ == "__main__":
    main()