package Level_2;
//https://school.programmers.co.kr/learn/courses/30/lessons/135807
import java.util.*;
public class DividingCards {
    public ArrayList<Integer> get_cd(int num) {
        ArrayList<Integer> cd = new ArrayList<>(); // 약수 저장 ArrayList
        for(int i = 1; i <= (int) Math.sqrt(num); i++){
            if(num % i == 0){ // 약수 중 작은 수 저장
                cd.add(i);
                if(num / i != i){ // 약수 중 큰 수 저장
                    cd.add(num / i);
                }
            }
        }
        cd.sort(Comparator.reverseOrder());
        return cd;
    }
    public int solution(int[] arrayA, int[] arrayB) {
        int answer = 0;
        int min_a = Arrays.stream(arrayA).min().getAsInt();
        int min_b = Arrays.stream(arrayB).min().getAsInt();

        ArrayList<Integer> cd_a = get_cd(min_a);
        ArrayList<Integer> cd_b = get_cd(min_b);

        for (Integer a_candidate: cd_a) {
            boolean valid = true;
            for (int a: arrayA) {
                if (a % a_candidate != 0) {
                    valid = false;
                    break;
                }
            }
            if (!valid) continue;
            for (int b: arrayB) {
                if (b % a_candidate == 0) {
                    valid = false;
                    break;
                }
            }
            if (valid && a_candidate > answer) answer = a_candidate;
        }
        for (Integer b_candidate: cd_b) {
            boolean valid = true;
            for (int a: arrayA) {
                if (a % b_candidate == 0) {
                    valid = false;
                    break;
                }
            }
            if (!valid) continue;
            for (int b: arrayB) {
                if (b % b_candidate != 0) {
                    valid = false;
                    break;
                }
            }
            if (valid && b_candidate > answer) answer = b_candidate;
        }
        return answer;
    }

}
