# Save ChatGPT

Quickly save your ChatGPT chat to text.

This entire app was written with the aid of ChatGPT by asking 
it questions on how to code it. 

The entire process took less than ~15mins

Fun experimental research

# Usage

go to https://chat.openai.com/chat

Open Chrome dev tools

Page in the 'console' tab:

```
function savechat() {

  let body = document.body.innerHTML;

  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://127.0.0.1:5000/save');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify({ body: body }));

}
```

Open a terminal, and run this flask app in on your local computer:

```
python3 -m venv venv
. venv/bin/activate
pip install flask
FLASK_DEBUG=1 flask run
```
That will start flask running in the background.

# How to save a chat

with the flask app running and the javascript pasted into chrome dev tools console:

1. Start a chat at https://chat.openai.com/chat
2. Open chrome dev tools
3. Call the 'savechat()' function
4. Your conversion is saved to file on your local computer.


# Help

If you get stuck, ask https://chat.openai.com/chat how to do it ;) 