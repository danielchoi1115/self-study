package Level_2;

import java.lang.reflect.Array;
import java.util.*;
public class BuyGames {
    public int solution(int[][] games) {
        int answer = 0;

        int[] dTable = new int[games.length];

        HashMap<Integer, HashMap<Integer, Integer>> dMap = new HashMap<>();

        for (int i = 0; i < games.length; i++) {
            if (!dMap.containsKey(games[i][1])) {
                HashMap<Integer, Integer> game = new HashMap<>();
                dMap.put(games[i][1], game);
            }
            dMap.get(games[i][1]).put(i, games[i][0]/games[i][2]);

            int Dday = games[i][1];
            dTable[Dday] = Math.max(dTable[Dday], games[i][0]/games[i][2]);
        }

        HashMap<Integer, Integer> pMap = new HashMap<>();

        for (int i = 0; i<games.length; i++) {
            pMap.put(i, games[i][0]);
        }

        List<Integer> keySetList = new ArrayList<>(pMap.keySet());

        Collections.sort(keySetList, (o1, o2) -> (pMap.get(o1).compareTo(pMap.get(o2))));

        int day = 0;
        int gCount = 0;
        while (gCount < games.length) {
            HashMap<Integer, Integer> dList = dMap.get(day);
        }

            return answer;
    }
}
