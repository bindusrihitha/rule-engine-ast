from flask import Flask, request, render_template
from models import db, Rule
from utils import create_rule, evaluate_rule

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()  # Create the database tables

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rule_name = request.form['rule_name']  # Retrieve the rule name
        rule_condition = request.form['rule_condition']  # Retrieve the rule condition
        rule_action = request.form['rule_action']  # Retrieve the rule action
        
        # Create a rule from the submitted condition
        rule_node = create_rule(rule_condition)  # Assuming you only need the condition for rule creation
        
        # Store the rule in the database
        new_rule = Rule(rule_string=rule_condition)  # Adjust if your Rule model needs different attributes
        db.session.add(new_rule)
        db.session.commit()
        
        # Evaluate the rule with sample data
        sample_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        
        if rule_node is None:
            result = "Error: Invalid rule syntax."
        else:
            result = evaluate_rule(rule_node, sample_data)

        return render_template('index.html', result=result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
