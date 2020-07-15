package Algorithm_Online_Study;

import java.util.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;


public class Sorting_Words_1181 {

	public static void main(String[] args) throws IOException{
		BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(BR.readLine());
		List<String> Basket = new ArrayList<String>(20000);
		for (int i = 0; i < T; i++) {
			String Temp = BR.readLine();
			if (!Basket.contains(Temp))
				Basket.add(Temp);
		}
		Comparator<String> MyComparator = new Comparator<String>() {
			public int compare(String x, String y) {
				if (x.length() > y.length()) {
					return 1;
				} else if (x.length() == y.length()) {
					return x.compareTo(y);
				}
				return -1;
			}
		};
		Collections.sort(Basket, MyComparator);
		for (int i = 0; i < Basket.size(); i++) {
			System.out.println(Basket.get(i));
		}

	}

}
