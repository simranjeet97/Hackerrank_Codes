"""

*                              
*  *                           * 
*  *  *                       *  * 
*  *  *  *                   *  *  * 
*  *  *  *  *               *  *  *  * 
*  *  *  *  *  *           *  *  *  *  * 
*  *  *  *  *  *  *       *  *  *  *  *  * 
*  *  *  *  *  *  *  *   *  *  *  *  *  *  * 
*  *  *  *  *  *  *  * * * *  *  *  *  *  *  * 
*  *  *  *  *  *  *  *   *  *  *  *  *  *  * 
*  *  *  *  *  *  *       *  *  *  *  *  * 
*  *  *  *  *  *           *  *  *  *  * 
*  *  *  *  *               *  *  *  * 
*  *  *  *                   *  *  * 
*  *  *                       *  * 
*  *                           * 

"""

for i in range(0, 7 + 1): 
        for j in range(0, 2 * 7 + 1): 
              
            # Left part of pattern 
            if (i < j): 
                print("", end = " "); 
            else: 
                print("*", end = " "); 
                  
            # Right part of pattern 
            if (i <= ((2 * 7) - j)): 
                print("", end = " "); 
            else: 
                print("*", end = " "); 
        print(""); 
      
    # This is lower  
    # half of pattern 
for i in range(0, 7 + 1):
    for j in range(0, 2 * 7 + 1):
        # Left part of pattern
        if (i > (7 - j + 1)): 
            print("", end = " "); 
        else: 
            print("*", end = " ");
        # Right part of pattern 
        if ((i + 7) > j): 
            print("", end = " ");
        else: 
            print("*", end = " "); 
    print(""); 
