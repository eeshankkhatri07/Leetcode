class Solution {
    public static int totalFruit(int[] tree) {
        Map<Integer, Integer> map = new HashMap<>();
        int start = 0, end = 0, counter = 0, len = 0;

        while (end < tree.length) {
            int a = tree[end];
            map.put(a, map.getOrDefault(a, 0) + 1);

            if (map.get(a) == 1) counter++;
            end++;

            while (counter > 2) {
                int temp = tree[start];
                map.put(temp, map.get(temp) - 1);
                if (map.get(temp) == 0) counter--;
                start++;
            }

            len = Math.max(len, end - start);
        }

        return len;
    }
}