import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class HamburgerDiet {
	
	static int N, L, maxScore;
	static int[] score, kcal;

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            maxScore = 0;
            N = sc.nextInt();
            L = sc.nextInt();
            
            score = new int[N];
            kcal = new int[N];
            
            for (int i=0; i<N; i++) {
            	score[i] = sc.nextInt();
            	kcal[i] = sc.nextInt();
            }
            
            hamburger(0, 0, 0);

            System.out.printf("#%d %d\n", test_case, maxScore);
		}
		
	}
	
	public static void hamburger(int cnt, int scoreSum, int kcalSum) {
		if (kcalSum > L) return;
		if (cnt == N) {
			maxScore = Math.max(maxScore, scoreSum);
            return;
		}
		
		hamburger(cnt+1, scoreSum+score[cnt], kcalSum+kcal[cnt]);
		hamburger(cnt+1, scoreSum, kcalSum);
	}

}
