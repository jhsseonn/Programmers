public class GCD {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        answer[0] = gcd(n, m);
        answer[1] = (n * m) / gcd(n, m);
        return answer;
    }
    
    public static int gcd(int p, int q) {
        if (q==0) return p;
        else return gcd(q, p%q);
    }
    
    // public static void main (String[] args) {
    //     Solution solution = new Solution();
    //     System.out.println(Arrays.toString(solution.solution(3, 12)));
    // }
}