import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    static Node[] arr = new Node[26];

    public static class Node {
        private char val;
        private char leftNode = '.';
        private char rightNode = '.';
        public Node(char val, char leftNode, char rightNode) {
            this.val = val;
            this.leftNode = leftNode;
            this.rightNode = rightNode;
        }

        public void preorderTraversal(int index) {
            char val = (char)(index + 'A');
            char lc = arr[index].leftNode;
            char rc = arr[index].rightNode;

            System.out.print(val);
            if (arr[index].leftNode!= '.')
                preorderTraversal(lc - 'A');
            if (arr[index].rightNode != '.')
                preorderTraversal(rc - 'A');
        }

        public void inorderTraversal(int index) {
            char val = (char)(index + 'A');
            char lc = arr[index].leftNode;
            char rc = arr[index].rightNode;

            if (arr[index].leftNode!= '.')
                inorderTraversal(lc - 'A');
            System.out.print(val);
            if (arr[index].rightNode != '.')
                inorderTraversal(rc - 'A');
        }

        public void postorderTraversal(int index) {
            char val = (char)(index + 'A');
            char lc = arr[index].leftNode;
            char rc = arr[index].rightNode;

            if (arr[index].leftNode!= '.')
                postorderTraversal(lc - 'A');
            if (arr[index].rightNode != '.')
                postorderTraversal(rc - 'A');
            System.out.print(val);
        }
    }

    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i =0; i < n; ++i) {
            String line = br.readLine();
            int index = line.charAt(0) - 65;
            arr[index] = new Node(line.charAt(0), line.charAt(2), line.charAt(4));
        }

        arr[0].preorderTraversal(0);
        System.out.println();
        arr[0].inorderTraversal(0);
        System.out.println();
        arr[0].postorderTraversal(0);
        System.out.println();
    }
}

/*
c로 풀면 금방읹데 진짜
자바.................*/
