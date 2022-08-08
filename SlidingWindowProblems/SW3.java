// Find 1st -ve number in each subarray of size(win_size).

import java.util.Scanner;
import java.util.ArrayDeque;
//import java.util.Stack;
class SW3{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		int []a = new int[n];

		int win_size = sc.nextInt();

		for(int i=0;i<n;i++){
			a[i] = sc.nextInt();
		}

		ArrayDeque<Integer> dq = new ArrayDeque<>();
		//Stack<Integer> stack = new Stack<>();

		int i=0,j=0;

		while(j<n){
			if(j-i+1 < win_size){
				if(a[j]<0){
					dq.offer(a[j]);
				}
				j++;
			}
			else if(j-i+1 == win_size){
				if(a[j]<0){
					dq.offer(a[j]);
				}
				if(a[i]==dq.peekFirst())
				{
				System.out.print(dq.pollFirst()+" ");
				}
				else{
					System.out.print(0+" ");
				}
				i++;
				j++;
			}

		}
	}
}