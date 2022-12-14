package Level_2;

import java.util.*;

//https://school.programmers.co.kr/learn/courses/30/lessons/42885
public class LifeBoat {
        public int solution(int[] people, int limit) {
            int answer = 0;
            Arrays.sort(people);
            int l = 0;
            int r = people.length-1;

            while (l <= r) {
                if (people[l] + people[r] <= limit) {
                    l += 1;
                }
                r -= 1;
                answer += 1;
            }

            return answer;
        }
}
