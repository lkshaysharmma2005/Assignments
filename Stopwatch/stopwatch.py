import time

def stopwatch():
    print("Press Enter to start the stopwatch and Ctrl+C to stop it.")
    try:
        input()
        start_time = time.time()
        print("Stopwatch started. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\nElapsed time: {elapsed_time:.2f} seconds")

stopwatch()
