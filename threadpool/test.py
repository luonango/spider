# Test a demo
from ThreadPool import *


# if __name__ == '__main__':
def test():
    import random
    import time
    import datetime

    def do_work(data):
        time.sleep(random.randint(1, 3))
        res = str(datetime.datetime.now()) + "" + str(data)
        return res

    def print_result(request, result):
        print "---Result from request %s : %r" % (request.requestID, result)

    main = ThreadPool(3)
    for i in range(40):
        req = WorkRequest(do_work, args=[i], kwds={}, callback=print_result)
        main.putRequest(req)
        print "work request #%s added." % req.requestID

    print '-' * 20, main.workersize(), '-' * 20

    counter = 0
    while True:
        try:
            time.sleep(0.5)
            main.poll()
            if (counter == 5):
                print "Add 3 more workers threads"
                main.createWorkers(3)
                print '-' * 20, main.workersize(), '-' * 20
            if (counter == 10):
                print "dismiss 2 workers threads"
                main.dismissWorkers(2)
                print '-' * 20, main.workersize(), '-' * 20
            counter += 1
        except NoResultsPending:
            print "no pending results"
            break

    main.stop()
    print "Stop"
