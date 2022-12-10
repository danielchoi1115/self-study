package Level_1;

import java.util.*;
//https://school.programmers.co.kr/learn/courses/30/lessons/138477
public class HallOfFame{
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];

        ArrayList<Integer> q = new ArrayList<>();
        for (int i = 0; i < score.length; i++) {
            if (q.size() < k){
                q.add(score[i]);
                Collections.sort(q);
                answer[i] = q.get(0);
                continue;
            }
            for (int j = 0; j < q.size(); j++) {
                if (q.get(j) < score[i]) {
                    q.remove(j);
                    q.add(j, score[i]);
                    break;
                }
            }
            Collections.sort(q);
            answer[i] = q.get(0);
        }

        return answer;
    }

}

// PriorityQueue 사용하는 법
//import java.util.*;
//class Solution {
//    public int[] solution(int k, int[] score) {
//        int[] answer = new int[score.length];
//        PriorityQueue<Integer> q = new PriorityQueue<>();
//        for(int i = 0; i < score.length; i++) {
//            q.add(score[i]);
//            if (q.size() > k) {
//                q.poll();
//            }
//            answer[i] = q.peek();
//        }
//        return answer;
//    }
//}