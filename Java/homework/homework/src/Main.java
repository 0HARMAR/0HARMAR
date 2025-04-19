import StringJoiner;
public class Main {
    public static void main(String[] args) {
        int lineCount = 0;
        StringJoiner currentLine = new StringJoiner(" ");

        for (int num = 1000; num <= 9999; num++) {
            int d1 = num / 1000;
            int d2 = (num / 100) % 10;
            int d3 = (num / 10) % 10;
            int d4 = num % 10;

            // 检查各位是否包含0
            if (d1 == 0 || d2 == 0 || d3 == 0 || d4 == 0) {
                continue;
            }

            // 检查各位和是否为10
            if (d1 + d2 + d3 + d4 == 10) {
                currentLine.add(Integer.toString(num));
                lineCount++;

                // 每行满14个数字时换行
                if (lineCount == 14) {
                    System.out.println(currentLine.toString());
                    currentLine = new StringJoiner(" ");
                    lineCount = 0;
                }
            }
        }

        // 输出剩余未满一行的数字
        if (lineCount > 0) {
            System.out.println(currentLine.toString());
        }
    }
}