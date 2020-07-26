from flask import Flask, render_template, url_for, request
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def name(page_name):
    return render_template(page_name)


def writetofile(datatorecieve):
    with open('./database.txt', 'a') as f:
        email = datatorecieve["email"]
        subject = datatorecieve["subject"]
        message = datatorecieve["message"]
        file = f.write(
            f'\nemail: {email},subject: {subject},message: {message}')
        f.close()


def writetocsv(data):
    with open('./database.csv', 'a', newline='',) as f2:
        try:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            csv_writer = csv.writer(
                f2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, subject, message])
            f2.close()
        except:
            return "can't send data from the server."


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            writetofile(data)
            writetocsv(data)
            return 'form submitted'
        except:
            return "can't send data from the server."
    else:
        return 'something went wrong, try again'


if __name__ == "__main__":
    app.run(debug=True)
