from supabase import create_client
import pandas as pd
import streamlit as st

# Set your Supabase credentials
supabase = create_client(st.secrets.database.supabase_url, st.secrets.database.supabase_key)


def insert_user(email):
    # Check if the email exists
    response = supabase.table("users").select("*").match({'email':email}).execute()

    if len(response.data) > 0:
        # If the email exists, increment the "emails_sent" column
        supabase.table("users").update({"emails_sent": response.data[0]["emails_sent"]+1}).eq('id',response.data[0]['id']).execute()
        print(f"User with email {email} already exists. Incremented 'emails_sent'.")
    else:
        # If the email doesn't exist, insert the user into the "users" table
        data = {"email": email, "emails_sent": 1}
        supabase.table("users").insert([data]).execute()
        print(f"User with email {email} inserted into the 'users' table.")


def construct_df():
    response = supabase.table("users").select("*").execute()

    # Convert the data to a Pandas DataFrame
    data = response.data
    df = pd.DataFrame(data)

    return df