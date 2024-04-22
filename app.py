from flask import Flask, render_template, request

app = Flask(__name__)

# Initial setpoint and deadband values
setpoint = 70
deadband = 2
heating_output = 0
cooling_output = 0
enable_control = False
user_overrides = {
    'setpoint': False,
    'deadband': False,
    'heating_output': False,
    'cooling_output': False,
    'enable_control': False
}

@app.route('/', methods=['GET', 'POST'])
def index():
    global setpoint, deadband, heating_output, cooling_output, enable_control, user_overrides

    if request.method == 'POST':
        if 'setpoint' in request.form:
            setpoint = float(request.form['setpoint'])
            user_overrides['setpoint'] = True
        if 'deadband' in request.form:
            deadband = float(request.form['deadband'])
            user_overrides['deadband'] = True
        if 'heating_output' in request.form:
            heating_output = int(request.form['heating_output'])
            cooling_output = 0 if heating_output > 0 else cooling_output
            user_overrides['heating_output'] = True
        if 'cooling_output' in request.form:
            cooling_output = int(request.form['cooling_output'])
            heating_output = 0 if cooling_output > 0 else heating_output
            user_overrides['cooling_output'] = True
        if 'enable_control' in request.form:
            enable_control = True if request.form['enable_control'] == 'on' else False
            user_overrides['enable_control'] = True

    return render_template('index.html', setpoint=setpoint, deadband=deadband, heating_output=heating_output,
                           cooling_output=cooling_output, enable_control=enable_control, user_overrides=user_overrides)

if __name__ == '__main__':
    app.run(debug=True)
