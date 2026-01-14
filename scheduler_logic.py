import turtle as t
from operator import itemgetter

ArrayAns = []

def draw_template():
    try:
        t.reset()
        screen = t.Screen()
        screen.setup(500,500)
        t.title("Process Scheduling Simulator")
        t.speed(0)
        t.hideturtle()
        t.bgcolor("Light grey")
        t.pu()
        t.goto(-200,20)
        t.pd()
        t.goto(200,20)
        t.goto(200,-20)
        t.goto(-200,-20)
        t.goto(-200,20)
        t.pu()
        t.goto(-200,-45)
        t.write("0",False,"center",("Arial",8,"normal"))
        t.goto(200,-45)
        t.write("100",False,"center",("Arial",8,"normal"))
        t.goto(100,200)
        t.color("red")
        t.write("Process 1: Red",False,"left",("Arial",8,"normal"))
        t.goto(100,180)
        t.color("green")
        t.write("Process 2: Green",False,"left",("Arial",8,"normal"))
        t.goto(100,160)
        t.color("blue")
        t.write("Process 3: Blue",False,"left",("Arial",8,"normal"))
        t.goto(100,140)
        t.color("Yellow")
        t.write("Process 4: Yellow",False,"left",("Arial",8,"normal"))
        t.goto(100,120)
        t.color("Purple")
        t.write("Process 5: Purple",False,"left",("Arial",8,"normal"))
    except:
        pass

def Special(list):
    global ArrayAns
    list.append(0)
  
    count2 = 0
    for i in range(0,len(list)):  
        if(i+1==len(list)):pass   
        elif(i != len(list)):
            if(list[i] != list[i+1] ): count2 += 1
            
    ArrayAns=[]

    
    for i in range(0,count2):
        ArrayAns+=[0]
    for i in range(0,count2):

        ArrayAns[i] = [0]*3
    for i in range(0,count2):   
        ArrayAns[i][0] = i

 
    start = 0
    i=0
    count = 0
 
    
    for i in range(0,len(list)):
        current = i

        if list[current] != list[start]:

          
            
            ArrayAns[count][0] = list[i-1] #indicate number of process
            ArrayAns[count][1] = start #Set the starting time of that process
            ArrayAns[count][2] = current #The stop time of that process
            
            count+=1
            start = current

    #print(ArrayAns)
    
    return ArrayAns # ArrayAns[ #number process, starting time, stop time]

def Respond(list):

    Res  = []

    AvgR = 0

    check=[]
    
    num =len(list)

    for i in range(0,num):
        if(list[i][0] in check):pass

        else:
            check.append(list[i][0])
            Res.append((list[i][0],list[i][1]))


    for i in range(0,len(Res)):

        AvgR += float(Res[i][1])

    #print(AvgR)
    #print(float(len(Res)))

    AvgR = AvgR/float(len(Res))

    #print(AvgR)

    return AvgR

def Waiting(list,list2):

    #list   = list ที่่ return จาก Special
    #list2  = list input เริ่มต้น (ที่เป็น process,burst,arrival) / (สร้าง duplicate มาใส่เพราะว่า algorithm ผมมัน pop ออก list ไปแล้ว)
    check = []
    check2 = []
    Wait = []
    AvgW = 0

    for i in range(len(list)-1,-1,-1):

        if(list[i][0] not in check2):
            check.append(list[i])
            check2.append(list[i][0])

            
          
    check.sort(key=lambda x: x[0])
    
    for i in range(len(check)):

        Wait.append(int(check[i][2])-int(list2[i][2])-int(list2[i][1]))

    for i in range(0,len(Wait)):

        AvgW += int(Wait[i])

    AvgW = AvgW/float(len(Wait))

    return AvgW

def Turn(list,list2):

    #list   = list ที่่ return จาก Special
    #list2  = list input เริ่มต้น (ที่เป็น process,burst,arrival) / (สร้าง duplicate มาใส่เพราะว่า algorithm ผมมัน pop ออก list ไปแล้ว)

    print(list)
    
    TotalFinish = 0
    TotalArrival = 0

    check=[]
    check2=[]
    
    for i in range(0,len(list2)):

        TotalArrival += list2[i][1]

    
        check = []
    
    for i in range(len(list)-1,-1,-1):

        if(list[i][0] not in check2):
            check.append(list[i])
            check2.append(list[i][0])

            
          
    check.sort(key=lambda x: x[0])



    for i in range(0,len(check)):

        TotalFinish += check[i][2]


    TotalTurn = (TotalFinish - TotalArrival)/float(len(check))


    #print(TotalTurn)

    return TotalTurn

def SJF_NON2( list ):

    timepast = 0
    r=0
    lista = []
    listb = []

    seq=[]
    
    while(len(list) != 0):

        #print('')
        list.sort(key=lambda x: x[1])

 
    
        for i in range(0,len(list)):

            if(int(list[0][1]) <= timepast):lista.append(list.pop(0))
            elif(int(list[0][1]) > timepast):listb.append(list.pop(0))

        for i in range(0,len(listb)):list.append(listb.pop(0))


        if(len(lista) != 0):

            lista.sort(key=lambda x: x[2])

            

            while(int(lista[0][2]) != 0):
    

                #print('Time : '+str(timepast)+' -> ',end='')
                #print(lista[0][0])
                seq.append(int(lista[0][0]))
                lista[0][2] = int(lista[0][2])-1
                timepast+=1
                


            lista.pop(0)
            
            while(len(lista) != 0):
                list.append(lista.pop(0))


            
                

        elif(len(lista) == 0):
            #print('Time : '+str(timepast)+' -> ',end='')
            #print('-')
            timepast+=1
            seq.append(0)
    Special(seq)
            
def RR( list, quantum ):

    ts = quantum

    seq = []
    timepast = 0
    queue = []
    queue2 = []
    r = 0
    tq = list
    tq.sort(key=lambda x: x[1])
    st = int(tq[0][1])
    
    
    while(len(list) != 0):
        

      
        
        for i in range(0,len(list)):
            
                if(int(list[0][1]) <= timepast ):
                    queue.append(list.pop(0))

                elif(int(list[0][1]) > timepast):
                    queue2.append(list.pop(0))


        for i in range(0,len(queue2)):
            list.append(queue2.pop(0))
            
        

        if(len(queue) == 0):
            #print('Time : '+str(timepast)+' -> ',end='')
            #print(' - ')
            timepast += 1
            seq.append(0)

        
        while(len(queue) != 0 ):
            for i in range(0,ts):
                

                if(len(queue) == 0):
                    #print('Time : '+str(timepast)+' -> ',end='')
                    #print(' - ')
                    timepast+=1
                    seq.append(0)
                elif(int(queue[0][2]) != 0):
                    #print('Time : '+str(timepast)+' -> ',end='')
                    #print(queue[0][0])
                    seq.append(int(queue[0][0]))
                    queue[0][2] = str(int(queue[0][2])-1)
                    if(int(queue[0][2]) == 0):
                        #print('')
                        #print(str(queue[0][0])+'Finished')
                        #print('')
                        queue.pop(0)
                    timepast+=1
                   
                
                    
            if(len(queue) != 0 ):list.append(queue.pop(0))



    #print('end')
            
    Special(seq)

def SJF( list ):


        lista = []
        listb = []
        timepast = 0
        r=0
        tl = list
        tl.sort(key=lambda x: x[1])
        st = int(tl[0][1])
        seq = []
        
        
        while(len(list) != 0):
            
      
                 
             for i in range(0,len(list)):
                 if(int(list[0][1]) <= timepast): lista.append(list.pop(0))
                 elif(int(list[0][1]) > timepast):listb.append(list.pop(0))

             for i in range(0,len(listb)):list.append(listb.pop(0))

      
   
             lista.sort(key=lambda x: x[2])



            # print('Time : '+str(timepast)+' -> ',end='')
             if(len(lista) != 0):
                 if(int(lista[0][2]) != 0):
                    #print('Time : '+str(timepast)+' -> ',end='')
                    #print(lista[0][0])
                    seq.append(int(lista[0][0]))
                    
                 elif(int(lista[0][2]) == 0 ):
                     if(len(lista) != 1):
                         #print('Time : '+str(timepast)+' -> ',end='')
                         seq.append(int(lista[1][0]))
                        # print(lista[1][0])
                         
                    
                     elif(len(lista) == 1):
                         #print('-')
                         seq.append(0)
                    
            
                 if(int(lista[0][2])==1):
                    #print(lista[0][0]+' Finished')
                    pass
                 if(int(lista[0][2])==0):lista.pop(0)
                     
                    
                 
                 if(len(lista) != 0):
                     if(int(lista[0][2]) > 0):
                         lista[0][2] = int(lista[0][2])-1
                         list.append(lista.pop(0))
                         

                 


                 for i in range(0,len(lista)):list.append(lista.pop(0))

             elif(len(lista) == 0):
               # print('Time : '+str(timepast)+' -> ',end='')
                #print(' - ')
                seq.append(0)
             timepast += 1


  
        Special(seq)

def draw_gantt_chart(array_ans, n):
    """Draw the Gantt chart visualization"""
    for i in range(len(array_ans)):
        s = array_ans[i][1]
        f = array_ans[i][2]
        if(array_ans[i][0] == 1):
            t.color("Red")
        elif(array_ans[i][0]== 2):
            t.color("Green")
        elif(array_ans[i][0]==3):
            t.color("Blue")
        elif(array_ans[i][0]==4):
            t.color("Yellow")
        elif(array_ans[i][0]==5):
            t.color("Purple")
        t.begin_fill()
        t.goto(4*s-200,-20)
        t.goto(4*f-200,-20)
        t.goto(4*f-200,20)
        t.goto(4*s-200,20)
        t.goto(4*s-200,-20)
        t.end_fill()
        t.color("black")
        t.goto(s*4-200,-45)
        t.write("%d"%s,False,"center",("Arial",8,"normal"))
        t.goto(f*4-200,-45)
        t.write("%d"%f,False,"center",("Arial",8,"normal"))

def display_metrics(wt, tat, rt):
    """Display the scheduling metrics"""
    t.goto(0,-175)
    t.write("Average Waiting Time : %.2f"%wt,False,"center",("Arial",14,"normal"))
    t.goto(0,-200)
    t.write("Average Turnaround Time : %.2f"%tat,False,"center",("Arial",14,"normal"))
    t.goto(0,-225)
    t.write("Average Respond Time : %.2f"%rt,False,"center",("Arial",14,"normal"))

def animate_FCFS(proc_list, temp2, n):
    global ArrayAns
    
    proc_list.sort(key=itemgetter(1))
    s1 = proc_list[0][1]
    f1 = s1 + proc_list[0][2]
    if(proc_list[1][1]<f1):
        s2 = f1
    else:
        s2 = proc_list[1][1]
    f2 = s2 + proc_list[1][2]
    if(proc_list[2][1]<f2):
        s3 = f2    
    else:
        s3 = proc_list[2][1]
    f3 = s3 + proc_list[2][2]
    if(n>=4):
        if(proc_list[3][1]<f3):
            s4 = f3
        else:
            s4 = proc_list[3][1]
        f4 = s4 + proc_list[3][2]
        if(n==5):
            if(proc_list[4][1]<f4):
                s5 = f4
            else:
                s5 = proc_list[4][1]
            f5 = s5 + proc_list[4][2]
    draw_template()
    if(proc_list[0][0] == 1):
         t.color("Red")
    elif(proc_list[0][0]== 2):
        t.color("Green")
    elif(proc_list[0][0]==3):
        t.color("Blue")
    elif(proc_list[0][0]==4):
        t.color("Yellow")
    elif(proc_list[0][0]==5):
        t.color("Purple")
    t.begin_fill()
    t.goto(4*s1-200,-20)
    t.goto(4*f1-200,-20)
    t.goto(4*f1-200,20)
    t.goto(4*s1-200,20)
    t.goto(4*s1-200,-20)
    t.end_fill()
    if(proc_list[1][0] == 1):
         t.color("Red")
    elif(proc_list[1][0]== 2):
        t.color("Green")
    elif(proc_list[1][0]==3):
        t.color("Blue")
    elif(proc_list[1][0]==4):
        t.color("Yellow")
    elif(proc_list[1][0]==5):
        t.color("Purple")
    t.begin_fill()
    t.goto(4*s2-200,-20)
    t.goto(4*f2-200,-20)
    t.goto(4*f2-200,20)
    t.goto(4*s2-200,20)
    t.goto(4*s2-200,-20)
    t.end_fill()
    if(proc_list[2][0] == 1):
         t.color("Red")
    elif(proc_list[2][0]== 2):
        t.color("Green")
    elif(proc_list[2][0]==3):
        t.color("Blue")
    elif(proc_list[2][0]==4):
        t.color("Yellow")
    elif(proc_list[2][0]==5):
        t.color("Purple")
    t.begin_fill()
    t.goto(4*s3-200,-20)
    t.goto(4*f3-200,-20)
    t.goto(4*f3-200,20)
    t.goto(4*s3-200,20)
    t.goto(4*s3-200,-20)
    t.end_fill()
    if(n>=4):
        if(proc_list[3][0] == 1):
            t.color("Red")
        elif(proc_list[3][0]== 2):
            t.color("Green")
        elif(proc_list[3][0]==3):
            t.color("Blue")
        elif(proc_list[3][0]==4):
            t.color("Yellow")
        elif(proc_list[3][0]==5):
            t.color("Purple")
        t.begin_fill()
        t.goto(4*s4-200,-20)
        t.goto(4*f4-200,-20)
        t.goto(4*f4-200,20)
        t.goto(4*s4-200,20)
        t.goto(4*s4-200,-20)
        t.end_fill()
        if(n==5):
            if(proc_list[4][0] == 1):
                t.color("Red")
            elif(proc_list[4][0]== 2):
                t.color("Green")
            elif(proc_list[4][0]==3):
                t.color("Blue")
            elif(proc_list[4][0]==4):
                t.color("Yellow")
            elif(proc_list[4][0]==5):
                t.color("Purple")
            t.begin_fill()
            t.goto(4*s5-200,-20)
            t.goto(4*f5-200,-20)
            t.goto(4*f5-200,20)
            t.goto(4*s5-200,20)
            t.goto(4*s5-200,-20)
            t.end_fill()
    t.color("black")
    t.goto(s1*4-200,-45)
    t.write("%d"%s1,False,"center",("Arial",8,"normal"))
    t.goto(f1*4-200,-45)
    t.write("%d"%f1,False,"center",("Arial",8,"normal"))
    t.goto(s2*4-200,-45)
    t.write("%d"%s2,False,"center",("Arial",8,"normal"))
    t.goto(f2*4-200,-45)
    t.write("%d"%f2,False,"center",("Arial",8,"normal"))
    t.goto(s3*4-200,-45)
    t.write("%d"%s3,False,"center",("Arial",8,"normal"))
    t.goto(f3*4-200,-45)
    t.write("%d"%f3,False,"center",("Arial",8,"normal"))
    if(n>=4):
        t.goto(s4*4-200,-45)
        t.write("%d"%s4,False,"center",("Arial",8,"normal"))
        t.goto(f4*4-200,-45)
        t.write("%d"%f4,False,"center",("Arial",8,"normal"))
        if(n==5):
            t.goto(s5*4-200,-45)
            t.write("%d"%s5,False,"center",("Arial",8,"normal"))
            t.goto(f5*4-200,-45)
            t.write("%d"%f5,False,"center",("Arial",8,"normal"))
    if(n == 3):
        ArrayAns = [[proc_list[0][0],s1,f1],[proc_list[1][0],s2,f2],[proc_list[2][0],s3,f3]]
        temp = [[proc_list[0][0],s1,f1],[proc_list[1][0],s2,f2],[proc_list[2][0],s3,f3]]
    if(n >= 4):
        ArrayAns = [[proc_list[0][0],s1,f1],[proc_list[1][0],s2,f2],[proc_list[2][0],s3,f3],[proc_list[3][0],s4,f4]]
        temp = [[proc_list[0][0],s1,f1],[proc_list[1][0],s2,f2],[proc_list[2][0],s3,f3],[proc_list[3][0],s4,f4]]
        if(n == 5):
            ArrayAns = [[proc_list[0][0],s1,f1],[proc_list[1][0],s2,f2],[proc_list[2][0],s3,f3],[proc_list[3][0],s4,f4],[proc_list[4][0],s5,f5]]
            temp = [[proc_list[0][0],s1,f1],[proc_list[1][0],s2,f2],[proc_list[2][0],s3,f3],[proc_list[3][0],s4,f4],[proc_list[4][0],s5,f5]]
    rt = Respond(ArrayAns)
    wt = Waiting(ArrayAns,proc_list)
    tat = Turn(temp,temp2)
    display_metrics(wt, tat, rt)
    t.goto(-150,200)
    t.write("FCFS scheduling",False,"center",("Arial",14,"bold","underline"))

def animate_SJFN(proc_list, temp, tempt, n):
    global ArrayAns
    
    draw_template()
    SJF_NON2(proc_list)
    for i in ArrayAns:
        if(i[0]==0):
            ArrayAns.remove(i)
    temp2 = ArrayAns
    temp2t = ArrayAns
    
    draw_gantt_chart(ArrayAns, n)
    
    rt = Respond(ArrayAns)
    wt = Waiting(temp2,temp)
    tat = Turn(temp2t,tempt)
    display_metrics(wt, tat, rt)
    t.goto(-100,200)
    t.write("SJF (Non-preemptive)",False,"center",("Arial",14,"bold","underline"))
    t.goto(-100,180)
    t.write("Scheduling",False,"center",("Arial",14,"bold","underline"))

def animate_SJF(proc_list, temp, tempt, n):
    global ArrayAns
    
    draw_template()
    SJF(proc_list)
    for i in ArrayAns:
        if(i[0]==0):
            ArrayAns.remove(i)
    temp2 = ArrayAns
    temp2t = ArrayAns
    
    draw_gantt_chart(ArrayAns, n)
    
    rt = Respond(ArrayAns)
    wt = Waiting(temp2,temp)
    tat = Turn(temp2t,tempt)
    display_metrics(wt, tat, rt)
    t.goto(-100,200)
    t.write("SJF (Preemptive)",False,"center",("Arial",14,"bold","underline"))
    t.goto(-100,180)
    t.write("Scheduling",False,"center",("Arial",14,"bold","underline"))

def animate_RR(proc_list, temp, tempt, n, quantum):
    global ArrayAns
    
    RR(proc_list, quantum)
    for i in ArrayAns:
        if(i[0]==0):
            ArrayAns.remove(i)
    temp2 = ArrayAns
    temp2t = ArrayAns
    draw_template()
    
    draw_gantt_chart(ArrayAns, n)
    
    rt = Respond(ArrayAns)
    print(temp)
    print(temp2)
    wt = Waiting(temp2,temp)
    tat = Turn(temp2t,tempt)
    display_metrics(wt, tat, rt)
    t.goto(-100,200)
    t.write("Round Robin Scheduling",False,"center",("Arial",14,"bold","underline"))
