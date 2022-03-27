/**
 * Given a number, return the fewest operations needed to reduce the number to 1.
 * Defined operations are:
 * - add 1,
 * - subtract 1,
 * - half the number
 * 
 * The solution should allow for integers up to 301 digits in length.
 */


import java.math.BigInteger;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

public class FewestOperations {
	private BigInteger key;
	private int size;
	
	public FewestOperations(BigInteger key, int size) {
		this.key = key;
		this.size = size;
	}
	
	
	public static boolean checkSet(Set<FewestOperations> set, FewestOperations node) {
		for (FewestOperations n : set) {
			if ((n.key).equals(node.key) && (node.size >= n.size)) {
				return true;
			}
		}
		set.add(node);
		return false;
	}
	
		
	public static int solution(String x) {
		BigInteger number = new BigInteger(x);
		
		Queue<FewestOperations> queue = new LinkedList<FewestOperations>();
		queue.add(new FewestOperations(number, 0));
		
		Set<FewestOperations> set = new HashSet<FewestOperations>();

		BigInteger zero = new BigInteger("0");
		BigInteger one = new BigInteger("1");
		BigInteger two = new BigInteger("2");
		
		int total = 0;
		while (!queue.isEmpty()) {
			FewestOperations node = queue.poll();
			if (checkSet(set, node)) {
				continue;
			}
			
			if ((node.key).equals(one)) {
				System.out.println("total loops this took was " + total);
				return node.size;
			}
			
			if ((node.key).mod(two).equals(zero)) {
				queue.add(new FewestOperations((node.key).divide(two), (node.size)+1));
			}
			else {
				queue.add(new FewestOperations((node.key).add(one), (node.size)+1));
				queue.add(new FewestOperations((node.key).subtract(one), (node.size)+1));
			}
			total += 1;
		}
		return -1;
	}

	public static void main(String[] args) {
		int answer = FewestOperations.solution("4");
		System.out.println("The solution was: " + answer);
		System.out.println("\n\n");
		
		int answer2 = FewestOperations.solution("15");
		System.out.println("The solution was: " + answer2);
		System.out.println("\n\n");
		
		int answer4 = FewestOperations.solution("999");
		System.out.println("The solution was: " + answer4);
		System.out.println("\n\n");
		
		int answer3 = FewestOperations.solution("143");
		System.out.println("The solution was: " + answer3);
		System.out.println("\n\n");
		
		int answer5 = FewestOperations.solution("99999999999999999");
		System.out.println("The solution was: " + answer5);
		System.out.println("\n\n");
	}
}
