with open("3/in.txt") as f:
    banks = f.readlines()
ans = 0
for bank in banks:
    bank = bank.strip()
    b1 = 0
    b2 = 0
    for i, battery in enumerate(bank):
        battery = int(battery)
        if battery > b1 and i < len(bank) - 1:
            b1 = battery
            b2 = 0
        elif battery > b2:
            b2 = battery

    v = int(str(b1) + str(b2))
    ans += v

print(ans)
