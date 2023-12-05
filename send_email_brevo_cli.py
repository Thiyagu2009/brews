import requests

api_key = "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"

def send_transactional_email(sender_name, sender_email, recipient_name, recipient_email, subject, html_content):
    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json",
    }

    data = {
        "sender": {
            "name": sender_name,
            "email": sender_email
        },
        "to": [
            {
                "email": recipient_email,
                "name": recipient_name
            }
        ],
        "subject": subject,
        "htmlContent": html_content
    }

    response = requests.post(url, headers=headers, json=data)

    return response.status_code, response.json()


import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = api_key

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
# start_date = '2020-10-01'
# end_date = '2020-10-15'
#tag = 'tag_example'

def email_events():


    try:
        api_response = api_instance.get_aggregated_smtp_report()#start_date=start_date, end_date=end_date, tag=tag)
        pprint(api_response)
        return api_response

    except ApiException as e:
        print("Exception when calling SMTPApi->get_aggregated_smtp_report: %s\n" % e)
