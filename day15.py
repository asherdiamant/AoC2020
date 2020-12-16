from tqdm import tqdm

starting_numbers = [16,12,1,0,15,7,11]
history = {}

for turn, num in enumerate(starting_numbers):
    history[num] = [turn+1, 0]

previous_num = starting_numbers[-1]

for turn in tqdm(range(len(starting_numbers) + 1, 30000000+1)):
    if history[previous_num][1] == 0:
        curr_num = 0
    else:
        curr_num = history[previous_num][0] - history[previous_num][1]
    if curr_num in history.keys():
        last_time = history[curr_num][0]
    else:
        last_time = 0
    history[curr_num] = [turn, last_time]
    previous_num = curr_num
    turn += 1
print("Say:", curr_num)