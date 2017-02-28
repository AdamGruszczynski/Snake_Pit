
# coding: utf-8

# In[72]:

import random
import time
import networkx as nx
import matplotlib as plt
get_ipython().magic(u'matplotlib inline')

start = time.time()

def person():
  #Generates a dictionary of person "objects" that have replicated survey submissions
  runtime = time.time()
  pdict1 = {}
  pdict2 = {}
  sub = []
  names = random.sample(range(30,301), 200)
  count = len(names)
  c1 = count/2
  for k in names[:int(c1)]:
    kid = k
    maxc = 1
    while maxc != 0:
      sub = random.sample(range(1,31), 30)
      if len(sub) > 24 and len(sub) <= 30:
        top = slice(0,4)
        bot = slice(len(sub)-4,len(sub))
      elif len(sub) > 12 and len(sub) <= 24:
        top = slice(0,3)
        bot = slice(len(sub)-3,len(sub))
      elif len(sub) > 3 and len(sub) <= 12:
        top = slice(0,2)
        bot = slice(len(sub)-2,len(sub))
      elif len(sub) > 2:
        top = slice(0,1)
        bot = slice(len(sub)-1,len(sub))
      else:
        top = slice(0)
        bot = (len(sub)-1)
      sub2 = sub[top] + sub[bot]
      #print(sub2)
      maxc -= 1
    pdict1[kid] = sub2
    sub2 = []
    #print ("Person " + str(kid) + " added.")
    count -= 1
  for k in names[int(c1):]:
    kid = k
    maxc = 1
    while maxc != 0:
      sub = random.sample(range(1,31), 30)
      #print(sub)
      #print(type(sub))
      top = slice(0,4)
      bot = slice(26,30)
      sub2 = sub[top] + sub[bot]
      #print(sub2)
      maxc -= 1
    pdict2[kid] = sub2
    sub2 = []
    #print ("Person " + str(kid) + " added.")
  endtime = time.time()
  print(endtime-runtime)
  return pdict1, pdict2


def networkgen(idict):
  #Develop a network by generating nodes and assigning values from person method, takes dictionary as argument
  g = nx.Graph()
  #print(idict[0].values())
  for per, val in idict[0].items():
    #print(per, val)
    #print(idict[0][per])
    #print("This is the dictionary ")
    g.add_node(str(per), answers = str(val))
    #g.node[per]["Answers"] = val
  #nx.set_node_attributes(g,'Answers',idict[0])
  #print(g.nodes(data=True))
  for per2, val2 in idict[1].items():
    #print(per)
    g.add_node(str(per2), answers = str(val2))
    #print(g.node[person])
  
  
  #print(g.nodes(data=True))
  return g

#print(type(netk))

def compare(key1, key2):
  #Compares integers in 2 lists at a topological level, requires dictionary as argument
  matchcount = 0
  total = 0
  for i, j in zip(key1, key2):
    if i == j:
        #print ("Match")
        matchcount += 1
        total += 1
    else:
        total += 1
        #print ("No Match")
  mper = matchcount/total
  #print ("The total match % is " + '{percent:.2%}'.format(percent=mper))
  return mper
  
#compare(test['p1'],test['p2'])
        
def cluster(idict):
  #Separate groups of people by matching percentage, requires dictionary as argument
  #assert(type(idict) == dict)
  identical = {}
  high = {}
  low = {}
  noMatches = {}
  for k1 in idict[0]:
    #print(k1)
    for k2 in idict[1]:
      #print(k2)
      mper = compare(idict[0][k1],idict[1][k2])
      if mper == float(1.0):
        identical[k1,k2] = mper
      elif mper < float(1.0) and mper >= float(0.2):
        high[k1,k2] = mper
      elif mper < float(0.2) and mper > float(0.0):
        low[k1,k2] = mper
      else:
        noMatches[k1,k2] = mper
  #print("Identical, " + "Length = " + str(len(identical)) + " " + str(identical))
  #print("High, " + "Length = " + str(len(high)) + " " + str(high))
  #print("Low, " + "Length = " + str(len(low)) + " " + str(low))
  elist = identical, high, low, noMatches
  return elist
#NOTE: THIS CLUSTER TEST OMITS DUPLICATES, TAKES SLIGHTLY LONGER HOWEVER - 

#NOTE2: CAN SAVE ON TIME BY ELIMINATING STORAGE OF 0% MATCHES - DONE

def edgegen(network, elist):
  #takes network and lists containing compare() values and assigns edges to all nodes with a weight > 0
  #print(elist)
  for k1,k2 in elist[0]:
    network.add_edge(k1,k2, weight = elist[0][k1,k2])
    print(k1,k2,network.edge[k1][k2])
  for k1,k2 in elist[1]:
    network.add_edge(k1,k2, weight = elist[1][k1,k2])
    print(k1,k2,network.edge[k1][k2])
  for k1,k2 in elist[2]:
    network.add_edge(k1,k2, weight = elist[2][k1,k2])
    print(k1,k2,network.edge[k1][k2])
  for k1,k2 in elist[3]:
    network.add_edge(k1,k2, weight = elist[3][k1,k2]+.01)
    #print(k1,k2,network.edge[k1][k2])
  return network
  
#netk = networkgen(test)
#finalnet = edgegen(netk, ctes

"""
from github import Github

def main():
    # Step 1: Create a Github instance:
    g = Github("usrname", "passwd")
    repo = g.get_user().get_repo('mathematics')

    # Step 2: Prepare files to upload to GitHub
    files = ['mathematics/numerical_analysis/regression_analysis/simple_regression_analysis.py', 'mathematics/numerical_analysis/regression_analysis/simple_regression_analysis.png']

    # Step 3: Make a commit and push
    commit_message = 'Add simple regression analysis'

    tree = repo.get_git_tree(sha)
    repo.create_git_commit(commit_message, tree, [])
    repo.push()

if __name__ == '__main__':
    main()
"""
test = person()
ctest = cluster(test)
net = networkgen(test)
full = edgegen(net,ctest)
nx.write_graphml(full, 'trialnet.graphml')
trial = nx.read_graphml('trialnet.graphml')
for node in trial.edges(data=True):
    print(node)
    

end = time.time()
print(end-start)

#nx.draw(trial)



# In[ ]:



