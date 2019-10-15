import time
import pandas as pd


def get_input(prompt, count):
    start_time = time.time()
    uinput = input('\n' + prompt + '\n')
    if uinput == prompt:
        end_time = time.time()
        count += 1
        trial_time = end_time - start_time
        print("\nSubmission accepted, time was {} sec, new count = {}".format(trial_time, count))
    else:
        print("\nSubmission rejected, expected '{}' but received '{}'".format(prompt, uinput))
        trial_time, count = get_input(prompt, count)
    return trial_time, count


def main():
    print("Welcome to the speed tester app")
    desired_count = int(input("Enter the number of trials to take: "))
    print(
        "The timer stops as soon as the prompt is shown.  Only entries that exactly match the prompt will be counted.")
    count = 0
    times = []
    prompt = "The quick brown fox jumps over the lazy dog"
    while count < desired_count:
        trial_time, count = get_input(prompt, count)
        times.append(trial_time)
    print("Trials complete.  Here are your times: ")
    print(times)
    csv_name = 'time_trials_{}.csv'.format(str(time.time())[-5:])
    df = pd.DataFrame({'Times': times})
    df.to_csv(csv_name)
    print("Times for each trial saved in: " + csv_name)


if __name__ == '__main__':
    main()


