from pylab import *
data = loadtxt('solflekker.txt', skiprows=1)

tid = data[:,0]
solflekker = data[:,1]

plot(tid,solflekker,color='forestgreen')
xlabel('Tid (mnd)')
ylabel('Gjennomsnittlig av solflekker')
