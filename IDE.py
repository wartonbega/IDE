import tkinter as tk
import os

text = ''
debut = ''
nombre = 0

parts=[]

def lettre(event):
    global text
    global debut
    debut = ''
    text = texte.get(0.0,tk.END)
    for i in range(len(text)):
        if text[i:i+1] == '\n' :
            break
        else:
            debut+=text[i]
    
def execute(event):
    global a
    global text
    file = open('./code','w')
    file.write(text[5:])
    file.close()

    a=str(os.popen("python3 code.py","r").read())
    output.insert(tk.END,a)
    if debut == 'html':
        os.popen('x-www-browser test.html','r')

def execu(event):
    global a
    global text
    global code
    global debut
    global nombre
    
    global onepart
    global center
    global secondpart
    
    code = text[len(debut):]
    if debut == 'python':
        file = open('./executeur/code.py','w')
        file.write(code)
        file.close()
        a=str(os.popen("python3 code.py").read())
        output.insert(tk.END,a+'\n')
        output.insert(tk.END,'out['+str(nombre)+']:')
        nombre+=1
    elif debut == 'html':
        index = 0
        index2 = 0
        onepart = ''
        center = ''
        secondpart = ''
        for i in range(len(code)):
            if code[i]=='<':
                index = i
                for x in range(len(code)):
                    if code[i+x]=='>':
                        index2 = i+x
                        onepart=code[index:index2+1]
                        for a in range(len(code)):
                            if code[a:a+len(onepart)+3] == '</'+onepart[1:-1]+'>':
                                secondpart='</'+onepart[1:-1]+'>'
                                center=code[index2+1:a]
                                print(center)
                                break
                        parts.append(onepart+center+secondpart)
                        break
                    
        print(parts)

def resave(event):
    global debut
    global titre
    global texte
    global inp
    code = text[len(debut):]
    tartre = inp.get()
    file = open('./fichiers/'+tartre,'w')
    file.write(code)
    file.close()
    titre.destroy()

def save(event):
    enregistrer()

def enregistrer():
    global inp
    global titre
    titre = tk.Tk()
    titre.title('enregister')
    inp = tk.Entry(titre)
    inp.pack()
    inp.bind('<Return>',resave)
    titre.mainloop()

def ope(event):
    global tatre
    global soap
    try:
        tutre = tatre.get()
        nom = ''
        extention = ''
        for i in range(len(tutre)):
            if tutre[i] == '.':
                extention+=tutre[i:]
                break
            else:
                nom+=tutre[i]
        
        file = open('./fichiers/'+tutre,'r')
        content = file.read()
        file.close()
        texte.delete(0.0,tk.END)
        
        if extention == '.py':
            texte.insert(tk.END,'python')
        elif extention == '.html':
            texte.insert(tk.END,'html')
        else:
            texte.insert(tk.END,"pas d'extention indiquée")
        texte.insert(tk.END,content)
        soap.destroy()
    except FileNotFoundError:
        tatre.delete(0,tk.END)
        tatre.insert(0,"ce fichier n'existe pas")

def ouvrir():
    global tatre
    global soap
    soap = tk.Tk()
    soap.title('ouvrir')
    tatre = tk.Entry(soap)
    tatre.pack()
    tatre.bind('<Return>',ope)
    soap.mainloop()
    
    

def ouvr(event):
    ouvrir()
           
window = tk.Tk()
window.title('IDE')
texte = tk.Text(window)
output = tk.Text(window)

texte.bind('<Key>',lettre)
texte.bind('<Control_L>'+'e',execu)
texte.bind('<Control_L>'+'s',save)
texte.bind('<Control_L>'+'o',ouvr)


but = tk.Button(window,text='executer',command=execu)
output.bind('<Return>')
enre = tk.Button(window,text='enregistrer',command=enregistrer)
browse = tk.Label(window,text = 'browse html')
browse.pack(side='right')
html_browse = ''

texte.pack()
output.pack()
output.insert(tk.END,'out['+str(nombre)+']:')
nombre+=1

file = open('./settings/sombre','r')
sombre = file.read()
file.close()
if sombre == 'oui':
    window.config(bg='black')
    output.config(bg='black',fg='white')
    texte.config(bg='black',fg='white')
    browse.config(bg='black',fg='white')


window.mainloop()