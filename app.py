from flask import Flask, request, render_template, redirect, url_for  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html')

@app.route('/math', methods=['GET', 'POST'])
def math():
        if request.method == 'POST':
            form = request.form
            radius = int(form['radius'])
            height = int(form['height'])
            pi = float(3.14)
            print(radius)
            print(height)
            Top_Area = pi*(radius)**2
            print(Top_Area)
            Side_Area = 2*(pi*(radius*height))
            print(Side_Area)
            Total_Area = Top_Area+Side_Area
            print(Total_Area)
            Total_AreaSQF = Total_Area/144
            print(Total_AreaSQF)
            Material_Cost = Total_AreaSQF*25
            print(Material_Cost)
            Labor_Cost = Total_AreaSQF*15
            print(Labor_Cost)
            Total_Cost = Material_Cost + Labor_Cost
            print(Total_Cost)
            return render_template('estimate.html', quote=Total_Cost)
        return render_template('estimate.html')

if __name__ == '__main__':
    app.run(debug=True)