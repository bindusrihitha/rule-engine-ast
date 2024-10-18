from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Rule {self.id}: {self.rule_string}>"
