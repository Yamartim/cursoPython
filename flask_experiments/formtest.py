from flask import Flask, request, render_template
from csv import writer

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def formtocsv():

    if request.method == "POST":

        form = request.form.listvalues()
        with open('dados.csv', 'a') as file:
            #file.writelines(form)
            escritor = writer(file)
            escritor.writerow(form)

        return render_template('profile.html')

    return render_template('profile.html')


if __name__ == '__main__':
    app.run()

