package Level_2;

import java.util.*;
public class DeliveryBox {
    public int solution(int[] order) {
        int answer = 0;

        Stack<Integer> s = new Stack<>();
        int orderPos = 0;
        int currentOrder = 1;
        while(orderPos < order.length) {
            if (order[orderPos] == currentOrder){
                answer += 1;
                orderPos += 1;
                currentOrder ++;
                continue;
            }
            if (!s.isEmpty() && order[orderPos] == s.peek()){
                s.pop();
                orderPos += 1;
                answer += 1;
                continue;
            }
            if (currentOrder > order.length) {
                break;
            }
            s.push(currentOrder);
            currentOrder ++;
        }

        return answer;
    }

}
