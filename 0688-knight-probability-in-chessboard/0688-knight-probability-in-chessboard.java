class Solution {
    public double knightProbability(int n, int k, int row, int column) {
        if(k==0)
        {
            return (double)1;
        }
        double dp[][] = new double[n][n];
        dp[row][column]=1;
        int val[][] = {{-2,1},{-1,2},{1,2},{2,1},{-2,-1},{-1,-2},{1,-2},{2,-1}};
        for(int ind=1;ind<=k;ind++)
        {
            double dp1[][] = new double[n][n];
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<n;j++)
                {
                    if(dp[i][j]!=0)
                    {
                        for(int iterate[] : val)
                        {
                            int ind_x=i+iterate[0];
                            int ind_y=j+iterate[1];
                            if(ind_x>=0 && ind_y>=0 && ind_x<n && ind_y<n)
                            {
                                dp1[ind_x][ind_y]+=dp[i][j]/8.0;
                            }
                        }
                    }
                }
            }
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<n;j++)
                {
                    dp[i][j]=dp1[i][j];
                }
            }
        }
        double ans=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                ans+=dp[i][j];
            }
        }
        return ans;
    }
}