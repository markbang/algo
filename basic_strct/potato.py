from ArrayQueue import ArrayQueue


def hot_potato(name_list, num):
    sim_queue = ArrayQueue()
    for name in name_list:
        sim_queue.enqueue(name)
    while len(sim_queue) > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.first())
            sim_queue.dequeue()
        sim_queue.dequeue()
    return sim_queue.first()


if __name__ == "__main__":
    name_list = ["Bill", "David", "Susan", "Jane", "Kent", "Bard"]
    num = 6
    win = hot_potato(name_list, num)
    print(win)
