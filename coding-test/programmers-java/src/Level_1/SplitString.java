package Level_1;
import Interfaces.*;
//https://school.programmers.co.kr/learn/courses/30/lessons/140108
public class SplitString implements Solution<String>{
    public int solution(String s) {
        int answer = 0;
        char x = 'a';
        int cnt_x = 0;
        int cnt_nx = 0;
        for (int i = 0; i < s.length(); i++) {
            if (cnt_x == 0 && cnt_nx == 0){
                x = s.charAt(i);
                cnt_x += 1;
            }
            else {
                if (x == s.charAt(i)) {
                    cnt_x += 1;
                }
                else {
                    cnt_nx += 1;
                }
                if (cnt_x == cnt_nx) {
                    answer += 1;
                    cnt_x = 0;
                    cnt_nx = 0;
                }
            }
        }
        if (cnt_x != cnt_nx) {
            answer+= 1;
        }
        return answer;
    }
}