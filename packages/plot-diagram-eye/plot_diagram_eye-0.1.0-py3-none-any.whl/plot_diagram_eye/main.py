import numpy as np
import matplotlib.pyplot as plt
def get_filter(name,T,rolloff= None):
     """
    Generate a filter function.

    Parameters:
    name (str): The type of filter to generate ('rect', 'rc', 'rrc').
    T (float): Symbol period.
    rolloff (float, optional): Roll-off factor for 'rc' and 'rrc' filters.

    Returns:
    function: A function representing the specified filter.

    Available Filters:
    - 'rect': Rectangular filter.
    - 'rc': Raised cosine filter.
    - 'rrc': Root raised cosine filter.
    """

     def rc(t,beta):
        return((np.sinc(t)*(np.cos(np.pi*beta*t)))/(1-((2*beta*t)**2)))
     def rrc(t,beta):
        return(np.sin(np.pi*t*(1-beta))+(4*beta*t*np.cos(np.pi*t*(1-beta))))/(np.pi*t*(1-((4*beta*t)**2)))
     if name=='rect':
        return lambda t:(abs(t/T)<0.5).astype(int)
    
     if name=='rc':
        return lambda t:rc(t/T,rolloff)
     if name=='rrc':
        return lambda t:rrc(t/T,rolloff)
def get_signal(data,g,T,Fs):


    """
    Generate a signal by convolving the data with the provided filter.

    Parameters:
    data (array-like): Input binary data stream.
    g (function): Filter function.
    T(int): Symbol period. 
    Fs(int): Sampling frequency.

    Returns:
    tuple:
        t (numpy.ndarray): Time vector.
        x (numpy.ndarray): Generated signal.
    """

    t=np.arange(-2*T, (len(data)+2)*T,1/Fs)
    for k in range(len(data)):
        x=sum(data[k]*g(t-k*T) for k in range(len(data)))
    return(t,x)
def drawFullEyeDiagram(x,T,Fs):

    """
    Generate and plot the eye diagram of the signal.

    Parameters:
    x (numpy.ndarray): Input signal.
    T(int): Symbol period. 
    Fs(int): Sampling frequency.

    Returns:
    None. The function plots the eye diagram.
    """

    samples_perT=Fs*T
    samples_perWindow=2*Fs*T
    startInd=2*samples_perT
    parts=[]
    for k in range(int(len(x)/samples_perT)-6):
        parts.append(x[startInd+k*samples_perT+np.arange(samples_perWindow)])
    parts=np.array(parts).T
    T_parts = np.arange(-T,T,1/Fs)
    plt.plot(T_parts,parts,'b-')
    plt.show()
    plt.tight_layout()
