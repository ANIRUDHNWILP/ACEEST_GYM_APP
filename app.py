from flask import Flask, render_template, request, redirect, url_for

app = Flask(__ACEEST__)

# In-memory database for members
members = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/plans')
def plans():
    # Example membership plans
    membership_plans = [
        {"name": "Basic Plan", "price": "₹500/month"},
        {"name": "Standard Plan", "price": "₹1000/month"},
        {"name": "Premium Plan", "price": "₹1500/month"}
    ]
    return render_template('plans.html', plans=membership_plans)

@app.route('/members', methods=['GET', 'POST'])
def manage_members():
    if request.method == 'POST':
        # Add a new member
        name = request.form.get('name')
        age = request.form.get('age')
        plan = request.form.get('plan')
        if name and age and plan:
            members.append({"name": name, "age": age, "plan": plan})
            return redirect(url_for('manage_members'))
    return render_template('members.html', members=members)

if __name__ == '__main__':
    app.run(debug=True)
