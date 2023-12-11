
with open("input.txt") as f:
    data = [item.strip("\n") for item in f.readlines()]

print("------- part 1 -------")
# part 1 
total_score = 0
for card in data:
    card_number, card_data = card.split(":")

    winning, my_numbers = card_data.split("|")
    winning_list = [number for number in winning.split(" ") if number]
    my_numbers_list =  [number for number in my_numbers.split(" ") if number]
    
    winning_count = len(set(winning_list) & set(my_numbers_list))

    card_score = 2**(winning_count-1) if winning_count>0 else 0
    total_score += card_score

print(total_score)

print("------- part 2 -------")
# part 2 
total_cards = 0
instances_tracker = [[f"Card : {i+1}", 1] for i in range(len(data))]

for index, card in enumerate(data):
    card_number, card_data = card.split(":")

    #print(card_number, instances_tracker[index])

    winning, my_numbers = card_data.split("|")
    winning_list = [number for number in winning.split(" ") if number]
    my_numbers_list =  [number for number in my_numbers.split(" ") if number]
    
    winning_count = len(set(winning_list) & set(my_numbers_list))

    if winning_count != 0:
        for i in range(index+2, index+2+winning_count):
            instances_tracker[i-1][1]+=1*instances_tracker[index][1]

    total_cards += instances_tracker[index][1]*winning_count

total_instances = sum([card[1] for card in instances_tracker])
print(total_instances)