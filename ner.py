import spacy

nlp = spacy.load("en_core_web_sm")

def extract_task_details(email_body):
    doc = nlp(email_body)
    tasks = []

    for sent in doc.sents:
        action = None
        owner = None
        deadline = None

        for token in sent:
            if token.dep_ == "ROOT":  # Main verb
                action = token.text
            elif token.ent_type_ == "PERSON":  # Named entity
                owner = token.text
            elif token.ent_type_ == "DATE":
                deadline = token.text
        
        if action:
            tasks.append({
                "Action": action,
                "Owner": owner,
                "Deadline": deadline
            })
    
    return tasks

email = "John, can you finalize the project proposal by next week?"
print(extract_task_details(email))
