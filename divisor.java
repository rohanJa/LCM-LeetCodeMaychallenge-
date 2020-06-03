/**
   Author is Rohan Jain 
   Created at 10/03/2020, 02:06:07
**/

import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader;
import java.util.StringTokenizer; 
class divisor{
    static class FastReader 
    { 
        BufferedReader br; 
        StringTokenizer st; 
  
        public FastReader() 
        { 
            br = new BufferedReader(new
                     InputStreamReader(System.in)); 
        } 
  
        String next() 
        { 
            while (st == null || !st.hasMoreElements()) 
            { 
                try
                { 
                    st = new StringTokenizer(br.readLine()); 
                } 
                catch (IOException  e) 
                { 
                    e.printStackTrace(); 
                } 
            } 
            return st.nextToken(); 
        } 
  
        int nextInt() 
        { 
            return Integer.parseInt(next()); 
        } 
  
        long nextLong() 
        { 
            return Long.parseLong(next()); 
        } 
  
  
        String nextLine() 
        { 
            String str = ""; 
            try
            { 
                str = br.readLine(); 
            } 
            catch (IOException e) 
            { 
                e.printStackTrace(); 
            } 
            return str; 
        } 
    }
    
    static int divSum(int n){
        int sum=0;

        for(int i=1;i<=(int)Math.sqrt(n);i++){
            if(n%i==0){
                sum+=i;
                if(i!=1&&n/i!=i) 
                    sum+=n/i;       
               }
        }


        return sum;
    }

    public static void  main(String[] args) {
        FastReader s =new FastReader();
        StringBuilder sb = new StringBuilder("");
        int testcase=s.nextInt();
        while(testcase-->0){
            int in =s.nextInt();
            if(divSum(in)==in)
                sb.append("YES\n");
            else 
                sb.append("NO\n");
        }
        System.out.println(sb);
    }
}