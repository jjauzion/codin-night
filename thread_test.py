import threading
from pathlib import Path
import random
import queue


def my_function(i, number, directory):
    s = "i is {} ; number is '{}'".format(i, number)
    file = Path(directory) / "{}-i{}.txt".format(number, i)
    with file.open(mode='w', encoding='utf-8') as fp:
        fp.write(s)


def create_thread(l_number, directory):
    thread = []
    cpt = 0
    for i, nb in enumerate(l_number):
        t = threading.Thread(target=my_function, args=(i, nb, directory))
        t.start()
        thread.append(t)
        cpt += 1
    print("nb of thread = {}".format(threading.active_count()))
    for t in thread:
        t.join()
    print(f"Done! cpt = {cpt} ; len thread = {len(thread)}")


def worker_daemon(q, i, directory):
    while True:
        nb = q.get()
        my_function(i, nb, directory)
        q.task_done()


def worker(q, i, directory):
    while True:
        try:
            nb = q.get(block=True, timeout=0.1)
            my_function(i, nb, directory)
            q.task_done()
        except queue.Empty:
            print("exception caught")
            break


def create_queue(l_number, directory, max_thread=10):
    q = queue.Queue()
    for nb in l_number:
        q.put(nb)
    print(f'queue size = {q.qsize()}')
    for i in range(max_thread):
        print(i)
        thread = threading.Thread(target=worker, args=(q, i, directory))
        thread.daemon = False
        thread.start()
    print("workers ready")
    q.join()
    print(f"Done!")


def run():
    directory = Path("../test_dir")
    directory.mkdir(exist_ok=True)
    l_number = random.sample(range(10000), k=10000)
    # create_thread(l_number, directory)
    create_queue(l_number, directory, max_thread=1)


if __name__ == "__main__":
    # cProfile.run('run()', 'restats')
    # p = pstats.Stats('restats')
    # p.strip_dirs().sort_stats(SortKey.TIME).print_stats()
    run()

