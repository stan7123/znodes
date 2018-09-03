import logging
import json
from flask import Flask, jsonify, abort
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config.update({
    'REDIS_URL': "unix://abrakadabra@/var/run/redis/redis-server.sock?db=0"
})
redis_store = FlaskRedis(app)


@app.route('/api/nodes/<string:ip>/<int:port>', methods=['GET'])
def get_node_info(ip, port):
    logging.warning('ip: {}, port: {}'.format(ip, port))
    map_key = "node-map:{}-{}".format(ip, port)
    node_data_serialized = redis_store.get(map_key)
    logging.warning('node_map_ser: {}'.format(node_data_serialized))
    if node_data_serialized is None:
        abort(404)
    node_data = json.loads(node_data_serialized)
    # logging.info('node_map: {}'.format(node_data))
    return jsonify({'node': '{}:{}'.format(ip, port), 'peers': node_data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
