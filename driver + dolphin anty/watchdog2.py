import multiprocessing
import time

# bar
def bar():
    print('Start')
    for i in range(6):
        print ("Tick")
        time.sleep(1)
    print('Stop')

if __name__ == '__main__':
    itr=input('Введите количество циклов=')
    i=0
    while i<int(itr):
        # Start bar as a process
        p = multiprocessing.Process(target=bar)
        p.start()

        # Подождите 10 секунд или пока процесс не завершится
        p.join(10)

        # Если поток все еще активен
        if p.is_alive():
            print ("running... let's kill it...")

            # Завершить - может не работать, если процесс завис навсегда
            p.terminate()
            # ИЛИ Убить - сработает точно, однако нет шансов, что процесс завершится красиво
            # p.kill()

            p.join()
        i+=1