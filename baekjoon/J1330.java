import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class J1330 {
  public static void main(String[] args) throws IOException {
    // Create the reader and writer.
    BufferedReader reader = new BufferedReader(
        new InputStreamReader(System.in));
    BufferedWriter writer = new BufferedWriter(
        new OutputStreamWriter(System.out));

    // Read inputs.
    String[] parts = reader.readLine().split(" ");
    int numA = Integer.parseInt(parts[0]);
    int numB = Integer.parseInt(parts[1]);

    // Print the output.
    String output;
    if (numA > numB) {
      output = ">\n";
    } else if (numA < numB) {
      output = "<\n";
    } else {
      output = "==\n";
    }
    writer.write(output);
    writer.flush();
  }
}
