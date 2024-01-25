#중력작용

#해당 코드는 학습용 코드로 직접 작성한 코드가 아님

import random
import sys
sys.setrecursionlimit(10**6)
def fw_append(arr,var):
    n=len(arr)
    w=(n&(-n))-1
    k=1
    while w>0:
        var+=arr[n-k]
        k<<=1
        w>>=1
    arr.append(var)
def fw_add(arr,index,delta):
    n=len(arr)
    while n>index:
        arr[index]+=delta
        w=index&(-index)
        index+=w
def fw_get(arr,index):
    rt=0
    while index:
        w=index&(-index)
        rt+=arr[index]
        index-=w
    return rt
class nd:
    def __init__(self,var,num):
        self.connect=[]
        self.num=num
        self.var=var
    def get_chain(self,num2chain,anc=None):
        max_chain=None
        max_l=0
        sumforfw=0
        max_fw=0

        for nd in self.connect:
            if nd==anc:
                continue
            else:
                fwsum,chain=nd.get_chain(num2chain,self)
                sumforfw+=fwsum
                chain.anc=self.num
                if max_l<chain.w:
                    max_l=chain.w
                    max_chain=chain
                    max_fw=fwsum
        if max_chain==None:
            new_nd=treap_nd(self.num,self.var)
            chain=treap(new_nd)
            num2chain[self.num]=chain
            return self.var,chain
        else:
            sumforfw-=max_fw
            max_chain.anc=None
            fw_append(max_chain.fw,sumforfw)
            sumforfw+=max_fw
            sumforfw+=self.var
            num2chain[self.num]=max_chain
            new_nd=treap_nd(self.num,self.var)
            max_chain.push_new(new_nd)
            return sumforfw,max_chain
class empty_nd:
    def __init__(self):
        self.w=0
        self.sum=0
class treap_nd:
    def __init__(self,num,var):
        self.w=1
        self.num=num
        self.var=var
        self.sum=var
        self.left=None
        self.right=None
        self.ran=random.random()
    
    def compran(self,nd):
        try:
            if self.ran>nd.ran:
                return True,True
            else:
                return False,False
        except:
            return True,False
class treap:
    def __init__(self,nd):
        self.root=nd
        self.num2pos={nd.num:0}
        self.fw=[0]
        self.anc=None
        self.w=1
    def push_new(self,nd):
        self.num2pos[nd.num]=self.w
        self.w+=1
        self.push(nd)
    def find_var(self,pos):
        now_nd=self.root
        while True:
            left_var=0
            if now_nd.left:
                left_var=now_nd.left.w
            if pos<left_var:
                now_nd=now_nd.left
            elif pos==left_var:
                return now_nd.var
            else:
                pos-=left_var+1
                now_nd=now_nd.right
    def push(self,nd):
        if nd.ran>self.root.ran:
            nd.left=self.root
            nd.sum+=self.root.sum
            nd.w+=self.root.w
            self.root=nd
        else:
            now_nd=self.root
            while True:
                now_nd.w+=1
                now_nd.sum+=nd.sum
                if now_nd.right:
                    if now_nd.right.ran>nd.ran:
                        now_nd=now_nd.right
                    else:
                        nd.left=now_nd.right
                        nd.sum+=nd.left.sum
                        nd.w+=nd.left.w
                        now_nd.right=nd
                        break
                else:
                    now_nd.right=nd
                    break
    def delete_nd(self,pos):
        anc_nds=[]
        isleft=True
        now_nd=self.root
        while True:
            left_var=0
            if now_nd.left:
                left_var=now_nd.left.w
            if pos<left_var:
                anc_nds.append(now_nd)
                now_nd=now_nd.left
                isleft=True
            elif pos==left_var:
                break
            else:
                pos-=left_var+1
                anc_nds.append(now_nd)
                now_nd=now_nd.right
                isleft=False
        del_var=now_nd.var
        anc=None
        for anc in anc_nds:
            anc.sum-=del_var
            anc.w-=1
        compS=now_nd.left
        compL=now_nd.right
        bp=True
        if anc==None:
            try:
                left_up,bp=compS.compran(compL)
                if not bp:
                    compL=empty_nd()
            except:
                left_up,bp=False,False
                compS=empty_nd()
            if left_up:
                self.root=compS
                compS.sum+=compL.sum
                compS.w+=compL.w
                anc=compS
                isleft=False
                compS=compS.right
            else:
                self.root=compL
                compL.sum+=compS.sum
                compL.w+=compS.w
                anc=compL
                isleft=True
                compL=compL.left
        while bp:
            try:
                left_up,bp=compS.compran(compL)
                if not bp:
                    compL = empty_nd()
            except:
                left_up = False
                bp = False
                compS = empty_nd()
                if compL == None:
                    if isleft:
                        anc.left = None
                    else:
                        anc.right = None
                    break
            if left_up:
                compS.sum += compL.sum
                compS.w += compL.w
                if isleft:
                    anc.left = compS
                else:
                    anc.right = compS
                anc = compS
                isleft = False
                compS = compS.right
            else:
                compL.sum += compS.sum
                compL.w += compS.w
                if isleft:
                    anc.left = compL
                else:
                    anc.right = compL
                anc = compL
                isleft = True
                compL = compL.left
        return now_nd.var    
    def get_sum(self,pos):
        fw_var=fw_get(self.fw,pos)
        now_nd=self.root
        now_sum=now_nd.sum
        while True:
            left_w=0
            if now_nd.left:
                left_w=now_nd.left.w
            if left_w>pos:
                now_sum-=now_nd.sum
                now_nd=now_nd.left
                now_sum+=now_nd.sum
            elif left_w==pos:
                if now_nd.right:
                    now_sum-=now_nd.right.sum
                return fw_var+now_sum
            else:
                pos-=left_w+1
                now_nd=now_nd.right
def subcalcul(u,w,dic,var):
    now_chain=dic[u]
    anc_u=now_chain.anc
    pos=now_chain.num2pos[u]
    if anc_u==None:
        new_node=treap_nd(0,w)
        now_chain.push(new_node)
        del_var=now_chain.delete_nd(pos)
        return del_var
    new_var=subcalcul(anc_u,w,dic,var)
    new_node=treap_nd(0,new_var)
    now_chain.push(new_node)
    del_var=now_chain.delete_nd(pos)
    anc_chain=dic[anc_u]
    anc_pos=anc_chain.num2pos[anc_u]
    fw_add(anc_chain.fw,anc_pos,new_var-var)
    return del_var
def qeury2(u,w,dic):
    now_chain=dic[u]
    anc_u=now_chain.anc 
    pos=now_chain.num2pos[u]
    if anc_u==None:
        new_node=treap_nd(0,w)
        now_chain.push(new_node)
        del_var=now_chain.delete_nd(pos)
        return del_var
    var=now_chain.find_var(pos)
    new_var=subcalcul(anc_u,w,dic,var)
    new_node=treap_nd(0,new_var)
    now_chain.push(new_node)
    del_var=now_chain.delete_nd(pos)
    anc_chain=dic[anc_u]
    anc_pos=anc_chain.num2pos[anc_u]
    fw_add(anc_chain.fw,anc_pos,new_var-del_var)
    return del_var    
def solution(values,edges,queries):
    answer=[]
    n=len(values)
    nodedic={i:nd(values[i-1],i) for i in range(1,n+1)}
    for i,j in edges:
        nodedic[j].connect.append(nodedic[i])
        nodedic[i].connect.append(nodedic[j])
    nd2chain={}
    nodedic[1].get_chain(nd2chain)
    for u,w in queries:
        chain=nd2chain[u]
        p=chain.num2pos[u]
        if w==-1:
            qn=chain.get_sum(p)
            answer.append(qn)
        else:
            qeury2(u,w,nd2chain)
    return answer

values=[1,10,100,1000,10000]
edges=[[1,2],[1,3],[2,4],[2,5]]
queries=[[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[4,1000],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[2,1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]]
print(solution(values,edges,queries))