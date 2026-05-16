<h1>Reproducible Randomness</h1>
<p>seed() Is Used To Fixes The Generation Process So That Same Random Output Is produced Every Time</p>

 <p> <em>Syntax</em>
    <code>
      np.random.seed(value)
    </code>
 </p>

 <p>E.G: 
    <code>
        import numpy as np <br>
        np.random.seed(42) <br>
        matrix=np.random.randint( <br>
          low=10,<br>
            high=50,<br>
            size=5<br>
        )<br>
        print(matrix)<br>
    </code>
 </p>