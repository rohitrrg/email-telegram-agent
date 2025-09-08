from reply_generator import generate_reply

context = """Alice invited you to a project review meeting scheduled for Friday at 3:00 PM. 
She requests confirmation of your attendance."""
shorthand = "yes confirm"

print(generate_reply(context, shorthand))
