
def demo(x):
    f = x+1
    number = []
    has_ball= [0,0,0,0,0,0,0,0,0,0]
    x_coor = []
    y_coor = []
    frame = [f,f,f,f,f,f,f,f,f,f]
    file_x = "xcoorlist.txt"
    file_y = 'ycoorlist.txt'
    for i in range(10):
        number.append(i+1)

    if f >107 and f <158:
        has_ball[9] = 1
    elif f > 180 and f <271:
        has_ball[3] = 1
    else:
        for i in range(10):
            has_ball[i] = 0

    with open(file_x, 'r') as file:
        line = file.readlines()
        if x <= len(line):
            t = eval(line[x].strip('\n'))
            print(t)
            for j in t:
                txt = str(j)
                x_coor.append(txt)

    with open(file_y, 'r') as file:
        line = file.readlines()
        if x <= len(line):
            t = eval(line[x].strip('\n'))
            print(t)
            for j in t:
                txt = str(j)
                y_coor.append(txt)    
                

    return number,has_ball,x_coor,y_coor,frame

if __name__ == '__main__':
        demo()
        #20 => 21