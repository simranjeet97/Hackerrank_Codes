"""
 * * * * * * * * *   * * * * * * * * * 
  * * * * * * * *     * * * * * * * * 
   * * * * * * *       * * * * * * * 
    * * * * * *         * * * * * * 
     * * * * *           * * * * * 
      * * * *             * * * * 
       * * *               * * * 
        * *                 * * 
         *                   * 
                              
         *                   * 
        * *                 * * 
       * * *               * * * 
      * * * *             * * * * 
     * * * * *           * * * * * 
    * * * * * *         * * * * * * 
   * * * * * * *       * * * * * * * 
  * * * * * * * *     * * * * * * * * 
 * * * * * * * * *   * * * * * * * * * 
"""
for i in range(1,10):
    for j in range(1,i+1):
        print("", end=" ")
    for k in range(10,i,-1):
        print("*", end=" ")
    for j in range(1,i+1):
        print(" ", end=" ")
    for l in range(10,i, -1):
        print("*", end=" ")
    print()

for i in range(0,10):
    for l in range(10,i,-1):
        print(" ", end="")
    for k in range(1,i+1):
        print("*", end=" ")
    for j in range(10,i,-1):
        print("", end="  ")
    for l in range(1,i+1):
        print("*", end=" ")
    print()
