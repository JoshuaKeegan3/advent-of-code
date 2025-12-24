with open("3/in.txt") as f:
    banks = f.readlines()
ans = 0
for bank in banks:
    bank = bank.strip()
    l = [0 for i in range(12)]
    for b, battery in enumerate(bank):  # every battery in the input
        battery = int(battery)
        for i, bi in enumerate(l):  # every in the battery in the output
            if battery > bi and len(bank) - b > 11 - i:
                l[i] = battery

                for j, bj in enumerate(l):
                    if j <= i:
                        continue
                    l[j] = 0

                break
        print(l)
    v = "".join([str(b) for b in l])
    print(v)
    ans += int(v)

print(ans)  # < 177444444444267
