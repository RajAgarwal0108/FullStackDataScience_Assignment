from tkinter import *
import tkinter as tk
import os
import logging as lg

lg.basicConfig(filename = '/home/raj/Ineuron_Project/LogFile.log', level = lg.INFO)

try:
	def merge_txt():
		merge_btn =  Button(root,text = "merge.txt",fg = 'blue',command = merge,border = 2,font =('Helvetica',24))
		merge_btn.place(x=700,y=50)
		lg.info('merge.txt created')
		



	def merge():
		print('merging')
		s = txt.get()
		print(s)
		"""
		merging all the files into a single file

		"""
		
		if s == '.txt':
			lg.info("merging all .txt files")
			T.delete('1.0',tk.END)
			T.insert(tk.END,"Merging.....\n")
			with open("newfile.txt",'a+') as f:
				for path, direc, name in os.walk('/home/raj/Downloads'):
					for i in name:
						name, ext = os.path.splitext(i)
						if ext.lower() == '.txt' and i!="newfile.txt":
							with open(os.path.join(path,i),'r') as fr:
								try:
									f.write(str(fr.read()))
								except Exception as e:
									print("error",e)
									lg.error(str(e))
									T.configure(fg='red')
									T.insert(tk.END,e)
			T.insert(tk.END,"merging sucessful\n")
		else :
			T.delete('1.0',tk.END)
			T.insert(tk.END,"Cannot merge this type of file.\n")
		merge_txt()
			


	def txt_files():
		lg.info('searching for text file')
		"""
		To display all the .txt file
		"""
		for path,direc,name in os.walk(os.getcwd()):
			for i in name:
				name,ext = os.path.splitext(i)
				if ext.lower() == '.txt':
					T.insert(tk.END,i)
					T.insert(tk.END,"\n")
		print("end")
		T.insert(tk.END,"END")
		T.insert(tk.END,"\n")
		merge_txt()




	
		

	def parsing(s):
		c = 0
		lg.info('searching for filename'+str(s))
		T.delete('1.0',tk.END)
		T.configure(fg = 'blue')
		f_name , f_ext = os.path.splitext(s)
		if f_ext == "":
			T.insert(tk.END,"provide an extension\n")
		for path,direc,name in os.walk(os.getcwd()):
			for i in name:
				f_na , f_e = os.path.splitext(i)
				if (i.lower() == s.lower()) or (f_name == f_na) :
					print(i)
					T.insert(tk.END,os.path.join(path,i),"\n")
					T.insert(tk.END,'\n')
					c+=1
				if s[0] == "*":
					for path,direc,name in os.walk(os.getcwd()):
						for i in name:
							f_na , f_e = os.path.splitext(i)
							if f_e == f_ext.lower():
								print(i)
								T.insert(tk.END,os.path.join(path,i),"\n")
								T.insert(tk.END,'\n')
								c+=1
		if c==0 and f_ext!="":
			T.insert(tk.END,"no matching files found\n")




	def search():
		lg.info("clicked on search")
		try:
			s_bar = txt.get()
			if s_bar == " " or "":
				T.insert(tk.END,"Search something\n")
			elif s_bar[0] == " ":
				T.insert(tk.END,"Unexpected Indent\n")
			elif s_bar[0] == '.':
				if s_bar.lower() == ".txt":
					txt_files()
				else:
					parsing("*"+s_bar)
			else:
				parsing(s_bar)
		except Exception as e:
			lg.error(str(e))
			T.insert(tk.END,str(e))
			T.insert(tk.END,"\n")
	def set_path():
		pth = cur_fol.get()
		try:
			os.chdir(pth)
		except Exception as e:
			lg.error("path error."+str(e))
			print("error",e)
			T.insert(tk.END,e,"\n")
		T.insert(tk.END,"\n")
		T.insert(tk.END,"folder set to:")
		T.insert(tk.END,os.getcwd())
		lg.info("path changed to"+ str(os.getcwd()))
		cur_fol.configure(state = 'normal')
		cur_fol.delete(0,END)
		cur_fol.insert(0,os.getcwd())
		

		


	root = Tk()

	root.title("Files")





	label = Label(root,text = "Enter file extension:",font =('Chilanka Bold',14))
	label.place(x=150,y=75,anchor = CENTER)

	root.geometry('1000x700')

	txt = Entry(root,width = 20,border = 4,font =('Chilanka',24))
	txt.place(relx = 0.5, rely = 0.1, anchor = CENTER)


	btn = Button(root,text = "search",fg = 'red',command = search,border = 2,font =('Helvetica',24))
	btn.place(relx = 0.5, rely = 0.2,anchor = CENTER)

	set_btn = Button(root,text = 'set',command = set_path,fg = 'green', font = ('Helvetica',20))
	set_btn.place(x = 10,y=10)

	cur_fol = Entry(root,width = 40,bg = 'grey', border = 2,fg = 'yellow',font = ('Helvetica bold',14))
	cur_fol.place(x = 300,y=10)
	cur_fol.insert(0,os.getcwd())



	T = Text(root,border = 8,height = 25,width = 70,font=('Chilanka',14))

	T.place(x=40,y=170)





	root.mainloop()
except Exception as e:
	print("main error",e)
	lg.error(str(e))
lg.shutdown()
