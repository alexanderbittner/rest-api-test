from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

def get_file_content(filename):
    with open(filename, 'r') as file:
        return file.read()
    return 'file issue'

def set_file_content(filename, content):
    with open(filename, 'w') as file:
        file.write(str(content))
        return 'success'
    return 'file issue'


class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}

class FileTest(Resource):
    def get(self):
        return {'content':get_file_content('file.txt')}

class FileWrite(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('content', required=True)

        content = parser.parse_args()
        set_file_content('file.txt', content)

        return {'message':'content changed'}


api.add_resource(HelloWorld, '/')
api.add_resource(FileTest, '/file')
api.add_resource(FileWrite, '/write')

if __name__ == '__main__':
    app.run(debug=True)




