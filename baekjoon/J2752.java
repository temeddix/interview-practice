import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class J2752 {
  public static void main(String[] args) throws IOException {
    var reader = new BufferedReader(new InputStreamReader(System.in));
    var writer = new BufferedWriter(new OutputStreamWriter(System.out));
    var numbers = Arrays.stream(reader.readLine().split(" "))
        .mapToInt(Integer::parseInt).sorted().toArray();
    for (int number : numbers) {
      writer.write(Integer.toString(number) + " ");
    }
    writer.flush();
  }
}
