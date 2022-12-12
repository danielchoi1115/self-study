package Level_2;

import java.util.*;
//https://school.programmers.co.kr/learn/courses/30/lessons/142085
public class DefenseGame {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int j : enemy) {
            if (k > 0) {
                pq.add(j);
                k -= 1;
                answer += 1;
                continue;
            }
            Integer root = pq.peek();
            if (root != null && j > root) {
                if (n - root < 0) break;
                n -= root;
                pq.poll();
                pq.add(j);
            } else {
                if (n - j < 0) break;
                n -= j;
            }
            answer += 1;
        }

        return answer;
    }

}
