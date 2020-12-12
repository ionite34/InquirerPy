from InquirerPy import prompt

questions = [
    {
        "type": "confirm",
        "name": "hello",
        "message": "Proceed?",
        "default": True,
        "qmark": "?",
    },
    {
        "type": "confirm",
        "name": "foo",
        "message": "Are you sure?",
        "when": lambda result: result["hello"] == True,
    },
]

print(prompt(questions))
