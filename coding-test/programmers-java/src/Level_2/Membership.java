package Level_2;

import java.util.Arrays;

public class Membership {
    public int[] solution(int[] periods, int[][] payments, int[] estimates) {
        int[] answer = new int[2];

        int VIPnow = 0;
        int VIPnext = 0;

        for (int i = 0; i < periods.length; i++) {
            if (periods[i]+1 < 24) {
                continue;
            }
            int sumNow = Arrays.stream(payments[i]).sum();
            int sumNext = sumNow - payments[i][0] + estimates[i];

            int t, tp;
            if (periods[i] <= 59) {
                t = 900000;
                tp = 23;
            } else {
                t = 600000;
                tp = 59;
            }

            if ((periods[i] == tp || sumNow >= t) && sumNext < t) {
                VIPnow += 1;
            } else if ((periods[i] == tp ||sumNow < t) && sumNext >= t) {
                VIPnext += 1;
            }

        }
        answer[0] = VIPnext;
        answer[1] = VIPnow;

        return answer;
    }
}
