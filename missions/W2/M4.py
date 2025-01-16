from multiprocessing import Queue, Process, Event
import time
from queue import Empty, Full


def produce_task(in_queue: Queue, count: int):
    for i in range(count):
        # try-except
        in_queue.put(f"Task no {i}")
        print(f"Task no {i}")


def consume_task(in_queue: Queue, out_queue: Queue, idx: int, stop_event):
    # 생각해보기...

    while True:
        # while not in_queue.empty() or not stop_event.is_set():
        try:
            task = in_queue.get_nowait()
            time.sleep(0.5)
            # out_queue.put(f"{task} is done by Process-{idx}")

            # 여기서 문제가 생기면 알수가 없다.
            # out_queue 크기를 제한하는 정책을 적용할수있다. -> 넘치면 앞에거 버리기.
            while True:
                try:
                    out_queue.put_nowait(f"{task} is done by Process-{idx}")
                    break
                except Full:
                    out_queue.get_nowait()
                    continue

        except Empty:
            if stop_event.is_set():
                break


def main():
    tasks_to_accomplish = Queue()
    tasks_that_are_done = Queue()
    stop_event = Event()

    producer = [
        Process(target=produce_task, args=(tasks_to_accomplish, 100)) for i in range(2)
    ]
    [p.start() for p in producer]

    consumers = [
        Process(
            target=consume_task,
            args=(tasks_to_accomplish, tasks_that_are_done, i, stop_event),
        )
        for i in range(4)
    ]
    [p.start() for p in consumers]

    [p.join() for p in producer]
    # end signal
    stop_event.set()

    # [p.join() for p in consumers]
    for p in consumers:
        p.join()

    # while true, try-except로 고치기.
    while not tasks_that_are_done.empty():
        try:
            print(tasks_that_are_done.get_nowait())
        except:
            break


if __name__ == "__main__":
    main()
