import random
import time

alpha_list = ["C", "D", "E", "F", "G", "A", "B"]


while True:
    time_start = time.time()
    for _ in range(10):
        idx = random.randint(0, 6)
        answer_alpha = random.randint(0, 1)
        if answer_alpha:
            question = idx + 1
            correct_answer = alpha_list[idx]
        else:
            question = alpha_list[idx]
            correct_answer = str(idx + 1)
        while True:
            answer = input("%s ?\n" % question)
            if answer.lower() == correct_answer.lower():
                print("Right!")
                break
            print("Wrong!")
    time_end = time.time()
    print("total time: %.2f, good job!\n" % (time_end - time_start))
