from openai import OpenAI

client = OpenAI(api_key="sk-WXFwDH1tvXskFJ8O46cXpJcL42dhbuNFm2")


def generate_blog(selected_option):
    """"
    This functions uses chatGPT to dynamically create mail contents based on user input
    """

    # prompt = f"Write a 200-word blog post about {selected_option} and provide it in email HTML format."
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=prompt,
    #     max_tokens=200,
    #     temperature=0.7
    # )
    if selected_option == "Wine":
        # Blog about wine
        email_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Discover the World of Fine Wines</title>
        </head>
        <body>
            <p>Dear Wine Enthusiast,</p>

            <p>Indulge your senses and embark on a journey through the exquisite world of fine wines with us. Our carefully curated selection of wines awaits your discerning palate, promising a delightful experience with every sip.</p>

            <p>From rich reds that dance on your taste buds to crisp whites that refresh the soul, our collection celebrates the diversity and complexity of wines from renowned vineyards around the globe.</p>

            <p>Whether you're a seasoned connoisseur or just beginning to explore the wonders of wine, we have something special for you. Join us in celebrating life's moments with the perfect bottle.</p>

            <p>Visit our store today and elevate your wine experience to new heights. Cheers to the joy of discovery!</p>

            <p>Best regards,</p>
            <p>Your Wine Aficionados</p>
        </body>
        </html>
        """
    else:
        email_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Discover Our Podcast Channel</title>
        </head>
        <body>
            <p>Dear Podcast Enthusiast,</p>

            <p>Exciting news! Dive into the world of captivating conversations and thought-provoking discussions by subscribing to our podcast channel. We bring you a mix of engaging topics, insightful interviews, and entertaining content that will enrich your listening experience.</p>

            <p>Whether you're into inspiring stories, industry insights, or just looking for a good laugh, our podcast has something for everyone. Tune in and join our community of listeners who are exploring, learning, and enjoying the power of audio storytelling.</p>

            <p>Don't miss out on the latest episodes. Subscribe now and stay connected with the pulse of our podcast channel. It's time to turn up the volume and embark on a journey of discovery!</p>

            <p>Thank you for being part of our podcast family!</p>

            <p>Best regards,</p>
            <p>Your Podcast Team</p>
        </body>
        </html>
        """
    return email_html
