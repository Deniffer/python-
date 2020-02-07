# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 10:19:32 2019

@author: HASEE"""
import copy
class Node(object):
	def __init__(self,value,data,tag=False):
		self.value=value
		self.data=data
		self.child_list=[]
		self.tag=tag
	def add_child(self,node):
		self.child_list.append(node)


def init():
	root=Node('A',1,tag=True)
	B=Node('B',2)
	root.add_child(B)
	root.add_child(Node('C',3))
	D=Node('D',2)
	root.add_child(D)
	B.add_child(Node('E',3))
	B.add_child(Node('F',4))
	B.add_child(Node('G',2))
	D.add_child(Node('H',1))
	D.add_child(Node('I',3))
	D.add_child(Node('J',4))
	return root

def DFS(cur,path=[],data=[],data_all=[]):
	path.append(cur.value)
	data.append(cur.data)
	if cur.child_list!=[]:
		for node in cur.child_list:
			if node.tag==False:
				#path.append(node.value)
				#data.append(node.data)
				node.tag==True
				t_path=copy.deepcopy(path)
				t_data=copy.deepcopy(data)
				DFS(node,t_path,t_data)
			if node.tag==True:
				continue
	else:
		data_all+=path
		path.pop()
		data.pop()
        
	return path,data
if __name__=="__main__":
    root=init()
    print(DFS(root))