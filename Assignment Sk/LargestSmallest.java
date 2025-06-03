import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;
public class LargestSmallest {

@Test
public void CheckTheArrayOfLargestSmallest() {
RangeOfnumber rane = new RangeOfnumber();
int[] input = {5,6,10,15,20};
int[] range = rane.numberRanges(input);
int[] result = {15};
assertArrayEquals(result,range);

   }

}