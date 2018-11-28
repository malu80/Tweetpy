from TwitterAPI import TwitterAPI
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS , cross_origin

app = Flask(__name__)
CORS(app)
api = Api(app)

class Twitter(Resource):
    def post(self,key,mesg):

        CONSUMER_KEY = 'dJDsnFRT2YLXQuVc7aNG6I02J'
        CONSUMER_SECRET = 'tOXx58OC6Oa1ysaNmorv2vuOKWJvDZkXLFnK67UeV2LUtFHTO2'
        ACCESS_TOKEN_KEY = '1067756218997829633-oVsy85mJONOV6ih7RLp7N662VzkAC1'
        ACCESS_TOKEN_SECRET = 'UwPEVJEkevvwEBaxFZoQ1nVIw5XgXcVLRSXN8kFTKFufO'

        api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
        file = open('test.png', 'rb')
        data = file.read()
        location='#tomtom'+key+'\n'+mesg
        r = api.request('statuses/update_with_media', {'status':location}, {'media[]':data})
        print(r.status_code)

        return {'Tweet posted':r.status_code}

api.add_resource(Twitter, '/twitter/<string:key>/<string:mesg>')

if __name__ == '__main__':
    app.run(host='10.26.34.97', port=8001)