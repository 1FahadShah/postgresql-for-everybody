from flask import Flask, jsonify, abort
import psycopg2
import psycopg2.extras

# --- Database Connection Details ---
DB_HOST = 'localhost'
DB_NAME = 'people'
DB_USER = 'fahad'
DB_PASS = 'secret'

# Create the Flask application
app = Flask(__name__)

# Define the API endpoint (URL route)
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = None
    try:
        # Connect to the database
        conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
        # Use DictCursor to get dictionary-like rows
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            # Query for the specific user
            cur.execute("SELECT profile FROM users_json WHERE id = %s;", (user_id,))
            user_data = cur.fetchone()

        if user_data is None:
            # If user not found, return a 404 error
            abort(404, description=f'User with ID {user_id} not found.')

        # The 'profile' column is already JSONB, so user_data['profile'] is a dict
        # jsonify will convert the Python dict to a JSON response
        return jsonify(user_data['profile'])

    except psycopg2.Error as e:
        # Handle potential database errors
        abort(500, description=f'Database error: {e}')

    finally:
        if conn is not None:
            conn.close()

# This allows us to run the app directly from the script
if __name__ == '__main__':
    app.run(debug=True)
