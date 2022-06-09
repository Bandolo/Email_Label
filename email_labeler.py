# Below is the function to classify the emails as either "Student wants to know if can share"
# or "Student has shared"

def email_label(share, email):
    '''
      Checks email and returns whether an email was shared or there was an intention to share the email.

        Args:
            share (str): The word "share" which will be used to check if found in the "email"
            email (str): The email to be checked if the word "share" appears in it or not

        Returns:
            1. Student has shared: A String
            2. Student wants to know if can share: A String
    '''
    email_words = email.split()
    response = "Student wants to know if can share" if share in email_words else "Student has shared"

    return response


