from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import json
import sys
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jump_data.db'
db = SQLAlchemy(app)

class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    diff = db.Column(db.String(20))
    tier = db.Column(db.String(20))
    server = db.Column(db.String(50))
    links = db.Column(db.String(500))
    founder = db.Column(db.String(100))
    line = db.Column(db.String(200))
    prover = db.Column(db.String(100))
    likes = db.Column(db.String())
    dislikes = db.Column(db.String())

    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location,
            'diff': self.diff,
            'tier': self.tier,
            'server': self.server,
            'links': self.links.split(',') if self.links else [],
            'founder': self.founder,
            'line': self.line,
            'prover': self.prover,
            'likes': self.likes,
            'dislikes': self.dislikes
        }

@app.route('/api/jumps', methods=['GET', 'POST'])
def handle_levels():
    if request.method == 'POST':
        criteria = request.get_json()
        filtered_data = filter_levels(criteria)
        return jsonify(filtered_data)
    else:
        levels = Level.query.all()
        data = [level.to_dict() for level in levels]
        return jsonify(data)

def filter_levels(criteria):
    query = Level.query
    for key, value in criteria.items():
        if key == 'links':
            query = query.filter(Level.links.like(f'%{value}%'))
        else:
            query = query.filter(getattr(Level, key) == value)
    levels = query.all()
    filtered_data = [level.to_dict() for level in levels]
    return filtered_data

import json

def update_dataset():
    url = 'https://raw.githubusercontent.com/JoniKauf2/Jumpedia/main/data/jump_data.json'
        # Send a GET request to fetch the webpage content
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the visible text elements
    visible_text = soup.find_all(string=True)

    # Filter out any unwanted elements such as scripts, styles, or hidden text
    visible_text = [text.strip() for text in visible_text if text.parent.name not in ['script', 'style', 'hidden']]

    # Join the extracted visible text into a single string
    visible_text = ' '.join(visible_text)
    
    if response.status_code == 200:
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Parse and populate new data
        data = response.json()
        with open('jump_data.json', 'w') as f:
            f.write(str(visible_text))  
        
        print('Dataset updated successfully.')
        
        updatejsonstructure()
    
    else:
        print('Failed to update dataset.')

def updatejsonstructure():
    print('Updating json structure\n')
    with open('jump_data.json', 'r') as file:
        data = json.load(file)
        
        for item_key, item_value in data.items():
            # Add 'likes' and 'dislikes' fields with default values of 0
            item_value['likes'] = "0"
            item_value['dislikes'] = "0"
            
        with open('jump_data.json', 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == '__main__':
    with app.app_context():
        if len(sys.argv) > 1 and sys.argv[1] == 'updatedataset':
            # Update the dataset
            update_dataset()

        if 'updatejsonstructure' in sys.argv:
            updatejsonstructure()

        if 'repopulate' in sys.argv:
            # Repopulate the database
            db.drop_all()
            db.create_all()
            with open('jump_data.json') as file:
                data = json.load(file)
                for item_key, item_value in data.items():
                    links_str = ','.join(item_value['links']) if item_value['links'] else None
                    level = Level(
                        name=item_value['name'],
                        location=item_value['location'],
                        diff=item_value['diff'],
                        tier=item_value['tier'],
                        server=item_value['server'],
                        links=links_str,
                        founder=item_value.get('founder'),
                        line=item_value.get('line'),
                        prover=item_value.get('prover'),
                        likes=item_value.get('likes'),
                        dislikes=item_value.get('dislikes')
                    )
                    db.session.add(level)
                db.session.commit()
            print("Database repopulated.")
        
        else:
            db.create_all()
    app.run()
