// Finding sum of minimum subset among all subsets of an array with a given window size (win_size).
import java.util.Scanner;

class SW2{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// array size
		int n = sc.nextInt();
		
		// initializing memory
		int a[] = new int[n];

		// window size
		int win_size = sc.nextInt();

		// taking n inputs from user
		for(int i=0;i<n;i++){
			a[i] = sc.nextInt();
		}

		// logic for sliding window
		int i=0,j=0;
		int min = Integer.MAX_VALUE;
		int sum = 0;
		while(j<n){
			if(j-i+1 < win_size){
				sum+=a[j];
				j++;
			}
			else if(j-i+1 == win_size){
				sum+=a[j];
				if(min>sum){
					min = sum;
				}
				sum-=a[i];
				i++;
				j++;
			}
		}
		System.out.println("The min subarray sum is:"+min);
	}
}