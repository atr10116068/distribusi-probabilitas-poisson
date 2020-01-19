import savefile,loadfile,color

data = loadfile.load()
menu=data['choice']
urutan=[]
backuprate="0.0"

def hP(p,n):
    tot = str(int(p)/n)[0:4]
    return tot

def hU(n,p):
    tot = str(float(n)*float(p))[0:4]
    return tot

def faktorial(n):
    tot=n
    for c in range(1,n):
        tot=tot*c
    return tot

def predik(x,u):
    e=2.7182
    tot = str(u**x)+"x"+format(float(e**-u), 'f')+"/"+str(faktorial(x))
    tott = str((float(u**x)*float(e**-u))/faktorial(x))[0:4]
    return tott


lanjut='ya'
while lanjut == 'ya':
    jawab={
    1:'wortel',
    2:'jagung',
    3:'kubis',
    4:'tomat',
    5:'sandwitch',
    6:'sate',
    7:'ayam',
    8:'sapi'}

    disp = "\t\t\t| "

    nourutan=len(urutan)
    for x in range(len(urutan)):
        disp += " %s "%urutan[nourutan-1]
        nourutan-=1
    disp += "|"
    print(disp)

    print('===========|')
    no=1

    for o in menu:
        nama = str(no)+". "+o
        pointawal = str(menu[o]['pawal'])
        point = str(menu[o]['p'])
        n = data['n']
        P = hP(pointawal,151)

        #prediksi dari 1/4 putaran sebelumnya
        U = hU(n,P)[0:3]
        pr = predik(2,float(U))

        if o == 'sate' or o == 'ayam' or o == 'sapi':
            display=(nama+"\t\t["+point+"]")
        else:
            display=(nama+"\t["+point+"]")
        display+=("\ttotal rate %s"%P+" %")
        display+=("\trate "+str(round(n*0.1))+" setelahnya %s"%U+" %")
        display+=("\t\tperkiraan "+str(color.green(pr+" %"))+" saat "+str(round(n*0.1))[0:3]+" putaran lagi ")
        try:
            if float(backuprate)>float(pr):
                display += "\t"+color.red(str(float(backuprate)-float(pr))[0:5]+" %")
                backuprate = str(float(backuprate)-float(pr))[0:5]
            else:
                display += "\t"+color.green(str(float(pr)-float(backuprate))[0:5]+" %")
                backuprate = str(float(pr)-float(backuprate))[0:5]
        except Exception as e:
            display+="\tCrash : "+str(e)
        no+=1
        print(display)
    print('===========|\n')

    tambah=input('tambah : ')

    try:
        if int(tambah) >= 1 and int(tambah) <= 8:
            print("\t\t\t[ Developer : TopixSayaBundar ]")
            id=jawab[int(tambah)]
            menu[id]['p'] += 1
            print("\t\t\t-> "+color.green(id+" +1"))
            data['n'] += 1
            if len(urutan) < 8:
                urutan.append(id)
            else:
                urutan.pop(0)
                urutan.append(id)
    except Exception:
        print(color.green('akan di save'))
        savefile.save(data)
        lanjut = 'tidak'