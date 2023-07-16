from flask import Flask, jsonify, request
import csv
import io

app = Flask(__name__)

# New route to handle GET request for fetching all bank branches data
@app.route('/bank_branches', methods=['GET'])
def get_all_bank_branches():
    data = read_csv_data()
    return jsonify(data)

# New route to handle GET request for fetching a specific branch details by IFSC code
@app.route('/bank_branches/<string:ifsc_code>', methods=['GET'])
def get_branch_details(ifsc_code):
    data = read_csv_data()
    branch_details = [branch for branch in data if branch['ifsc'] == ifsc_code]
    if branch_details:
        return jsonify(branch_details[0])
    else:
        return jsonify({'message': 'Branch not found'}), 404

# New route to handle GET request for fetching branch details by branch name
@app.route('/bank_branches/branch/<string:branch_name>', methods=['GET'])
def get_branch_by_name(branch_name):
    data = read_csv_data()
    branches_by_name = [branch for branch in data if branch['branch'].lower() == branch_name.lower()]
    return jsonify(branches_by_name)

# New route to handle GET request for fetching branch details by city
@app.route('/bank_branches/city/<string:city>', methods=['GET'])
def get_branch_by_city(city):
    data = read_csv_data()
    branches_by_city = [branch for branch in data if branch['city'].lower() == city.lower()]
    return jsonify(branches_by_city)

# New route to handle GET request for fetching branch details by district
@app.route('/bank_branches/district/<string:district>', methods=['GET'])
def get_branch_by_district(district):
    data = read_csv_data()
    branches_by_district = [branch for branch in data if branch['district'].lower() == district.lower()]
    return jsonify(branches_by_district)

# New route to handle GET request for fetching branch details by state
@app.route('/bank_branches/state/<string:state>', methods=['GET'])
def get_branch_by_state(state):
    data = read_csv_data()
    branches_by_state = [branch for branch in data if branch['state'].lower() == state.lower()]
    return jsonify(branches_by_state)

def read_csv_data():
    data = []
    with open('bank_branches.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            data.append({
                'ifsc': row[0],
                'bank_id': row[1],
                'branch': row[2],
                'address': row[3],
                'city': row[4],
                'district': row[5],
                'state': row[6],
                'bank_name': row[7]
            })
    return data

if __name__ == '__main__':
    app.run(debug=True)
