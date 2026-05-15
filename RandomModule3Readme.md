<h1>Random Module Choice ()</h1>
 <p>Def: It selects Value Randomly From A Given DataSet </p>

<h4><strong>Syntax:</strong>
    <code>np.random.choice(a,size=None,replace=True,p=None)</code>
    
</h4>
<p>Where:
    a=input range
    size=number of Output 
    replace= Allows To Repetition Or Not
    p=Probability Weighted
</p>
<code>
    import numpy as np
    matrix=np.random.choice([1,2,3,4,5])
    print(matrix)
    Possible Output:
         5
</code>
<h2>Multiple Random Selections</h2>
 <code>
    matrix=np.random.choice(
        [10,20,30,40] 
        size=5 
    )
 </code>
 <p>Possible Output :
    [10,20,30,20,40]
 </p>
 <em>IMP OBS 🤷‍♂️</em>
 <hr>
  <p>replace=True (Means Here repetition is Allowed(☑️))</p>
  <p>replace=False (Means Here repetition is not  Allowed(❌))</p>

  <h1><em>Refer  RandomModule3.py For Assignments
   Follow For More..... :) </em></h1>