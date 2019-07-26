#用基于距离的edr算法对轨迹进行聚类
from sklearn.cluster import AgglomerativeClustering
import random
import cPickle
import numpy as np
import multiprocessing
import traj_dist.distance as tdist
import os
import read_data

from sklearn.metrics import accuracy_score

accs = []

def trajectoryAlldistance(i,trjs):
    trs_matrix = tdist.cdist(trjs, [trjs[i]],metric="edr",eps=0.05)
    #print(trs_matrix)
    cPickle.dump(trs_matrix, open('./distance_compution/EDR_distance/EDR_distance_' + str(i), 'w'))
    print 'complete: '+str(i)

def compute_distance():
    filelist = [ f for f in os.listdir('./distance_compution/EDR_distance/') ]
    for f in filelist:
        os.remove(os.path.join('./distance_compution/EDR_distance/', f))
    trjs = cPickle.load(open('./band_data/trajectories'))
    #print np.shape(trjs[0])
    trs_compare = []
    for tr in trjs:
        trarray = []
        for record in tr:
            trarray.append([record[1],record[2]])
        trs_compare.append(np.array(trarray))
    #print trs_compare
    pool = multiprocessing.Pool(processes=4)
    # print np.shape(distance)
    
    for i in range(len(trs_compare)):
        #print str(i)
        pool.apply_async(trajectoryAlldistance, (i, trs_compare))
    pool.close()
    pool.join()
    #trajectoryAlldistance(0, trs_compare)
    
def combainDistances(inputPath = './distance_compution/EDR_distance/'):
    files = os.listdir(inputPath)
    files_index = []
    for fn in files:
        i = int(fn.split('_')[2])
        files_index.append((fn,i))
    files_index.sort(key=lambda x:x[1])
    distances = []
    for fn in files_index:
        distance = []
        dis = cPickle.load(open(inputPath+fn[0]))
        for i in dis:
            distance.append(i[0])
        distances.append(np.array(distance))
    #print np.shape(distances)
    cPickle.dump(distances,open('./distances/'+inputPath.split('/')[2]+'_matrix','w'))

def kMedoids(D, k, tmax=100):
    # determine dimensions of distance matrix D
    m, n = D.shape

    if k > n:
        raise Exception('too many medoids')
    # randomly initialize an array of k medoid indices
    M = np.arange(n)
    np.random.shuffle(M)
    M = np.sort(M[:k])

    # create a copy of the array of medoid indices
    Mnew = np.copy(M)

    # initialize a dictionary to represent clusters
    C = {}
    for t in xrange(tmax):
        # determine clusters, i. e. arrays of data indices
        J = np.argmin(D[:,M], axis=1)
        for kappa in range(k):
            C[kappa] = np.where(J==kappa)[0]
        # update cluster medoids
        for kappa in range(k):
            J = np.mean(D[np.ix_(C[kappa],C[kappa])],axis=1)
            j = np.argmin(J)
            Mnew[kappa] = C[kappa][j]
        np.sort(Mnew)
        # check for convergence
        if np.array_equal(M, Mnew):
            break
        M = np.copy(Mnew)
    else:
        # final update of cluster memberships
        J = np.argmin(D[:,M], axis=1)
        for kappa in range(k):
            C[kappa] = np.where(J==kappa)[0]

    # return results
    return M, C

def distanceClusterTest(inputFile ='./distances/EDR_distance_matrix'):
    distanceMatrix = cPickle.load(open(inputFile))
    labels = np.array(cPickle.load(open('./band_data/labels')))
    
    #使用层次聚类
    clustering = AgglomerativeClustering(affinity='precomputed',linkage='average').fit(np.array(distanceMatrix))
    pred_labels = clustering.labels_
    acc = accuracy_score(labels, pred_labels)
    print acc
    
    '''
    #使用kMedoids聚类
    M,C = kMedoids(np.array(distanceMatrix),2)
    print(C)
    cresult = []
    for label in C:
        count1 = 0
        count2 = 0
        for point_idx in C[label]:
            if point_idx in range(0,sampleNum): count1+=1
            if point_idx in range(sampleNum, sampleNum+sampleNum2): count2 += 1
        cresult.append([label,count1,count2])
    #print(cresult)

    all  = 0.

    List1 = [[te[0],te[1]] for te in cresult]
    print '1:  '+str(List1)
    m = max([te[1] for te in List1])
    all = all + m
    print float(m) / sampleNum

    List2 = [[te[0],te[2]] for te in cresult]
    print '2:  '+str(List2)
    m = max([te[1] for te in List2])
    all = all + m
    print float(m) / sampleNum2

    print 'overall'
    print all/(sampleNum+sampleNum2)
    print '---------------------------------'
    '''
    

if __name__ == '__main__':
    for i in range(20):
        read_data.read_data('alpha',1,i+1)  #将最大通道和能量信息读取成轨迹信息，前两个参数为指定的频率段和condition
        compute_distance()
        combainDistances(inputPath='./distance_compution/EDR_distance/')
        distanceClusterTest(inputFile='./distances/EDR_distance_matrix')