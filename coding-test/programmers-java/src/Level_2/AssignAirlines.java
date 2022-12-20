package Level_2;


import java.util.*;
import java.util.stream.Collectors;

public class AssignAirlines {
    public int[] solution(int[][] gates, int[] airlines){
        ArrayList<Integer> answer = new ArrayList<>();


//        Arrays.sort(gates[0]);
        for (int day = 0; day < gates.length; day++) {
            ArrayList<Integer> airlineList = new ArrayList<>();
            for (int i: airlines) {
                airlineList.add(i);
            }

            Collections.sort(airlineList, Collections.reverseOrder());
            Arrays.sort(gates[day]);
            for (int g = gates[day].length-1; g >= 0; g--) {
                if (airlineList.isEmpty()) break;
                airlineList.set(0, airlineList.get(0)-gates[day][g]);
                if (airlineList.get(0) <= 0) {
                    airlineList.remove(0);
                }
                Collections.sort(airlineList, Collections.reverseOrder());
            }
            int s = 0;
            for (Integer j: airlineList){
                s += j;
            }
            if (s == 0) {
                answer.add(day+1);
            }
        }
        if (answer.isEmpty()) {
            int[] answerArray = {-1};
            return answerArray;
        }
        int[] answerArray = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            answerArray[i] = answer.get(i);
        }
        Arrays.sort(answerArray);
        return answerArray;
    }

}



