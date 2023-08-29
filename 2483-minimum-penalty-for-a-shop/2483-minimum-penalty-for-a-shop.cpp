class Solution {
public:
    int bestClosingTime(string customers) {
        int sz = customers.size();

        int nTotal = count(customers.begin(), customers.end(), 'N');
        int yTotal = count(customers.begin(), customers.end(), 'Y');
       
        if(nTotal == 0)return sz;

        int nCnt = 0, yCnt = 0, minPen = INT_MAX, minClose = INT_MAX;
       
        for(int indx = 0; indx < sz; indx++){
            int pen = nCnt + (yTotal - yCnt);
            if(pen < minPen){
                minPen = pen;
                minClose = indx;
            }
            if(customers[indx] == 'Y')yCnt++;
            else nCnt++;
        }
   
        int pen = nCnt;
        if(pen  < minPen){
            minPen = pen;
            minClose = sz;
        }

        return minClose;        
    }
};