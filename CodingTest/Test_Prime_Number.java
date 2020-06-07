package CodingTest;

import java.util.Scanner;

public class Test_Prime_Number {

	public int prime_number(int num) {

		int result = 0;
		boolean[] primeNumber = new boolean[num + 1];

		for (int i = 2; i <= num; i++) {
			primeNumber[i] = true; // 2~num 까지 true로 초기화
		}
		// 제곱근 구하기
		int root = (int) Math.sqrt(num);

		for (int i = 2; i <= root; i++) { // 2부터 num의 제곱근까지 검사하기
			if (primeNumber[i] = true) { // i번째 수가 소수였을 경우!
				for (int j = i; i * j <= num; j++) { // i 번째를 제외하고 그 배수를 전부 false로 초기화!(배수는 소수가 아니야!)
					primeNumber[i * j] = false;
				}
			}
		}

		for (int i = 2; i <= num; i++) {
			if (primeNumber[i] == true) { // 소수의 갯수 세기
				result++;
			}

		}

		return result;
	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);

		Test_Prime_Number c = new Test_Prime_Number();

		System.out.println(c.prime_number(10));
		System.out.println(c.prime_number(5));

		int a = input.nextInt();
		System.out.println(c.prime_number(a));

	}

}