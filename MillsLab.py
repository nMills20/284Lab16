from flask import Flask, render_template
from gpiozero import LED

app = Flask(__name__)
led = LED(18)

@app.route('/')
def index():
    return render_template('HTML Code.html')

@app.route('/toggle/<action>')
def LEDControl(action):
    if action == 'on':
        led.on()
        return 'LED Turned On'
    elif action == 'off':
        led.off()
        return 'LED Turned Off'
    
    if __name__ == '_main_':
        app.run(host='192.168.1.20', port=80)