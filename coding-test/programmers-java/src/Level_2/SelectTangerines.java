package Level_2;

import java.util.*;
//https://school.programmers.co.kr/learn/courses/30/lessons/138476
public class SelectTangerines {
    public int solution(int k, int[] tangerine) {
        int answer = 0;

        HashMap<Integer, Integer> m = new HashMap<>();
        for (int t : tangerine) {
            Integer c = m.get(t);
            if (c == null) {
                m.put(t, 1);
            }
            else {
                m.put(t, c+1);
            }
        }
        LinkedHashMap<Integer, Integer> sortedMap = new LinkedHashMap<>();
        m.entrySet()
                .stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .forEachOrdered(x -> sortedMap.put(x.getKey(), x.getValue()));

        ArrayList<Integer> keyList = new ArrayList<>();
        for (Integer key: sortedMap.keySet()) {
            k -= sortedMap.get(key);
            keyList.add(key);
            if (k <= 0) {
                break;
            }
        }
        return keyList.size();
    }
}
