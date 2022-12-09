import Level_1.*;
import Level_2.*;
import Level_3.*;

import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        AssignAirlines s = new AssignAirlines();

        int[][] gates = {{5,4,4,2}};
        int[] esti = {8,5,2};

        System.out.println(Arrays.toString(s.solution(gates, esti)));

        System.out.println(100/50);

    }
}