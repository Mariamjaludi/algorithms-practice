import java.math.*;
import java.util.regex.*;


class Difference {
  private int[] elements;
  public int maximumDifference;
  Difference(int[] el){
      elements = el;
      maximumDifference = 0;
  }
  public void computeDifference(){
      int max = this.elements[0];
      int min = this.elements[0];
      for(int i = 1; i < elements.length;i++)
      {
          max = elements[i] >= max ? elements[i] : max;
          min = elements[i] <= min ? elements[i] : min;
      }
      this.maximumDifference = max - min;
  }
}

public class Solution {

  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int n = sc.nextInt();
      int[] a = new int[n];
      for (int i = 0; i < n; i++) {
          a[i] = sc.nextInt();
      }
      sc.close();

      Difference difference = new Difference(a);

      difference.computeDifference();

      System.out.print(difference.maximumDifference);
  }
}
