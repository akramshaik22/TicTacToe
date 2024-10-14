'''
    Tic Tac Toe Game

    Code by
             Akram Shaik
'''
from tkinter import*
from tkinter import messagebox
tic=Tk()
tic.title('TicTacToe')
tic.geometry('285x260')
count,var,bg_color=0,' ','white'
def click(a):
    global count,var,bg_color
    if b_dict[a]['text']==' ' and count%2==0:
        var,bg_color='X','light green'
    elif b_dict[a]['text']==' ':
        var,bg_color='O','sky blue'
    else:
        messagebox.showerror('INFO', 'Cell Already Filled')
        count-=1
    b_dict[a].config(text=var, bg=bg_color)
    count += 1
    if count>2 and count<10:
            for i in range(0,3):
                if (b_dict[m[i][0]]['text'] == b_dict[m[i][1]]['text'] == b_dict[m[i][2]]['text'] == var) or \
                    (b_dict[m[0][i]]['text'] == b_dict[m[1][i]]['text'] == b_dict[m[2][i]]['text'] == var) or \
                    (b_dict[m[0][0]]['text'] == b_dict[m[1][1]]['text'] == b_dict[m[2][2]]['text'] == var) or \
                    (b_dict[m[0][2]]['text'] == b_dict[m[1][1]]['text'] == b_dict[m[2][0]]['text'] == var)  :
                    messagebox.showinfo('GAME OVER', var + ' Player is Winner')
                    new_game()
    if count>8:
        messagebox.showinfo('GAME OVER', 'No Winner \n DRAW')
        new_game()
b_dict,b_list,m={},[],[]
def new_game():
    global count
    count = 0
    for i in range(1,4):
        t=[]
        for j in range(1,4):
            b = 'b'+str(i)+str(j)
            t.append(b)
            def func(arg=b):
                b_dict[arg].config(command=click(arg))
            b_dict[b] = Button(tic, text=' ',fg='red',font=('Times New Roman',10), width=12, height=5, command=func)
            b_dict[b].grid(row=i, column=j)
        m.append(t)
new_game()
tic.mainloop()