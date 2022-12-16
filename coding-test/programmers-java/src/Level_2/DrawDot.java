package Level_2;
//https://school.programmers.co.kr/learn/courses/30/lessons/140107
public class DrawDot {
    public double dist(int x1, int x2) {
        return Math.sqrt(Math.pow(x1, 2) + Math.pow(x2, 2));
    }
    public long solution(int k, int d) {
        long answer = 0;
        int base = (int) Math.ceil((float) d / (float) k);
        for (int i = 0; i < d; i+=k) {
            while (dist(k*(base-1), i) > d) {
                base -= 1;
            }
            answer += base;

        }
        if (d % k == 0) {
            answer += 2;
        }
        return answer;
    }
}
