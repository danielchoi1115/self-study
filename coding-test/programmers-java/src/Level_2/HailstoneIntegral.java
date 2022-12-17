package Level_2;

import java.util.*;
//https://school.programmers.co.kr/learn/courses/30/lessons/134239
public class HailstoneIntegral {
    public double[] solution(int k, int[][] ranges) {
        double[] answer = new double[ranges.length];
        ArrayList<Integer> list = new ArrayList<>();
        list.add(k);
        while (k > 1) {
            if (k % 2 == 0) {
                k = k/2;
            }
            else k = k*3 + 1;
            list.add(k);
        }
        for (int i = 0; i < ranges.length; i++) {
            int l = ranges[i][0];
            int r = list.size() + ranges[i][1] - 1;
            if (r < l || r >= list.size() || l < 0) {
                answer[i] = -1.0;
                continue;
            }
            answer[i] = 0;
            for (int j = l; j < r; j++) {
                answer[i] += trapezoidArea(list.get(j), list.get(j+1), 1);
            }
        }
        return answer;
    }
    public double trapezoidArea(int a, int b, int h) {
        return 0.5 * (a+b) * h;
    }
}
