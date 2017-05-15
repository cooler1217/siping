from flup.server.fcgi import WSGIServer
import sys
from core import cooler
from core import cat
from core import main

app = main.app



def main():
    print sys.argv[1] if len(sys.argv) > 1 else 'work'

    WSGIServer(app, bindAddress=(config.get('server', 'host'), 8089)).run()

if __name__ == '__main__':
    # main()
    # print "ddd"
    app.run(host='0.0.0.0',port=9091)