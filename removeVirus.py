def removeVirus(files):
    file = files[10:].split(",")
    l = len(file)
    i=0
    while i < l:
        if ("virus" in file[i] or "malware" in file[i]):
            if ('antivirus' not in file[i] and 'notvirus' not in file[i]):
                file.pop(i)
                l -= 1
                continue
        i+=1

    #printing
    print("PC Files:",end=" ")
    if (len(file)==0):
        print("Empty")
    for i in range(len(file)):
        print(file[i],end="")
        if(i!=len(file)-1):
            print(",",end="")
    print()
            

removeVirus("PC Files: notvirus.exe, funnycat.gif")
removeVirus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")
removeVirus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")
removeVirus("PC Files: fsocietyvirus.exe, somemalware.gif")