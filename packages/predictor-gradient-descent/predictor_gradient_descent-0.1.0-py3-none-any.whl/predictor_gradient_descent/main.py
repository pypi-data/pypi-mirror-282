def output_predictor():
    """Predicts the Y value(output) for given test data points. The model must be trained with samples and output before.
    Just need to call the function. Accuracy of equation will depend on the no of samples entered..(Directly proportional)
    Equation should be of the form Ax(0) + Bx(1) + Cx(2) = Y, where A,B and C are coefficients of the linear equation.
    Input: No of samples, x(0),x(1) and x(2) of all the samples and their Y value
    Output: Y value for new set of x(0), x(1) and x(2)
    """
    test=[]
    n=int(input('ENTER THE NO OF SAMPLES AVAILABLE:'))
    print("Enter the samples:")
    for i in range(n):
        sample=[]
        print("\n")
        print("Enter the elements in sample",i+1,"\n")
        for j in range(4):
                if(j!=3):
                    print('Enter the value of X{}:'.format(j))
                else:
                    print('Enter the value of Y:')
                sample.append(float(input()))
        test.append(sample)           
    theta=[0,0,0]
    print("\n","MODEL IS BEING TRAINED..PLEASE WAIT!!","\n")
    J=0
    for k in range (1000000):
        temp_array=[]
        temp=[]
        for i in range(n):
                sum1=0
                for j in range(3):
                    sum1=sum1+(theta[j]*test[i][j])
                temp.append(sum1-test[i][j+1])
                temp_array.append((sum1-test[i][j+1])**2)
        J=((1/n)*sum(temp_array))
        alpha=0.02
        for i in range(3):
                sum2=0
                for j in range(n):
                    sum2=sum2+(temp[j]*test[j][i])
                theta[i]=theta[i]-(alpha*(1/n)*(sum2))  
    print("MODEL TRAINED!!!","\n") 
    print("ENTER THE NEW SAMPLE TO GET THE Y","\n")
    sample=[]
    for i in range(3):
        print("Enter the element X{}:".format(i))
        sample.append(float(input()))
    Y=(round(theta[0])*sample[0])+(round(theta[1])*sample[1])+(round(theta[2])*sample[2])
    print("PREDICTED Y:{}".format(Y))