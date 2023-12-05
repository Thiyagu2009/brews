from supabase import create_client
import pandas as pd

# Set your Supabase credentials
supabase_url = "https://ppjbgzzpfcnjiowdxyld.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBwamJnenpwZmNuamlvd2R4eWxkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwMTc1NTM3MiwiZXhwIjoyMDE3MzMxMzcyfQ.wjAxhuO-8jC6AXDeOxjkP-FeeDUgzpfmrbum1M4Grio"
supabase = create_client(supabase_url, supabase_key)


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