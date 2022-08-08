import java.util.function.Consumer;
import java.util.*;
class UsingAnonymusFunctions{
	public static void main(String[] args) {
		List<Integer> lst = Arrays.asList(1,2,3,4,5);

		Consumer<Integer> c = (Integer i) -> System.out.println(i);

		lst.forEach(c);



	}
}