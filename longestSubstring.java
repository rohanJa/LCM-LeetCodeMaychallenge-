/**
   Author is Rohan Jain 
   Created at 14/03/2020, 18:43:45
**/

import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader;
import java.util.StringTokenizer; 
class longestSubstring{
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
  
        double nextDouble() 
        { 
            return Double.parseDouble(next()); 
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

    static int calc(char[] a,char[] b){
        int result=0;

        int [][]arr = new int[a.length+1][b.length+1];

        for(int i=0;i<b.length;i++)
            arr[0][i]=0;
        for(int i=0;i<a.length;i++)
            arr[i][0]=0;

        for(int i=1;i<=a.length;i++){
            for(int j=1;j<=b.length;j++){
                if(a[i-1]==b[j-1]){
                    arr[i][j]=arr[i-1][j-1]+1;
                    result=Math.max(arr[i][j],result);
                }
                else    
                    arr[i][j]=0;
            }
        }
        return result;
    }
    public static void  main(String[] args) {
        FastReader s =new FastReader();

        String s1=s.nextLine();
        String s2=s.nextLine();
        System.out.println(calc(s1.toCharArray(),s2.toCharArray()));
        
        System.out.println(calc(s1.toCharArray(),s2.toCharArray()));
    }
}