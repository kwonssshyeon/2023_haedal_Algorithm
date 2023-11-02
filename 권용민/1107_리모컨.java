import java.util.Scanner;

public class Main {
    static int targetChannel;
    static boolean[] isBroken;

    public static boolean canMove(int channel) {
        for (char ch : Integer.toString(channel).toCharArray()) {
            if (isBroken[Character.getNumericValue(ch)])
                return false;
        }
        return true;
    }

    public static int getMinPress() {
        int minPress = Math.abs(targetChannel - 100);

        // i는 +,- 버튼 수
        for (int i = 0; i < 500000; i++) {
            int channel = targetChannel - i;
            if (channel >= 0 && canMove(channel)) {
                minPress = Math.min(minPress, Integer.toString(channel).length() + i);
            }

            channel = targetChannel + i;
            if (canMove(channel)) {
                minPress = Math.min(minPress, Integer.toString(channel).length() + i);
            }

            if (minPress != Math.abs(targetChannel - 100))
                break;
        }
        return minPress;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        targetChannel = sc.nextInt();
        isBroken = new boolean[10];
        int brokenCount = sc.nextInt();
        for (int i = 0; i < brokenCount; ++i) {
            isBroken[sc.nextInt()] = true;
        }

        System.out.println(getMinPress());
    }
}

// gpt는 신이다
