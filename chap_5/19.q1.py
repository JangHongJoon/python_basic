def the_pouring(capacities, bottles, from_id, to_id) :
    for a in range(len(from_id)):


        i = from_id[a]
        j = to_id[a]

        print(bottles[i], bottles[j])
        print (i,j)
        if bottles[i] + bottles[j] > capacities[j]:
            bottles[i] -= capacities[j] - bottles[j]
            bottles[j] = capacities[j]
        else :
            bottles[i] = 0
            bottles[j] += bottles[i]
    return bottles



c=list(map(int, input().split(" ")))
b=list(map(int, input().split(" ")))
f=list(map(int, input().split(" ")))
t=list(map(int, input().split(" ")))

print(the_pouring(c, b, f, t))

