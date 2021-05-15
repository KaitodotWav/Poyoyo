save_user = False
cache = [line.strip() for line in open("reg_user.txt")]
U_id = []
U_name = []
for i in range(len(cache)):
    filt = str(cache[i])
    filt2 = filt.split(":")
    U_id.append(filt2[1])
    U_name.append(filt2[0])