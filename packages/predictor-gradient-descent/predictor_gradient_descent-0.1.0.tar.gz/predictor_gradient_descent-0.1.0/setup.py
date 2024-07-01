# setup.py

from setuptools import setup, find_packages

setup(
    name='predictor_gradient_descent',
    version='0.1.0',
    packages=find_packages(),
    #install_requires=[]
    #extras_require={
       # 'dev': [
        #    'matplotlib',
        #    'unittest',
       # ],
   # },
    author='K ABHISHEK MENON',
    author_email='kabhishekmenon@gmail.com',
    description="""A library which Predicts the Y value(output) for given test data points using gradient descent algorithm.
      Use:    import gradient_descent as gd
              gd.output_predictor() 
              #and run the code..You will be guided.
              # Predicts the Y value(output) for given test data points. The model must be trained with samples and output before.
    Just need to call the function. Accuracy of equation will depend on the no of samples entered..(Directly proportional)
    Equation should be of the form Ax(0) + Bx(1) + Cx(2) = Y, where A,B and C are coefficients of the linear equation.
    Input: No of samples, x(0),x(1) and x(2) of all the samples and their Y value
    Output: Y value for new set of x(0), x(1) and x(2)
              """,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    #url='https://github.com/yourusername/gradient_descent',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
